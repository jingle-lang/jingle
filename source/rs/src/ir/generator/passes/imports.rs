/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:50 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{cell::RefMut, mem, rc::Rc};

use crate::{
    ast::{Import, Module},
    error::{Error, Errors, Res},
    ir::{generator::passes::PreMIRPass, result::ToMIRResult, Imports, MModule, MutRc},
};

fn find_module<'a>(
    module: &MModule,
    modules: &'a [MutRc<MModule>],
    import: &Import,
) -> Res<&'a MutRc<MModule>> {
    modules
        .iter()
        .find(|m| m.try_borrow().ok().map(|m| Rc::clone(&m.path)) == Some(Rc::clone(&import.path)))
        .or_err(&module.path, &import.symbol, "Unknown module.")
}

fn get_imports(module: &mut MModule, is_export: bool) -> &mut Imports {
    if is_export {
        &mut module.exports
    } else {
        &mut module.imports
    }
}

/// This pass imports all types.
pub struct ImportTypes();

impl PreMIRPass for ImportTypes {
    fn run(
        &mut self,
        ast: &mut Module,
        module: MutRc<MModule>,
        modules: &[MutRc<MModule>],
    ) -> Result<(), Errors> {
        module.borrow_mut().imports.ast = mem::replace(&mut ast.imports, vec![]);
        module.borrow_mut().exports.ast = mem::replace(&mut ast.exports, vec![]);

        drain_mod_imports(
            modules,
            module,
            &mut |modules, module, import, is_export| {
                let src_module_rc = find_module(module, modules, import)?;
                let src_module = src_module_rc.borrow();

                if &import.symbol.lexeme[..] == "*" {
                    for name in &src_module.local_names {
                        module.try_reserve_name_rc(name, &import.symbol, false)?;
                    }

                    get_imports(module, is_export)
                        .modules
                        .insert(Rc::clone(&src_module.path), Rc::clone(src_module_rc));
                    Ok(false)
                } else {
                    let name = Rc::clone(&import.symbol.lexeme);
                    let ty = src_module.find_local_type(&name);

                    if let Some(ty) = ty {
                        get_imports(module, is_export).types.insert(name, ty);
                    } else {
                        let proto = src_module.find_local_prototype(&name);
                        match proto {
                            Some(p) => get_imports(module, is_export).protos.insert(name, p),
                            None => return Ok(false),
                        };
                    }

                    module.try_reserve_name(&import.symbol, false)?;
                    Ok(true)
                }
            },
        )
    }
}

/// This pass imports all globals.
pub struct ImportGlobals();

impl PreMIRPass for ImportGlobals {
    fn run(
        &mut self,
        _ast: &mut Module,
        module: MutRc<MModule>,
        modules: &[MutRc<MModule>],
    ) -> Result<(), Errors> {
        drain_mod_imports(
            modules,
            module,
            &mut |modules, module, import, is_export| {
                let src_module_rc = find_module(module, modules, import)?;
                let src_module = src_module_rc.borrow();

                if &import.symbol.lexeme[..] == "*" {
                    Ok(true)
                } else {
                    module.try_reserve_name(&import.symbol, false)?;
                    let name = Rc::clone(&import.symbol.lexeme);
                    let global = src_module.find_local_global(&name);

                    if let Some(global) = global {
                        get_imports(module, is_export).globals.insert(name, global);
                        Ok(true)
                    } else {
                        Err(Error::new(
                            &import.symbol,
                            "MIR",
                            "Unknown module member.".to_string(),
                            &module.path,
                        ))
                    }
                }
            },
        )
    }
}

/// This function runs `drain_filter` on all imports in the given module, using the given function as a filter.
/// If the filter returns Err, the function exits prematurely and returns the error.
fn drain_mod_imports(
    modules: &[MutRc<MModule>],
    module: MutRc<MModule>,
    cond: &mut dyn FnMut(&[MutRc<MModule>], &mut RefMut<MModule>, &Import, bool) -> Res<bool>,
) -> Result<(), Errors> {
    let mut errs = Vec::new();
    let mut module = module.borrow_mut();

    // This can be replaced with drain_filter once stabilized:
    // https://github.com/rust-lang/rust/issues/43244
    let mut i = 0;
    while i != module.imports.ast.len() {
        let import = module.imports.ast.remove(i);
        if !cond(modules, &mut module, &import, false)
            .map_err(|e| errs.push(e))
            .unwrap_or(false)
        {
            module.imports.ast.insert(i, import);
            i += 1;
        }
    }

    i = 0;
    while i != module.exports.ast.len() {
        let export = module.exports.ast.remove(i);
        if !cond(modules, &mut module, &export, true)
            .map_err(|e| errs.push(e))
            .unwrap_or(false)
        {
            module.exports.ast.insert(i, export);
            i += 1;
        }
    }

    if errs.is_empty() {
        Ok(())
    } else {
        Err(Errors(errs, Rc::clone(&module.src)))
    }
}
