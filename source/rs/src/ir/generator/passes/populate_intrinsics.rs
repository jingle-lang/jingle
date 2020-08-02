/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:50 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use crate::{
    ast::Module,
    error::Errors,
    ir::{
        generator::{intrinsics::INTRINSICS, passes::PreMIRPass},
        MModule, MutRc,
    },
};

/// This pass populates the intrinsics struct.
pub struct PopulateIntrinsics();

impl PreMIRPass for PopulateIntrinsics {
    fn run(
        &mut self,
        _ast: &mut Module,
        module: MutRc<MModule>,
        _modules: &[MutRc<MModule>],
    ) -> Result<(), Errors> {
        let module = module.borrow();
        if **module.path.0[0] == *"std" && **module.path.0[1] == *"ops" {
            // This is the std/ops module, containing all operator interfaces
            INTRINSICS.with(|i| i.borrow_mut().fill_ops_table(module))
        } else if **module.path.0[0] == *"std" && **module.path.0[1] == *"string" {
            // This is std/string, containing the string class
            INTRINSICS.with(|i| {
                i.borrow_mut().string_type = module.find_type(&"String".to_string());
            })
        } else if **module.path.0[0] == *"std" && **module.path.0[1] == *"collections" {
            // This is std/collections, containing the array class
            INTRINSICS.with(|i| {
                i.borrow_mut().array_proto = module.find_prototype(&"Array".to_string());
            })
        } else if **module.path.0[0] == *"std" && **module.path.0[1] == *"memory" {
            INTRINSICS.with(|i| {
                i.borrow_mut().free_iface = module.find_type(&"Free".to_string());
            })
        }
        Ok(())
    }
}

/// This pass populates the intrinsics struct functions.
pub struct PopulateIntrinsicsFunctions();

impl PreMIRPass for PopulateIntrinsicsFunctions {
    fn run(
        &mut self,
        _ast: &mut Module,
        module: MutRc<MModule>,
        _modules: &[MutRc<MModule>],
    ) -> Result<(), Errors> {
        let module = module.borrow();
        if **module.path.0[0] == *"std" && **module.path.0[1] == *"intrinsics" {
            INTRINSICS.with(|i| {
                i.borrow_mut().libc_free = module.find_global(&"free".to_string());
            })
        }
        Ok(())
    }
}
