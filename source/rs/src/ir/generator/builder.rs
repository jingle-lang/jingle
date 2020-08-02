/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 2:44 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::rc::Rc;

use crate::{
    ast::{module::ModulePath, Type as ASTType},
    error::Res,
    scanner::token::Token,
    ir::{
        generator::intrinsics::INTRINSICS,
        nodes::{ClosureType, Type},
        result::ToMIRResult,
        MModule, MutRc,
    },
};
use indexmap::map::IndexMap;

/// The MIR builder is used alongside the module after
/// all types have been declared. It can be used for
/// resolving types and similar tasks.
///
/// It is also used by the `MIRGenerator`.
#[derive(Clone)]
pub struct MIRBuilder {
    /// The path of the current module.
    /// Separate to reduce amount of borrows on the module.
    pub path: Rc<ModulePath>,

    /// The module this builder is linked to.
    pub module: MutRc<MModule>,

    /// See docs on [Context].
    pub context: Context,
}

impl MIRBuilder {
    /// Returns the MIR type of the AST type passed.
    /// Will search for the type in the scope of the module
    /// and return an error if no such type exists.
    /// Note that this function can call `borrow_mut()` on the module.
    pub fn find_type(&self, ast: &ASTType) -> Res<Type> {
        match ast {
            ASTType::Ident(tok) => {
                let ty = self.find_type_by_name(&tok);
                let ty = ty.or_else(|| Some(self.context.type_aliases.get(&tok.lexeme)?.clone()));
                ty.or_type_err(&self.path, ast, "Unknown type.")
            }

            ASTType::Pointer(inner) => {
                let inner = self.find_type(inner)?;
                Ok(Type::Pointer(Box::new(inner)).maybe_simplify())
            }

            ASTType::Value(inner) => {
                let inner = self.find_type(inner)?;

                // Primitives are already values so it would
                // be unnecessary to wrap them
                Ok(if !inner.is_primitive() {
                    Type::Value(Box::new(inner)).maybe_simplify()
                } else {
                    inner
                })
            }

            ASTType::Array(inner) => {
                let tok = inner.get_token().clone();
                INTRINSICS.with(|i| i.borrow().get_array_type(self.find_type(inner)?, Some(tok)))
            }

            ASTType::Closure {
                params, ret_type, ..
            } => {
                let parameters = params
                    .iter()
                    .map(|p| self.find_type(p))
                    .collect::<Res<Vec<_>>>()?;
                let ret_type = ret_type
                    .as_ref()
                    .map_or(Ok(Type::None), |t| self.find_type(t))?;
                Ok(Type::Closure(Rc::new(ClosureType {
                    parameters,
                    ret_type,
                })))
            }

            ASTType::Generic { token, types } => {
                let proto = self
                    .module
                    .borrow()
                    .find_prototype(&token.lexeme)
                    .or_type_err(&self.path, ast, "Unknown prototype.")?;

                let args = types
                    .iter()
                    .map(|ty| self.find_type(&ty))
                    .collect::<Res<Vec<Type>>>()?;

                proto.build(args, &self.module, token, Rc::clone(&proto))
            }
        }
    }

    fn find_type_by_name(&self, tok: &Token) -> Option<Type> {
        Some(match &tok.lexeme[..] {
            "Nil" => Type::None,
            "Bool" => Type::Bool,
            "Integer" => Type::I64,
            "Float" => Type::F64,

            "i8" => Type::I8,
            "i16" => Type::I16,
            "i32" => Type::I32,
            "i64" => Type::I64,
            #[cfg(target_pointer_width = "64")]
            "isize" => Type::I64,
            #[cfg(not(target_pointer_width = "64"))]
            "isize" => Type::I32,

            "u8" => Type::U8,
            "u16" => Type::U16,
            "u32" => Type::U32,
            "u64" => Type::U64,
            #[cfg(target_pointer_width = "64")]
            "usize" => Type::U64,
            #[cfg(not(target_pointer_width = "64"))]
            "usize" => Type::U32,

            "f32" => Type::F32,
            "f64" => Type::F64,

            _ => self.module.borrow().find_type(&tok.lexeme)?,
        })
    }

    /// Switch the module this builder is operating on.
    pub fn switch_module(&mut self, module: &MutRc<MModule>) {
        self.path = Rc::clone(&module.borrow().path);
        self.module = Rc::clone(module);
    }

    pub fn add_to_context(&mut self, context: &Context) {
        match () {
            _ if self.context.type_aliases.is_empty() => self.context = context.clone(),
            _ if context.type_aliases.is_empty() => (),
            _ => {
                self.context = Context {
                    type_aliases: Rc::new(
                        context
                            .type_aliases
                            .iter()
                            .chain(self.context.type_aliases.iter())
                            .map(|(a, b)| (a.clone(), b.clone()))
                            .collect(),
                    ),
                };
            }
        }
    }

    pub fn new(module: &MutRc<MModule>) -> MIRBuilder {
        MIRBuilder {
            path: Rc::clone(&module.borrow().path),
            module: Rc::clone(module),
            context: Context::default(),
        }
    }

    pub fn with_context(module: &MutRc<MModule>, context: Context) -> MIRBuilder {
        MIRBuilder {
            path: Rc::clone(&module.borrow().path),
            module: Rc::clone(module),
            context,
        }
    }
}

/// A context contains additional data that changes the
/// behavior of the builder. Mostly either module-level
/// or type-level.
///
/// Note that a context is cheap to clone.
#[derive(Debug, Clone, Default)]
#[repr(transparent)]
pub struct Context {
    /// A map of type aliases, where the key
    /// will be translated to the value when encountered
    /// as a type. Used for instantiating generic stuff
    /// where the key is the parameter name (like T)
    /// and the value the type to use in its place.
    pub type_aliases: Rc<IndexMap<Rc<String>, Type>>,
}
