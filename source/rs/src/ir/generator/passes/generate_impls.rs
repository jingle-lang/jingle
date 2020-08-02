/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:50 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::rc::Rc;

use crate::{
    error::Res,
    ir::{
        generator::{
            builder::Context,
            passes::{declaring_iface_impls::get_or_create_iface_impls, ModulePass, PassType},
            MIRGenerator,
        },
        nodes::{IFaceImpls, Type},
        MutRc,
    },
};

/// This pass generates all functions inside iface impls.
/// The boolean indicates if the pass has already been run at least once.
pub struct GenerateImpls();

impl ModulePass for GenerateImpls {
    fn get_type(&self) -> PassType {
        PassType::AllTypes
    }

    fn run_type(&self, gen: &mut MIRGenerator, ty: Type) -> Res<()> {
        let impls = get_or_create_iface_impls(&ty);
        gen_impl_for_type(gen, &impls)
    }
}

pub fn gen_impl_for_type(gen: &mut MIRGenerator, impls: &MutRc<IFaceImpls>) -> Res<()> {
    let impls = impls.borrow();

    for im in impls.interfaces.values() {
        gen.builder.context = im.implementor.context().unwrap_or_else(Context::default);
        gen.builder.add_to_context(&im.iface.borrow().context);

        let ast = Rc::clone(&im.ast);
        gen.switch_module(&im.module);

        for (i, (_, method)) in im.methods.iter().enumerate() {
            gen.generate_function(&ast.methods[i], Some(method.type_.as_function()))?;
        }
    }

    Ok(())
}
