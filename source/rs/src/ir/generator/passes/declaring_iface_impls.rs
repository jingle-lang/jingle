/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:50 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{collections::HashMap, rc::Rc};

use indexmap::IndexMap;

use crate::{
    ast,
    ast::Module,
    error::{Error, Errors, Res},
    ir::{
        generator::{builder::MIRBuilder, passes::PreMIRPass},
        get_iface_impls, mutrc_new,
        nodes::{IFaceImpl, IFaceImpls, Type},
        result::ToMIRResult,
        MModule, MutRc, IFACE_IMPLS,
    },
};

/// This pass inserts all iface impls in the global impl
/// table. It only validates that the type implementing for
/// exists, no other checks are performed.
pub struct DeclareIfaceImpls();

impl PreMIRPass for DeclareIfaceImpls {
    fn run(
        &mut self,
        ast: &mut Module,
        module: MutRc<MModule>,
        _modules: &[MutRc<MModule>],
    ) -> Result<(), Errors> {
        let mut errs = Vec::new();
        let mut builder = MIRBuilder::new(&module);

        for im in ast.iface_impls.drain(..) {
            declare_impl(im, &mut builder, None)
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

pub fn declare_impl(
    iface_impl: ast::IFaceImpl,
    builder: &mut MIRBuilder,
    override_implementor: Option<Type>,
) -> Res<()> {
    let err_token = iface_impl.iface.get_token().clone();
    let implementor =
        override_implementor.map_or_else(|| builder.find_type(&iface_impl.implementor), Ok);
    if implementor.is_err() && iface_impl.implementor.is_generic() {
        return add_impl_to_proto(iface_impl, builder);
    }
    let implementor = implementor?;

    let ty = builder.find_type(&iface_impl.iface)?;
    if !ty.is_adt() || !ty.as_adt().borrow().ty.is_interface() {
        return Err(Error::new(
            &err_token,
            "MIR",
            "Not an interface".to_string(),
            &builder.path,
        ));
    };

    let impls = get_or_create_iface_impls(&implementor);
    let mir_impl = IFaceImpl {
        implementor,
        iface: Rc::clone(ty.as_adt()),
        methods: IndexMap::with_capacity(iface_impl.methods.len()),
        module: Rc::clone(&builder.module),
        ast: Rc::new(iface_impl),
    };
    let already_defined = impls.borrow_mut().interfaces.insert(ty, mir_impl).is_some();
    if already_defined {
        return Err(Error::new(
            &err_token,
            "MIR",
            "Interface already defined for type".to_string(),
            &builder.path,
        ));
    }

    Ok(())
}

/// Gets the interfaces implemented by a type.
pub fn get_or_create_iface_impls(ty: &Type) -> MutRc<IFaceImpls> {
    match get_iface_impls(ty) {
        Some(impls) => impls,
        None => IFACE_IMPLS.with(|impls| {
            let iface_impls = mutrc_new(IFaceImpls {
                implementor: ty.clone(),
                interfaces: HashMap::with_capacity(2),
                methods: HashMap::with_capacity(2),
            });
            impls
                .borrow_mut()
                .insert(ty.clone(), Rc::clone(&iface_impls));
            iface_impls
        }),
    }
}

fn add_impl_to_proto(iface_impl: ast::IFaceImpl, builder: &mut MIRBuilder) -> Res<()> {
    let implementor = iface_impl.implementor.get_token();
    let proto = builder
        .module
        .borrow()
        .find_prototype(&implementor.lexeme)
        .or_err(&builder.path, &implementor, "Unknown prototype.")?;
    proto
        .impls
        .borrow_mut()
        .push((iface_impl, Rc::clone(&builder.module)));
    Ok(())
}
