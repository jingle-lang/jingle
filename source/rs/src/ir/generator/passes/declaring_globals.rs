/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/28/19 10:20 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::rc::Rc;

use either::Either;

use crate::{
    ast,
    ast::{
        declaration::{FuncSignature, FunctionParam},
        module::ModulePath,
        Module,
    },
    error::{Errors, Res},
    scanner::token::Token,
    ir::{
        generator::{builder::MIRBuilder, intrinsics::INTRINSICS, passes::PreMIRPass},
        mutrc_new,
        nodes::{Function, Type, Variable},
        result::ToMIRResult,
        MModule, MutRc,
    },
};

/// This pass defines all globals inside the module; currently only functions.
/// It only creates a signature and inserts it into the module;
/// no actual body/code is generated at this stage.
/// Since it requires types for its signature, this pass has to run
/// after `DeclareTypes`.
pub struct DeclareGlobals();

impl PreMIRPass for DeclareGlobals {
    fn run(
        &mut self,
        ast: &mut Module,
        module: MutRc<MModule>,
        _modules: &[MutRc<MModule>],
    ) -> Result<(), Errors> {
        let mut errs = Vec::new();
        let builder = MIRBuilder::new(&module);

        for function in ast.functions.drain(..) {
            let is_ext = function.body.is_none();
            create_function(&builder, Either::Right(function), is_ext, None)
                .map_err(|e| errs.push(e))
                .ok();
        }

        if errs.is_empty() {
            Ok(())
        } else {
            Err(Errors(errs, Rc::clone(&module.borrow().src)))
        }
    }
}

/// Creates a function.
/// `this_arg` indicates that the function is a method
/// with some kind of receiver, with the 'this' parameter
/// added to the 0th position of the parameters and the
/// function renamed to '$receiver-$name'.
pub fn create_function(
    builder: &MIRBuilder,
    func: Either<&FuncSignature, ast::Function>,
    is_external: bool,
    this_arg: Option<FunctionParam>,
) -> Res<Rc<Variable>> {
    let name_token = match &func {
        Either::Left(sig) => &sig.name,
        Either::Right(func) => &func.sig.name,
    }
    .clone();

    let (full_name, name) =
        get_and_reserve_func_name(&builder.module, name_token.clone(), &this_arg, is_external)?;
    let function = generate_mir_fn(builder, func, full_name, this_arg)?;
    let global = Variable::new(false, Type::Function(function), &name);
    insert_global_and_type(&builder.module, &global);
    maybe_set_main_fn(&builder.module.borrow().path, &global, name_token)?;
    Ok(global)
}

fn get_and_reserve_func_name(
    module: &MutRc<MModule>,
    mut name: Token,
    this_param: &Option<FunctionParam>,
    is_external: bool,
) -> Res<(String, Rc<String>)> {
    if let Some(arg) = &this_param {
        name.lexeme = Rc::new(format!("{}-{}", arg.type_, name.lexeme));
    }
    module.borrow_mut().try_reserve_name(&name, true)?;

    let full_name = if is_external {
        String::clone(&name.lexeme)
    } else {
        get_function_name(&module.borrow().path, &name.lexeme)
    };
    Ok((full_name, Rc::clone(&name.lexeme)))
}

pub fn get_function_name(path: &Rc<ModulePath>, func_name: &Rc<String>) -> String {
    if func_name.as_ref() == "main" {
        func_name.to_string()
    } else {
        format!("{}:{}", path, func_name)
    }
}

pub fn generate_mir_fn(
    builder: &MIRBuilder,
    func: Either<&FuncSignature, ast::Function>,
    name: String,
    this_arg: Option<FunctionParam>,
) -> Res<MutRc<Function>> {
    let func_sig = match &func {
        Either::Left(sig) => sig,
        Either::Right(func) => &func.sig,
    };

    let ret_type = func_sig
        .return_type
        .as_ref()
        .map_or(Ok(Type::None), |ty| builder.find_type(ty))?;

    let mut parameters = Vec::with_capacity(func_sig.parameters.len());
    for param in this_arg.iter().chain(func_sig.parameters.iter()) {
        parameters.push(Variable::new(
            false,
            builder.find_type(&param.type_)?,
            &param.name.lexeme,
        ));
    }

    Ok(mutrc_new(Function {
        name,
        parameters,
        exprs: Vec::with_capacity(4),
        variables: Default::default(),
        ret_type,
        context: builder.context.clone(),
        ast: func.right().map(Rc::new),
        gc_inspected: false,
    }))
}

pub fn insert_global_and_type(module: &MutRc<MModule>, global: &Rc<Variable>) {
    module
        .borrow_mut()
        .globals
        .insert(Rc::clone(&global.name), Rc::clone(&global));
    module
        .borrow_mut()
        .types
        .insert(Rc::clone(&global.name), global.type_.clone());
}

fn maybe_set_main_fn(path: &Rc<ModulePath>, global: &Rc<Variable>, err_tok: Token) -> Res<()> {
    if &global.name[..] == "main" {
        INTRINSICS
            .with(|i| i.borrow_mut().set_main_fn(global))
            .or_err(path, &err_tok, "Can't define main multiple times.")?;
    }
    Ok(())
}
