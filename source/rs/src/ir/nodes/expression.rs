/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 3:01 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{
    fmt::{Display, Error, Formatter},
    rc::Rc,
};

use crate::{
    ast::{expression::LOGICAL_BINARY, Literal},
    scanner::token::TType,
    ir::{
        generator::intrinsics::INTRINSICS,
        nodes::{ADTMember, Function, Type, Variable, ADT},
        MutRc,
    },
};
use either::Either::{Left, Right};
use std::cell::Cell;

/// All expressions in MIR. All of them produce a value.
/// Expressions are in blocks in functions. Gelix does not have statements.
///
/// When compiling MIR expressions into IR, they are not checked for
/// validity. Invalid/Illegal expressions will most likely result in a
/// crash or broken IR code.
#[derive(Debug, Clone, EnumIsA, EnumAsGetters)]
pub enum Expr {
    /// Create a class or enum instance.
    /// This will perform the following steps in IR:
    /// - Allocate either an alloca or on the heap with malloc
    /// - Call the instantiator with this new allocation
    /// - Call the given constructor with the allocation
    /// - Return the now initialized object as the value of this Expr
    AllocInst {
        ty: MutRc<ADT>,
        constructor: Rc<Variable>,
        constructor_args: Vec<Expr>,
        heap: Cell<bool>,
    },

    /// Simply a binary operation between numbers.
    Binary {
        left: Box<Expr>,
        operator: TType,
        right: Box<Expr>,
    },

    /// A break expression inside a loop.
    Break(Box<Expr>),

    /// A freestanding block.
    /// Cannot be simplified since IR GC needs to be aware of blocks.
    Block(Vec<Expr>),

    /// A static function call.
    /// callee can be both a function or a closure.
    Call {
        callee: Box<Expr>,
        arguments: Vec<Expr>,
    },

    /// A dynamic function call, where the callee is an interface method.
    /// The index is of the function to be called in the iface's method/vtable field.
    /// Implemented in IR as a struct with pointers to implementor and vtable (fat ptr).
    /// The value/fat ptr is obtained from the arguments list.
    CallDyn {
        callee: MutRc<ADT>,
        index: usize,
        arguments: Vec<Expr>,
    },

    /// A cast to some other type.
    /// Following casts are currently done:
    /// - Interface implementor to interface
    ///   -> Will create a temp alloca in IR to hold the interface struct.
    ///
    /// Following casts are simply a noop bitcast in IR:
    /// - Enum case to parent enum
    /// - Parent enum to case (unchecked; MIR code does so)
    Cast { object: Box<Expr>, to: Type },

    /// Construct a closure from the given function along with the captured
    /// variables. The function must have an additional first parameter
    /// for all captured variables; similarly to the 'this' param on methods.
    ConstructClosure {
        function: MutRc<Function>,
        global: Rc<Variable>,
        captured: Rc<Vec<Rc<Variable>>>,
    },

    /// Calls libc free() on the inner expression.
    /// Currently only used in destructors.
    Free(Box<Expr>),

    /// An if branching expression.
    /// For ASTExpr::If without else block,
    /// else is simply Expr::none_const()
    /// `phi` indicates that the expression will return
    /// the value of the branch executed.
    If {
        condition: Box<Expr>,
        then: Box<Expr>,
        else_: Box<Expr>,
        phi: bool,
    },

    /// Simply produces the literal as value.
    Literal(Literal),

    /// A loop. body is executed until the condition is no
    /// longer true; else is executed if it is never true.
    /// For ASTExpr::For without else block,
    /// else is simply Expr::none_const()
    /// `result_store` is the value of the expression
    /// if present, otherwise it's Expr::none_const().
    Loop {
        condition: Box<Expr>,
        body: Box<Expr>,
        else_: Box<Expr>,
        result_store: Option<Rc<Variable>>,
    },

    /// Modifies the refcount on a value, either
    /// incrementing or decrementing it.
    /// It returns the value - it essentially wraps it
    ModifyRefCount { object: Box<Expr>, dec: bool },

    /// Return from the function with the given value.
    /// Return without expression will use Literal::None.
    Return(Box<Expr>),

    /// Gets a member of a class struct.
    StructGet {
        object: Box<Expr>,
        index: usize,
        val_ty: Type,
    },

    /// Sets a member of a class struct.
    StructSet {
        object: Box<Expr>,
        index: usize,
        value: Box<Expr>,
        first_set: bool,
    },

    /// Similar to VarGet, but returns a Type::Type.
    TypeGet(Type),

    /// A unary expression on numbers.
    Unary { operator: TType, right: Box<Expr> },

    /// Returns a variable.
    VarGet(Rc<Variable>),

    /// Stores a value inside a variable.
    VarStore {
        var: Rc<Variable>,
        value: Box<Expr>,
        first_store: bool,
    },

    /// A when expression.
    /// Cases are (condition, body).
    Switch {
        cases: Vec<(Expr, Expr)>,
        else_: Option<Box<Expr>>,
        phi: Option<Type>,
    },
}

impl Expr {
    pub fn alloc_type(ty: Type, constructor: &Rc<Variable>, constructor_args: Vec<Expr>) -> Expr {
        // The type to alloc might still be boxed in Type::Type,
        // unbox it if so
        let ty = if let Type::Type(ty) = ty { *ty } else { ty };

        Expr::AllocInst {
            ty: ty.into_adt(),
            constructor: Rc::clone(&constructor),
            constructor_args,
            heap: Cell::new(true),
        }
    }

    pub fn binary(left: Expr, operator: TType, right: Expr) -> Expr {
        Expr::Binary {
            left: Box::new(left),
            operator,
            right: Box::new(right),
        }
    }

    pub fn break_(expr: Option<Expr>) -> Expr {
        Expr::Break(Box::new(expr.unwrap_or_else(Expr::none_const)))
    }

    pub fn cast(obj: Expr, ty: &Type) -> Expr {
        Expr::Cast {
            object: Box::new(obj),
            to: ty.clone(),
        }
    }

    pub fn maybe_cast(obj: Expr, obj_ty: &Type, ty: &Type) -> Expr {
        if obj_ty == ty {
            obj
        } else {
            Self::cast(obj, ty)
        }
    }

    pub fn construct_closure(global: &Rc<Variable>, captured: Rc<Vec<Rc<Variable>>>) -> Expr {
        Expr::ConstructClosure {
            function: Rc::clone(global.type_.as_function()),
            global: Rc::clone(global),
            captured,
        }
    }

    pub fn call(callee: Expr, arguments: Vec<Expr>) -> Expr {
        Expr::Call {
            callee: Box::new(callee),
            arguments,
        }
    }

    pub fn call_dyn(callee: &MutRc<ADT>, index: usize, arguments: Vec<Expr>) -> Expr {
        Expr::CallDyn {
            callee: Rc::clone(callee),
            index,
            arguments,
        }
    }

    pub fn if_(cond: Expr, then: Expr, else_: Expr, phi: bool) -> Expr {
        Expr::If {
            condition: Box::new(cond),
            then: Box::new(then),
            else_: Box::new(else_),
            phi,
        }
    }

    pub fn loop_(cond: Expr, body: Expr, else_: Option<Expr>, store: Option<Rc<Variable>>) -> Expr {
        Expr::Loop {
            condition: Box::new(cond),
            body: Box::new(body),
            else_: Box::new(else_.unwrap_or_else(Expr::none_const)),
            result_store: store,
        }
    }

    pub fn mod_rc(val: Expr, dec: bool) -> Expr {
        Expr::ModifyRefCount {
            object: Box::new(val),
            dec,
        }
    }

    pub fn ret(expr: Expr) -> Expr {
        Expr::Return(Box::new(expr))
    }

    pub fn struct_get(object: Expr, field: &Rc<ADTMember>) -> Expr {
        Expr::StructGet {
            object: Box::new(object),
            index: field.index,
            val_ty: field.type_.clone(),
        }
    }

    pub fn struct_set(object: Expr, index: usize, value: Expr, first_set: bool) -> Expr {
        Expr::StructSet {
            object: Box::new(object),
            index,
            value: Box::new(value),
            first_set,
        }
    }

    pub fn type_get(ty: Type) -> Expr {
        Expr::TypeGet(Type::Type(Box::new(ty)))
    }

    pub fn unary(right: Expr, op: TType) -> Expr {
        Expr::Unary {
            operator: op,
            right: Box::new(right),
        }
    }

    pub fn store(var: &Rc<Variable>, value: Expr, first_store: bool) -> Expr {
        Expr::VarStore {
            var: Rc::clone(var),
            value: Box::new(value),
            first_store,
        }
    }

    pub fn load(var: &Rc<Variable>) -> Expr {
        Expr::VarGet(Rc::clone(var))
    }

    pub fn switch(cases: Vec<(Expr, Expr)>, else_: Option<Expr>, phi: Type) -> Expr {
        Expr::Switch {
            cases,
            else_: else_.map(Box::new),
            phi: if phi == Type::None { None } else { Some(phi) },
        }
    }

    pub fn none_const() -> Expr {
        Expr::Literal(Literal::None)
    }

    /// Returns the type of this `MIRExpression`.
    /// Note that this function does not do type validation, and calling this function
    /// on malformed expressions is undefined behavior that can lead to panics.
    pub fn get_type(&self) -> Type {
        match self {
            Expr::AllocInst { ty, .. } => Type::Adt(ty.clone()),

            Expr::Binary {
                right, operator, ..
            }
            | Expr::Unary { operator, right } => {
                if LOGICAL_BINARY.contains(&operator) {
                    Type::Bool
                } else {
                    right.get_type()
                }
            }

            Expr::Break(_) | Expr::Return(_) | Expr::Free(_) => Type::Any,

            Expr::Block(exprs) => exprs.last().map_or(Type::None, Expr::get_type),

            Expr::Call { callee, .. } => match callee.get_type() {
                Type::Function(func) => func.borrow().ret_type.clone(),
                Type::Closure(closure) => closure.ret_type.clone(),
                _ => panic!("Invalid callee"),
            },

            Expr::CallDyn { callee, index, .. } => callee
                .borrow()
                .dyn_methods
                .get_index(*index)
                .unwrap()
                .1
                .ret_type
                .clone(),

            Expr::Cast { to, .. } => to.clone(),

            Expr::ConstructClosure { function, .. } => function.borrow().to_closure_type(),

            Expr::If {
                then, else_, phi, ..
            } => {
                if *phi {
                    let then_ty = then.get_type();
                    if then_ty != Type::Any {
                        then_ty
                    } else {
                        else_.get_type()
                    }
                } else {
                    Type::None
                }
            }

            Expr::Loop { result_store, .. } => {
                if let Some(store) = result_store {
                    store.type_.clone()
                } else {
                    Type::None
                }
            }

            Expr::Literal(literal) => match literal {
                Literal::Any => Type::Any,
                Literal::None => Type::None,
                Literal::Bool(_) => Type::Bool,
                Literal::I8(_) => Type::I8,
                Literal::I16(_) => Type::I16,
                Literal::I32(_) => Type::I32,
                Literal::I64(_) => Type::I64,
                Literal::U8(_) => Type::U8,
                Literal::U16(_) => Type::U16,
                Literal::U32(_) => Type::U32,
                Literal::U64(_) => Type::U64,
                Literal::F32(_) => Type::F32,
                Literal::F64(_) => Type::F64,
                Literal::Char(_) => unimplemented!(),
                Literal::String(_) => INTRINSICS.with(|i| i.borrow().string_type.clone().unwrap()),
                Literal::Array(Right(arr)) => INTRINSICS
                    .with(|i| i.borrow().get_array_type(arr.type_.clone(), None))
                    .ok()
                    .unwrap(),
                Literal::Closure(_) | Literal::Array(Left(_)) => panic!("invalid literal"),
            },

            Expr::ModifyRefCount { object, .. } => object.get_type(),

            Expr::TypeGet(ty) => ty.clone(),

            Expr::StructGet { val_ty, .. } => val_ty.clone(),

            Expr::StructSet { value, .. } => value.get_type(),

            Expr::VarGet(var) | Expr::VarStore { var, .. } => var.type_.clone(),

            Expr::Switch { phi, .. } => phi.clone().unwrap_or(Type::None),
        }
    }
}

impl Display for Expr {
    fn fmt(&self, f: &mut Formatter) -> Result<(), Error> {
        match self {
            Expr::AllocInst { ty, heap, .. } => {
                write!(f, "alloc {} (heap: {})", ty.borrow(), heap.get())
            }

            Expr::Binary {
                left,
                operator,
                right,
            } => write!(f, "({}) {:?} ({})", left, operator, right),

            Expr::Call { callee, arguments } => {
                write!(f, "call {}", callee)?;
                if !arguments.is_empty() {
                    write!(f, " with ")?;
                }
                for arg in arguments.iter() {
                    write!(f, "({}) ", arg)?;
                }
                Ok(())
            }

            Expr::CallDyn {
                callee,
                index,
                arguments,
            } => {
                let method_name =
                    Rc::clone(callee.borrow().dyn_methods.get_index(*index).unwrap().0);
                write!(f, "call method {}", method_name)?;
                write!(f, " with ")?;
                for arg in arguments.iter() {
                    write!(f, "({}) ", arg)?;
                }
                Ok(())
            }

            Expr::Cast { object, to, .. } => write!(f, "cast {} to {}", object, to),

            Expr::ConstructClosure {
                global, captured, ..
            } => {
                write!(f, "closure fn({}) capture", global.name)?;
                for capture in captured.iter() {
                    write!(f, " {}", capture.name)?;
                }
                Ok(())
            }

            Expr::Free(expr) => write!(f, "free({})", expr),

            Expr::ModifyRefCount { object, dec } => write!(f, "rc+{} on {}", !dec, object),

            Expr::StructGet { object, index, .. } => write!(f, "get {} from ({})", index, object),

            Expr::StructSet {
                object,
                index,
                value,
                ..
            } => write!(f, "set {} of ({}) to ({})", index, object, value),

            Expr::Literal(literal) => write!(f, "{}", literal),

            Expr::Unary { right, .. } => write!(f, "neg ({})", right),

            Expr::VarGet(var) => write!(f, "{}", var.name),

            Expr::VarStore { var, value, .. } => write!(f, "store ({}) in {}", value, var.name),

            Expr::Break(expr) => write!(f, "break {}", expr),

            Expr::Block(exprs) => {
                writeln!(f, "{{")?;
                for expr in exprs.iter() {
                    writeln!(f, "    {}", expr)?;
                }
                writeln!(f, "}}")
            }

            Expr::If {
                condition,
                then,
                else_,
                phi,
            } => write!(
                f,
                "if (phi {}) ({}) {} else {}",
                phi, condition, then, else_
            ),

            Expr::Loop {
                condition,
                body,
                else_,
                ..
            } => write!(f, "loop ({}) {} else {}", condition, body, else_),

            Expr::Return(expr) => write!(f, "return {}", expr),

            Expr::TypeGet(ty) => write!(f, "get_type {}", ty),

            // TODO: Not be lazy
            Expr::Switch { phi, .. } => write!(f, "when (ty: {})", phi.is_some()),
        }
    }
}

/// An array literal in MIR. See ast/literal.rs for usage.
#[derive(Debug, Clone)]
pub struct ArrayLiteral {
    pub values: Vec<Expr>,
    pub type_: Type,
}
