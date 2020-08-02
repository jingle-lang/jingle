/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 3:23 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{cell::RefCell, rc::Rc};

use crate::{
    ast::module::Module,
    error::Errors,
    ir::{
        generator::{
            builder::MIRBuilder,
            intrinsics::INTRINSICS,
            passes::{
                declaring_globals::DeclareGlobals,
                declaring_iface_impls::DeclareIfaceImpls,
                declaring_methods::DeclareMethods,
                declaring_types::DeclareTypes,
                fill_impls::FillIfaceImpls,
                filter_prototypes::FilterPrototypes,
                generate::Generate,
                generate_impls::GenerateImpls,
                imports::{ImportGlobals, ImportTypes},
                insert_members::InsertClassMembers,
                populate_intrinsics::{PopulateIntrinsics, PopulateIntrinsicsFunctions},
                validate::ValidateIntrinsics,
                ModulePass, PassType, PreMIRPass,
            },
            MIRGenerator,
        },
        mutrc_new,
        nodes::Type,
        MModule, MutRc, IFACE_IMPLS,
    },
};

thread_local! {
    /// A map containing passes that have run, and the currently running pass.
    /// This is global state since it is shared across modules.
    pub static DONE_PASSES: RefCell<Vec<Box<dyn ModulePass>>> = RefCell::new(Vec::new());
}

/// Responsible for collecting all passes that run on the MIR.
/// MIR is built purely by running many transformation passes,
/// it is considered compiled once the last pass
/// has been run.
pub struct PassRunner {
    /// All the modules in this compilation run.
    modules: Vec<MutRc<MModule>>,
}

impl PassRunner {
    pub fn execute(self, mut modules: Vec<Module>) -> Result<Vec<MutRc<MModule>>, Vec<Errors>> {
        reset_mir();
        let mut passes: Vec<Box<dyn PreMIRPass>> = vec![
            Box::new(FilterPrototypes()),
            Box::new(DeclareTypes()),
            Box::new(PopulateIntrinsics()),
            Box::new(ImportTypes()),
            Box::new(DeclareIfaceImpls()),
            Box::new(DeclareGlobals()),
            Box::new(PopulateIntrinsicsFunctions()),
            Box::new(ImportGlobals()),
        ];

        for mut pass in passes.drain(..) {
            let mut errs = Vec::new();
            for (ast, module) in modules.iter_mut().zip(self.modules.iter()) {
                pass.run(ast, Rc::clone(&module), &self.modules)
                    .map_err(|e| errs.push(e))
                    .ok();
            }
            if !errs.is_empty() {
                return Err(errs);
            }
        }

        let mut passes: Vec<Box<dyn ModulePass>> = vec![
            Box::new(DeclareMethods()),
            Box::new(FillIfaceImpls()),
            Box::new(InsertClassMembers()),
            Box::new(Generate()),
            Box::new(GenerateImpls()),
            Box::new(ValidateIntrinsics()),
            // Box::new(GCMarkEscapeVariables()),
        ];
        let mut generator = MIRGenerator::new(MIRBuilder::new(&self.modules[0]));
        for pass in passes.drain(..) {
            // The pass needs to be put into DONE_PASSES before running.
            DONE_PASSES.with(|d| d.borrow_mut().push(pass));
            DONE_PASSES.with(|d| self.run_pass(&**d.borrow().last().unwrap(), &mut generator))?;
        }

        Ok(self.modules)
    }

    pub fn run_pass(
        &self,
        pass: &dyn ModulePass,
        gen: &mut MIRGenerator,
    ) -> Result<(), Vec<Errors>> {
        let mut errors = Vec::new();

        let pass_type = DONE_PASSES.with(|d| d.borrow().last().unwrap().get_type());
        match pass_type {
            PassType::Globally => {
                pass.run_globally(&self.modules)?;
            }

            PassType::Type | PassType::AllTypes => {
                let primitive_iter = if pass_type == PassType::AllTypes {
                    Some((Type::primitives().to_vec(), Rc::clone(&gen.module)))
                } else {
                    None
                }
                .into_iter();

                let types = self
                    .modules
                    .iter()
                    .map(|module| {
                        (
                            module.borrow().types.values().cloned().collect::<Vec<_>>(),
                            Rc::clone(module),
                        )
                    })
                    .collect::<Vec<_>>();

                for (types, module) in primitive_iter.chain(types.into_iter()) {
                    let mut errs = Vec::new();

                    gen.switch_module(&module);
                    for ty in types {
                        ty.context().map(|c| gen.builder.context = c);
                        pass.run_type(gen, ty).map_err(|e| errs.push(e)).ok();
                    }

                    if !errs.is_empty() {
                        errors.push(Errors(errs, Rc::clone(&module.borrow().src)));
                    }
                }
            }
        }

        if errors.is_empty() {
            Ok(())
        } else {
            Err(errors)
        }
    }

    pub fn new(modules: &[Module]) -> Self {
        Self {
            modules: modules.iter().map(MModule::new).map(mutrc_new).collect(),
        }
    }
}

/// This function resets MIR global state.
/// Called before starting a new compile.
fn reset_mir() {
    INTRINSICS.with(|i| i.borrow_mut().reset());
    IFACE_IMPLS.with(|i| i.borrow_mut().clear());
    DONE_PASSES.with(|d| d.borrow_mut().clear());
}
