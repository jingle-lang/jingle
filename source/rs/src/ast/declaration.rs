/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 7:25 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::fmt;

use super::{super::scanner::token::Token, expression::Expression};
use std::rc::Rc;

/// Visibilities of a declaration.
/// Most declarations default to 'module'
#[derive(Debug, Clone, Copy, PartialEq)]
pub enum Visibility {
    /// Visible and importable from anywhere.
    Public,
    /// Local to the given file/submodule.
    Private,
    /// Local to the given base module, 'std' for example.
    Module,
}

/// An generic ADT declaration.
#[derive(Debug, Clone)]
pub struct ADT {
    pub name: Token,
    pub visibility: Visibility,
    pub generics: Option<Vec<GenericParam>>,
    pub methods: Vec<Function>,
    pub ty: ADTType,
}

impl ADT {
    pub fn members(&self) -> Option<&[ADTMember]> {
        match &self.ty {
            ADTType::Enum { variables, .. }
            | ADTType::Class { variables, .. }
            | ADTType::EnumCase { variables, .. } => Some(&variables),
            ADTType::Interface => None,
        }
    }

    pub fn constructors(&self) -> Option<&[Constructor]> {
        match &self.ty {
            ADTType::Class { constructors, .. } | ADTType::EnumCase { constructors, .. } => {
                Some(&constructors)
            }
            _ => None,
        }
    }

    /// Returns case name if this is an enum case, regular name otherwise.
    pub fn case_name(&self) -> Rc<String> {
        Rc::clone(match &self.ty {
            ADTType::EnumCase { case_name, .. } => case_name,
            _ => &self.name.lexeme,
        })
    }

    /// This is only called on prototypes and used to replace their name with
    /// the name of an instance. For `EnumCase`, it is assumed the name
    /// is for the parent, since only Enum prototypes exist
    pub fn replace_proto_name(&mut self, new: &Rc<String>) {
        match &mut self.ty {
            ADTType::Enum { cases, .. } => {
                self.name.lexeme = Rc::clone(new);
                for case in cases.iter_mut() {
                    case.replace_proto_name(new)
                }
            }

            ADTType::EnumCase { case_name, .. } => {
                self.name.lexeme = Rc::new(format!("{}:{}", new, case_name))
            }

            _ => self.name.lexeme = Rc::clone(new),
        }
    }
}

#[derive(Debug, Clone)]
pub enum ADTType {
    /// A class declaration.
    Class {
        variables: Vec<ADTMember>,
        constructors: Vec<Constructor>,
        // If this class is marked with "extern".
        // Will cause the class to NOT be memory-managed and
        // be compatible with C structs.
        external: bool,
    },

    /// An interface declaration.
    Interface,

    /// An enum declaration.
    Enum {
        variables: Vec<ADTMember>,
        cases: Vec<ADT>,
    },

    /// An enum case.
    EnumCase {
        // Includes all parent members
        variables: Vec<ADTMember>,
        constructors: Vec<Constructor>,
        // The name of the case without the parent before it
        case_name: Rc<String>,
        // If this case has no body, and is simply `case Name`
        no_body: bool,
    },
}

/// A constructor in a declaration.
/// The body can be empty if the constructor
/// only requires parameter setters and would
/// simply have a pointless empty body otherwise.
#[derive(Debug, Clone)]
pub struct Constructor {
    pub visibility: Visibility,
    pub parameters: Vec<ConstructorParam>,
    pub body: Option<Expression>,
}

pub type ConstructorParam = (Token, Option<Type>);

/// A member of a declaration.
#[derive(Debug, Clone)]
pub struct ADTMember {
    pub name: Token,
    pub visibility: Visibility,
    pub mutable: bool,
    pub ty: Option<Type>,
    pub initializer: Option<Expression>,
}

/// An interface implementation for a class.
#[derive(Debug, Clone)]
pub struct IFaceImpl {
    pub iface: Type,
    pub implementor: Type,
    pub methods: Vec<Function>,
}

/// A function signature.
#[derive(Debug, Clone)]
pub struct FuncSignature {
    pub name: Token,
    pub visibility: Visibility,
    pub generics: Option<Vec<GenericParam>>,
    pub return_type: Option<Type>,
    pub parameters: Vec<FunctionParam>,
    pub variadic: bool,
}

/// A function argument.
#[derive(Debug, Clone)]
pub struct FunctionParam {
    pub type_: Type,
    pub name: Token,
}

impl FunctionParam {
    /// Used to create the implicit 'this' parameter in class & iface methods.
    pub fn this_param(ty: &Token) -> FunctionParam {
        FunctionParam {
            name: Token::generic_identifier("this".to_string()),
            type_: Type::Ident(ty.clone()),
        }
    }

    /// See above.
    pub fn this_param_(ty: &Type) -> FunctionParam {
        FunctionParam {
            name: Token::generic_identifier("this".to_string()),
            type_: ty.clone(),
        }
    }
}

/// A function definition.
#[derive(Debug, Clone)]
pub struct Function {
    pub sig: FuncSignature,
    pub body: Option<Expression>,
}

/// A variable definition.
#[derive(Debug, Clone)]
pub struct Variable {
    pub name: Token,
    pub mutable: bool,
    pub initializer: Expression,
}

/// A type literal, like 'String' or '[i64]'
#[derive(Clone, Debug, PartialEq, EnumAsGetters, EnumIsA)]
pub enum Type {
    /// Just an identifier, primitive type, class, or interface
    Ident(Token),

    /// A pointer type, written *$type.
    /// For primitives, this is a pointer.
    /// For ADTs, this is a double pointer.
    Pointer(Box<Type>),

    /// A value type, written ^$type.
    /// For primitives, this will do nothing (already a value).
    /// For ADTs, this will compile to a direct struct value instead of a pointer.
    Value(Box<Type>),

    /// An array of a type, written [$type]
    Array(Box<Type>),

    /// A closure signature, written (param1: $ty1, param2: $ty2): $ret_type
    Closure {
        params: Vec<Type>,
        ret_type: Option<Box<Type>>,
        closing_paren: Token,
    },

    /// An identifier with additional generic parameters, a prototype
    /// instantiation: Prototype<TypeA, TypeB>
    Generic { token: Token, types: Vec<Type> },
}

impl Type {
    pub fn get_token(&self) -> &Token {
        match self {
            Type::Ident(token)
            | Type::Generic { token, .. }
            | Type::Closure {
                closing_paren: token,
                ..
            } => token,
            Type::Pointer(inner) | Type::Array(inner) | Type::Value(inner) => inner.get_token(),
        }
    }
}

impl fmt::Display for Type {
    fn fmt(&self, f: &mut fmt::Formatter) -> Result<(), fmt::Error> {
        match self {
            Type::Ident(tok) => write!(f, "{}", tok.lexeme),

            Type::Pointer(type_) => write!(f, "*{}", type_),

            Type::Value(type_) => write!(f, "^{}", type_),

            Type::Array(type_) => write!(f, "[{}]", type_),

            Type::Closure {
                params, ret_type, ..
            } => {
                write!(f, "(")?;
                let mut iter = params.iter();
                if let Some(param) = iter.next() {
                    write!(f, "{}", param)?;
                }
                for param in iter {
                    write!(f, ", {}", param)?;
                }
                write!(f, ")")?;
                if let Some(ret_type) = ret_type {
                    write!(f, "-> {}", ret_type)?;
                }
                Ok(())
            }

            Type::Generic { token, types } => {
                write!(f, "{}<", token.lexeme)?;
                let mut iter = types.iter();
                if let Some(type_) = iter.next() {
                    write!(f, "{}", type_)?;
                }
                for type_ in iter {
                    write!(f, ", {}", type_)?;
                }
                write!(f, ">")
            }
        }
    }
}

/// A generic parameter.
#[derive(Debug, Clone)]
pub struct GenericParam {
    /// The name of the parameter
    pub name: Token,
    /// Optional bounds of types substituting it
    pub bound: Option<Type>,
}
