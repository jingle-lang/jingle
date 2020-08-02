/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:50 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::rc::Rc;

use crate::{
    error::Errors,
    ir::{
        generator::{
            intrinsics::INTRINSICS,
            passes::{ModulePass, PassType},
        },
        MModule, MutRc,
    },
};

/// This pass validates the intrinsics.
pub struct ValidateIntrinsics();

impl ModulePass for ValidateIntrinsics {
    fn get_type(&self) -> PassType {
        PassType::Globally
    }

    fn run_globally(&self, _modules: &[MutRc<MModule>]) -> Result<(), Vec<Errors>> {
        INTRINSICS
            .with(|i| i.borrow_mut().validate())
            .map_err(|e| vec![Errors(vec![e], Rc::new("".to_string()))])
    }
}
