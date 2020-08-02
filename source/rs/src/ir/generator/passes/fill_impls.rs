/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:50 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{collections::HashMap, mem, rc::Rc};

use either::Either::Left;

use crate::{
    ast,
    ast::declaration::{Function, FunctionParam},
    error::{Error, Res},
    ir::{
        generator::{
            builder::MIRBuilder,
            passes::{
                declaring_globals::create_function,
                declaring_iface_impls::get_or_create_iface_impls, ModulePass, PassType,
            },
            MIRGenerator,
        },
        nodes::{AbstractMethod, Type, Variable},
        result::ToMIRResult,
    },
};

/// This pass defines all methods on interface impls.
/// The boolean indicates if the pass has already been run at least once.
pub struct FillIfaceImpls();

impl ModulePass for FillIfaceImpls {
    fn get_type(&self) -> PassType {
        PassType::AllTypes
    }

    fn run_type(&self, gen: &mut MIRGenerator, ty: Type) -> Res<()> {
        let impls = get_or_create_iface_impls(&ty);
        let mut impls = impls.borrow_mut();

        let mut methods = HashMap::with_capacity(impls.interfaces.len() * 2);
        for iface_impl in impls.interfaces.values_mut() {
            gen.builder.switch_module(&iface_impl.module);

            let ast = Rc::clone(&iface_impl.ast);
            let iface = Rc::clone(&iface_impl.iface);
            let this_arg = FunctionParam::this_param_(&ast.implementor);

            for method in &ast.methods {
                let iface = iface.borrow();
                let iface_method = iface.dyn_methods.get(&method.sig.name.lexeme).or_err(
                    &gen.builder.path,
                    &method.sig.name,
                    "Method is not defined in interface.",
                )?;

                let mir_method = create_function(
                    &gen.builder,
                    Left(&method.sig),
                    false,
                    Some(this_arg.clone()),
                )?;
                iface_impl
                    .methods
                    .insert(Rc::clone(&method.sig.name.lexeme), Rc::clone(&mir_method));
                if methods.contains_key(&method.sig.name.lexeme) {
                    methods.remove(&method.sig.name.lexeme);
                } else {
                    methods.insert(Rc::clone(&method.sig.name.lexeme), Rc::clone(&mir_method));
                }

                check_equal_signature(&gen.builder, method, mir_method, iface_method)?;
            }

            if iface.borrow().methods.len() > iface_impl.methods.len() {
                return Err(Error::new(
                    &ast.iface.get_token(),
                    "MIR",
                    "Missing methods in interface impl.".to_string(),
                    &gen.builder.path,
                ));
            }
        }

        mem::replace(&mut impls.methods, methods);
        Ok(())
    }
}

/// Ensures that the implemented interface method matches the expected signature.
fn check_equal_signature(
    builder: &MIRBuilder,
    method: &Function,
    mir_method: Rc<Variable>,
    iface_method: &AbstractMethod,
) -> Res<()> {
    let mir_method = mir_method.type_.as_function();
    let mir_method = mir_method.borrow();

    if mir_method.ret_type != iface_method.ret_type {
        let tok = method
            .sig
            .return_type
            .as_ref()
            .map_or(&method.sig.name, ast::Type::get_token);
        return Err(Error::new(
            tok,
            "MIR",
            "Incorrect return type on interface method.".to_string(),
            &builder.path,
        ));
    }

    for (i, (method_param, iface_param)) in mir_method
        .parameters
        .iter()
        .skip(1)
        .zip(iface_method.parameters.iter())
        .enumerate()
    {
        if &method_param.type_ != iface_param {
            let tok = &method.sig.parameters[i].name;
            return Err(Error::new(
                tok,
                "MIR",
                format!(
                    "Incorrect parameter type on interface method (Expected {}, was {}).",
                    iface_param, method_param.type_
                ),
                &builder.path,
            ));
        }
    }

    Ok(())
}
