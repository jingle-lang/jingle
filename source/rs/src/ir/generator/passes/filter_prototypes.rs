/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:54 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{cell::RefCell, rc::Rc};

use crate::{
    ast::Module,
    error::{Error, Errors},
    ir::{
        generator::passes::PreMIRPass,
        nodes::{ProtoAST, Prototype},
        MModule, MutRc,
    },
};

/// This pass removes all types/functions with generic parameters
/// from the AST list, since they are handled separately.
pub struct FilterPrototypes();

impl PreMIRPass for FilterPrototypes {
    fn run(
        &mut self,
        ast: &mut Module,
        module_rc: MutRc<MModule>,
        _modules: &[MutRc<MModule>],
    ) -> Result<(), Errors> {
        let mut module = module_rc.borrow_mut();
        let mut errs = Vec::new();

        let class_iter = ast
            .adts
            .drain_filter(|a| a.generics.is_some())
            .map(|a| (a.name.clone(), ProtoAST::ADT(Rc::new(a))));
        let func_iter = ast
            .functions
            .drain_filter(|f| f.sig.generics.is_some())
            .map(|f| (f.sig.name.clone(), ProtoAST::Function(Rc::new(f))));

        for (name, ast) in class_iter.chain(func_iter) {
            module
                .try_reserve_name(&name, true)
                .map_err(|e| errs.push(e))
                .ok();
            let call_parameters = ast
                .get_call_parameters()
                .map_err(|(e, tok)| errs.push(Error::new(&tok, "MIR", e, &module.path)))
                .unwrap_or_else(|()| vec![]); // value won't matter since it'll abort due to the error anyway
            module.protos.insert(
                Rc::clone(&name.lexeme),
                Rc::new(Prototype {
                    name: name.lexeme,
                    instances: Default::default(),
                    impls: RefCell::new(vec![]),
                    module: Rc::clone(&module_rc),
                    ast,
                    call_parameters,
                }),
            );
        }

        if errs.is_empty() {
            Ok(())
        } else {
            Err(Errors(errs, Rc::clone(&module.src)))
        }
    }
}
