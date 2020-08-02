/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:50 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::rc::Rc;

use crate::{
    ast::Module,
    error::Errors,
    ir::{
        generator::{builder::Context, passes::PreMIRPass},
        nodes::{ADTType, Type, ADT},
        MModule, MutRc,
    },
};

/// This pass defines all types inside the module.
/// It only creates a stub MIR definition and inserts it as a type;
/// nothing is filled or created.
pub struct DeclareTypes();

impl PreMIRPass for DeclareTypes {
    fn run(
        &mut self,
        ast: &mut Module,
        module: MutRc<MModule>,
        _modules: &[MutRc<MModule>],
    ) -> Result<(), Errors> {
        let mut module = module.borrow_mut();
        let mut errs = Vec::new();

        for adt in ast.adts.drain(..) {
            let name = adt.name.clone();
            module
                .try_reserve_name(&name, true)
                .map_err(|e| errs.push(e))
                .ok();

            let adt = ADT::from_ast(adt, Context::default(), None);
            module
                .types
                .insert(Rc::clone(&name.lexeme), Type::Adt(Rc::clone(&adt)));

            if let ADTType::Enum { cases } = &adt.borrow().ty {
                for case in cases.values() {
                    module
                        .types
                        .insert(Rc::clone(&case.borrow().name), Type::Adt(Rc::clone(&case)));
                }
            };
        }

        if errs.is_empty() {
            Ok(())
        } else {
            Err(Errors(errs, Rc::clone(&module.src)))
        }
    }
}
