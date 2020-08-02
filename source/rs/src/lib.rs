/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:51 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

#![feature(drain_filter)]
#![warn(clippy::pedantic)]
#![allow(clippy::needless_pass_by_value)]
#![allow(clippy::unneeded_field_pattern)] // Causes false positives with enum_method derives
#![allow(clippy::ptr_arg)] // Causes false positives with hash map string keys

// Too pedantic:
#![allow(clippy::must_use_candidate)]
#![allow(clippy::use_self)]
#![allow(clippy::module_name_repetitions)]
#![allow(clippy::too_many_lines)]
#![allow(clippy::similar_names)]
#![allow(clippy::cast_possible_truncation)]
#![allow(clippy::cast_lossless)]
#![allow(clippy::new_without_default)]
#![allow(clippy::if_not_else)]
#![allow(clippy::default_trait_access)]
#![allow(clippy::try_err)]
#![allow(clippy::unused_self)]
#![allow(clippy::option_map_unit_fn)]
#![allow(clippy::find_map)]
#![allow(clippy::inline_always)]

#[macro_use]
extern crate enum_methods;
#[macro_use]
#[cfg(test)]
extern crate lazy_static;

use std::{env, fs, path::PathBuf, rc::Rc};

use crate::{
    ast::module::{Import, Module, ModulePath},
    error::{Error, Errors},
    codegen::IRGenerator,
    scanner::token::Token,
    ir::{generator::module::PassRunner, MModule, MutRc},
};

pub mod ast;
//#[cfg(test)]
//pub mod bench;
pub mod error;
pub mod codegen;
pub mod scanner;
pub mod ir;
pub mod parser;
#[cfg(test)]
pub mod tests;

pub fn parse_source(input: Vec<PathBuf>) -> Result<Vec<Module>, Vec<Errors>> {
    let mut modules = Vec::new();
    for path in input {
        make_modules(path, &mut ModulePath(vec![]), &mut modules)?;
    }
    Ok(modules)
}

fn make_modules(
    input: PathBuf,
    path: &mut ModulePath,
    modules: &mut Vec<Module>,
) -> Result<(), Vec<Errors>> {
    path.0.push(stem_to_rc_str(&input));

    if let Ok(dir) = input.read_dir() {
        let mut errors = Vec::new();
        for file in dir {
            let file = file.expect("Failed to read file").path();

            // If the file is named 'module.jn', it should have the
            // containing directory as its module path.
            let result = if file.file_name().unwrap() == "module.jn" {
                parse_module(file, path).map(|m| modules.push(m))
            } else {
                make_modules(file, path, modules)
            };

            if let Err(mut errs) = result {
                errors.append(&mut errs);
            }
        }

        if !errors.is_empty() {
            return Err(errors);
        }
    } else if *input
        .extension()
        .map(|ext| ext == "jn")
        .get_or_insert(false)
    {
        // If 'input' is a .jn file; parse it if true
        modules.push(parse_module(input, path)?);
    }

    path.0.pop();
    Ok(())
}

fn parse_module(input: PathBuf, path: &mut ModulePath) -> Result<Module, Vec<Errors>> {
    let code = Rc::new(fs::read_to_string(&input).expect("Failed to read file."));
    let mut module = Module::new(path, &code);

    fill_module(code, &mut module).map_err(|e| vec![e])?;
    Ok(module)
}

fn fill_module(code: Rc<String>, module: &mut Module) -> Result<(), Errors> {
    let lexer = scanner::Lexer::new(&code);
    let parser = parser::Parser::new(lexer, Rc::clone(&module.path));
    parser.parse(module).map_err(|errs| Errors(errs, code))
}

pub fn auto_import_prelude(modules: &mut Vec<Module>) {
    let prelude_import = Import {
        path: Rc::new(ModulePath(vec![
            Rc::new("std".to_string()),
            Rc::new("prelude".to_string()),
        ])),
        symbol: Token::generic_identifier("*".to_string()),
    };

    for module in modules
        .iter_mut()
        .filter(|module| module.path != prelude_import.path)
    {
        module.imports.push(prelude_import.clone())
    }
}

pub fn compile_mir(modules: Vec<Module>) -> Result<Vec<MutRc<MModule>>, Vec<Errors>> {
    let pool = PassRunner::new(&modules);
    pool.execute(modules)
}

pub fn compile_ir(modules: Vec<MutRc<MModule>>) -> inkwell::module::Module {
    let gen = IRGenerator::new();
    gen.generate(modules)
}

pub fn stem_to_rc_str(path: &PathBuf) -> Rc<String> {
    Rc::new(path.file_stem().unwrap().to_str().unwrap().to_string())
}

pub fn find_std_module() -> Result<PathBuf, &'static str> {
    let mut local_std = env::current_dir().expect("Failed to get current directory!");
    local_std.push("std");
    if local_std.exists() {
        return Ok(local_std);
    }

    let mut user_std = dirs::data_dir().expect("Failed to get home directory!");
    user_std.push("jinglec");
    user_std.push("std");
    if user_std.exists() {
        return Ok(user_std);
    }

    let system_std = PathBuf::from("/usr/local/lib/jinglec/std");
    if system_std.exists() {
        return Ok(system_std);
    }

    Err("Failed to find standard library. Please make sure to follow the installation instructions.")
}
