/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 3:23 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

//! This module contains things related to intrinsics: things that
//! bridge the gap between the compiler and the language.
//! An example would be the translation of operator
//! overloading interfaces into actually changing the behavior
//! of the expression.

use std::{
    cell::{Ref, RefCell},
    collections::HashMap,
    rc::Rc,
};

use crate::{
    error::{Error, Res},
    scanner::token::{TType, Token},
    ir::{
        nodes::{Prototype, Type, Variable},
        MModule,
    },
};

thread_local! {
    pub static INTRINSICS: RefCell<Intrinsics> = RefCell::new(Intrinsics::default());
}

/// Contains all data structures that require some sort of special treatment.
#[derive(Default)]
pub struct Intrinsics {
    /// Contains prototypes of all operators.
    /// For binary operators, the key is the TType of the operator.
    /// For IndexGet, its LeftBracket.
    /// For IndexSet, its RightBracket.
    ops: HashMap<TType, Rc<Prototype>>,
    /// Prototype of the Array<T> class, used for array type aliases like [i8]
    pub array_proto: Option<Rc<Prototype>>,
    /// String type, used for string literals.
    pub string_type: Option<Type>,
    /// The Free interface, used while compiling a class destructor.
    pub free_iface: Option<Type>,
    /// libc free.
    pub libc_free: Option<Rc<Variable>>,
    /// The entry point of the program - more than one function
    /// named main is a compile error
    pub main_fn: Option<Rc<Variable>>,
}

impl Intrinsics {
    /// Returns the interface corresponding with this binary operator
    pub fn get_op_iface(&self, ty: TType) -> Option<Rc<Prototype>> {
        self.ops.get(&ty).cloned()
    }

    /// Returns the array type for a given array literal,
    /// building the type if needed.
    pub fn get_array_type(&self, ty: Type, tok: Option<Token>) -> Res<Type> {
        let proto = self.array_proto.as_ref().cloned().unwrap();
        let err_tok = tok.unwrap_or_else(|| Token::generic_token(TType::Identifier));
        proto.build(vec![ty], &proto.module, &err_tok, Rc::clone(&proto))
    }

    /// Only call this with the std/ops module, containing all operator interfaces;
    /// fills self.ops
    pub fn fill_ops_table(&mut self, module: Ref<MModule>) {
        for (name, iface) in &module.protos {
            let iface = Rc::clone(iface);
            match &name[..] {
                "Add" => self.ops.insert(TType::Plus, iface),
                "Sub" => self.ops.insert(TType::Minus, iface),
                "Mul" => self.ops.insert(TType::Star, iface),
                "Div" => self.ops.insert(TType::Slash, iface),
                "Rem" => self.ops.insert(TType::Modulo, iface),
                "Equal" => {
                    self.ops.insert(TType::EqualEqual, Rc::clone(&iface));
                    self.ops.insert(TType::BangEqual, iface)
                }
                "IndexGet" => self.ops.insert(TType::LeftBracket, iface),
                "IndexSet" => self.ops.insert(TType::RightBracket, iface),
                _ => None,
            };
        }
    }

    /// Sets the main fn. Returns success, None indicates that
    /// a main function already existed
    pub fn set_main_fn(&mut self, func: &Rc<Variable>) -> Option<()> {
        if self.main_fn.is_some() {
            None
        } else {
            self.main_fn = Some(Rc::clone(func));
            Some(())
        }
    }

    pub fn validate(&mut self) -> Res<()> {
        if self.main_fn.is_none() {
            return Err(Error {
                line: 0,
                start: 0,
                len: 0,
                producer: "MIR",
                message: "Could not find main function.".to_string(),
                module: Rc::new(Default::default()),
            });
        }
        Ok(())
    }

    pub fn reset(&mut self) {
        self.ops.clear();
        self.array_proto = None;
        self.main_fn = None;
    }
}
