/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 2/3/20 9:12 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

//! This module contains all functions directly responsible for parsing the tokens
//! and creating the AST from them.

use std::rc::Rc;

use either::Either;

use crate::{
    ast::{
        declaration::{
            ADTMember, Constructor, ConstructorParam, FuncSignature, Function, FunctionParam,
            IFaceImpl, Type, Variable, Visibility,
        },
        expression::Expression,
        literal::Literal,
        module::{Import, Module, ModulePath},
    },
    scanner::token::{TType, Token},
    parser::Parser,
    Error,
};

use crate::ast::{
    declaration::{ADTType, GenericParam, ADT},
    literal::{Closure, ClosureParameter},
};

// All expressions that require no semicolon when used as a higher expression.
static NO_SEMICOLON: [TType; 3] = [TType::If, TType::Colon, TType::Switch];

// All tokens that indicate that a function has a body (bodies are optional in enum and interface definitions).
static START_OF_FN_BODY: [TType; 2] = [TType::Colon, TType::Equal];

// All tokens that can be modifiers at all.
pub static MODIFIERS: [TType; 4] = [
    TType::Public,
    TType::Private,
    TType::Extern,
    TType::Variadic,
];

// All tokens that can be modifiers on any declaration.
static GLOBAL_MODIFIERS: [TType; 2] = [TType::Public, TType::Private];

// All tokens that can be modifiers on a class.
static CLASS_MODIFIERS: [TType; 1] = [TType::Extern];
// All tokens that can be modifiers on a class member.
static MEMBER_MODIFIERS: [TType; 0] = [];
// All tokens that can be modifiers on a method.
static METHOD_MODIFIERS: [TType; 0] = [];

// All tokens that can be modifiers on an enum.
static ENUM_MODIFIERS: [TType; 0] = [];

// All tokens that can be modifiers on a function.
static FUNC_MODIFIERS: [TType; 2] = [TType::Extern, TType::Variadic];
// All tokens that can be modifiers on an interface.
static IFACE_MODIFIERS: [TType; 0] = [];
// All tokens that can be modifiers on an import declaration.
static IMPORT_MODIFIERS: [TType; 0] = [];

#[macro_use]
mod bin_macro {
    /// This macro is used to generate binary operator parsing functions.
    /// The parser is a recursive descent parser.
    /// name is the name of the binary operation, next is the descending function name.
    /// matching is an array literal of the tokens that should match.
    #[macro_export]
    macro_rules! binary_op {
        ($name:ident, $next:ident, $matching:expr) => {
            fn $name(&mut self) -> Option<Expression> {
                let mut left = self.$next()?;
                while let Some(operator) = self.match_tokens(&$matching) {
                    let right = self.$next()?;
                    left = Expression::Binary {
                        left: Box::new(left), operator, right: Box::new(right)
                    }
                }
                Some(left)
            }
        };
    }
}

impl Parser {
    /// Parses the tokens and returns a full module.
    /// Returns a list of errors on failure.
    pub fn parse(mut self, module: &mut Module) -> Result<(), Vec<Error>> {
        while !self.is_at_end() {
            // Only true on error
            if self.declaration(module).is_none() {
                self.synchronize();
            }
        }

        if self.errors.is_empty() {
            Ok(())
        } else {
            Err(self.errors)
        }
    }

    /// The entry point for generating a declaration.
    /// The reason for returning Option is that the parser will error out and abort the current
    /// declaration when illegal syntax is encountered.
    /// Note that synchronization is not done on error, and is done by the caller.
    pub fn declaration(&mut self, module: &mut Module) -> Option<()> {
        self.consume_mods();
        match self.advance().t_type {
            TType::Class => module.adts.push(self.class_declaration()?),
            TType::Enum => module.adts.push(self.enum_declaration()?),
            TType::Export => module.exports.push(self.import_declaration("export")?),
            TType::Func => module.functions.push(self.function()?),
            TType::Import => module.imports.push(self.import_declaration("import")?),
            TType::Interface => module.adts.push(self.iface_declaration()?),
            TType::Impl => module.iface_impls.push(self.iface_impl()?),
            _ => self.error_at_current("Encountered invalid top-level declaration.")?,
        }

        Some(())
    }

    fn func_signature(&mut self) -> Option<FuncSignature> {
        self.check_mods(&FUNC_MODIFIERS, "function");
        let (name, generics) = self.generic_ident()?;
        self.consume(TType::LeftParen, "Expected '(' after function name.");

        let parameters = self.func_parameters()?;
        let return_type = if self.matches(TType::Arrow) {
            Some(self.type_("Expected return type after '->'.")?)
        } else {
            None
        };

        Some(FuncSignature {
            name,
            visibility: self.get_visibility()?,
            return_type,
            parameters,
            generics,
            variadic: self.modifiers.iter().any(|m| m.t_type == TType::Variadic),
        })
    }

    fn func_parameters(&mut self) -> Option<Vec<FunctionParam>> {
        let mut parameters: Vec<FunctionParam> = Vec::new();
        if !self.check(TType::RightParen) {
            loop {
                let name = self.consume(TType::Identifier, "Expected parameter name.")?;
                self.consume(TType::Colon, "Expected ':' after parameter name.")?;
                let type_ = self.type_("Expected parameter type.")?;
                parameters.push(FunctionParam { type_, name });
                if !self.matches(TType::Comma) {
                    break;
                }
            }
        }
        self.consume(TType::RightParen, "Expected ')' after parameters.")?;
        Some(parameters)
    }

    fn enum_declaration(&mut self) -> Option<ADT> {
        self.check_mods(&ENUM_MODIFIERS, "enum")?;
        let visibility = self.get_visibility()?;
        let (name, generics) = self.generic_ident()?;

        self.consume(TType::Colon, "Expected '{' before enum body.")?;

        let mut methods: Vec<Function> = Vec::new();
        let mut variables: Vec<ADTMember> = Vec::new();
        let mut cases: Vec<ADT> = Vec::new();

        while !self.check(TType::End) && !self.is_at_end() {
            self.consume_mods();
            match self.advance().t_type {
                TType::Var => variables.push(self.class_variable(true)?),
                TType::Val => variables.push(self.class_variable(false)?),
                TType::Case => cases.push(self.enum_case(&name)?),
                TType::Func => methods.push(self.function()?),

                _ => self.error_at_current("Encountered invalid declaration inside enum.")?,
            }
        }

        // TODO: no
        for (i, var) in variables.iter().enumerate() {
            for case in &mut cases {
                if let ADTType::EnumCase {
                    ref mut variables, ..
                } = &mut case.ty
                {
                    variables.insert(i, var.clone())
                }
            }
        }

        self.consume(TType::End, "Expected '}' after enum body.")?;
        Some(ADT {
            name,
            visibility,
            generics,
            methods,
            ty: ADTType::Enum { variables, cases },
        })
    }

    fn enum_case(&mut self, parent_name: &Token) -> Option<ADT> {
        let mut name = self.consume(TType::Identifier, "Expected case name.")?;
        let new_name = Rc::new(format!("{}:{}", parent_name.lexeme, name.lexeme));
        let case_name = std::mem::replace(&mut name.lexeme, new_name);

        let mut methods: Vec<Function> = Vec::new();
        let mut variables: Vec<ADTMember> = Vec::new();
        let mut constructors: Vec<Constructor> = Vec::new();

        let no_body = if self.matches(TType::Colon) {
            while !self.check(TType::End) && !self.is_at_end() {
                self.consume_mods();
                match self.advance().t_type {
                    TType::Var => variables.push(self.class_variable(true)?),
                    TType::Val => variables.push(self.class_variable(false)?),
                    TType::Construct => constructors.push(self.constructor()?),
                    TType::Func => methods.push(self.function()?),

                    _ => {
                        self.error_at_current("Encountered invalid declaration inside enum case.")?
                    }
                }
            }
            self.consume(TType::End, "Expected '}' after case body.")?;
            false
        } else if self.matches(TType::LeftParen) {
            while !self.check(TType::RightParen) && !self.is_at_end() {
                self.consume_mods();

                let tok = self.match_tokens(&[TType::Val, TType::Var]);
                let mutable = if let Some(tok) = tok {
                    tok.t_type == TType::Var
                } else {
                    self.error_at_current("Expected 'var' or 'val'.")?;
                    unreachable!();
                };

                let name = self.consume(TType::Identifier, "Expected member name.")?;
                self.consume(TType::Colon, "Expected ':' after member name.")?;
                let ty = self.type_("Expected member type.")?;
                variables.push(ADTMember {
                    name,
                    visibility: self.get_visibility()?,
                    mutable,
                    ty: Some(ty),
                    initializer: None,
                });

                if !self.matches(TType::Comma) {
                    break;
                }
            }
            self.consume(TType::RightParen, "Expected ')' after members.")?;

            constructors.push(Constructor {
                visibility: Visibility::Public,
                parameters: variables.iter().map(|m| (m.name.clone(), None)).collect(),
                body: None,
            });

            false
        } else {
            true
        };

        Some(ADT {
            name,
            visibility: Visibility::Public,
            generics: None,
            methods,
            ty: ADTType::EnumCase {
                variables,
                constructors,
                case_name,
                no_body,
            },
        })
    }

    fn class_declaration(&mut self) -> Option<ADT> {
        self.check_mods(&CLASS_MODIFIERS, "class")?;
        let visibility = self.get_visibility()?;
        let (name, generics) = self.generic_ident()?;
        let external = self.modifiers.iter().any(|t| t.t_type == TType::Extern);

        self.consume(TType::Colon, "Expected '{' before class body.")?;

        let mut methods: Vec<Function> = Vec::new();
        let mut variables: Vec<ADTMember> = Vec::new();
        let mut constructors: Vec<Constructor> = Vec::new();

        while !self.check(TType::End) && !self.is_at_end() {
            self.consume_mods();
            match self.advance().t_type {
                TType::Var => variables.push(self.class_variable(true)?),
                TType::Val => variables.push(self.class_variable(false)?),
                TType::Construct => constructors.push(self.constructor()?),
                TType::Func => methods.push(self.function()?),

                _ => self.error_at_current("Encountered invalid declaration inside class.")?,
            }
        }

        self.consume(TType::End, "Expected '}' after class body.")?;
        Some(ADT {
            name,
            visibility,
            generics,
            methods,
            ty: ADTType::Class {
                variables,
                constructors,
                external,
            },
        })
    }

    fn class_variable(&mut self, mutable: bool) -> Option<ADTMember> {
        self.check_mods(&MEMBER_MODIFIERS, "class member")?;
        let name = self.consume(TType::Identifier, "Expected variable name.")?;

        let mut ty = None;
        let mut initializer = None;
        match self.advance().t_type {
            TType::Equal => {
                initializer = Some(self.expression()?);
            }

            TType::Colon => {
                ty = Some(self.type_("Expected class member type.")?);
                if self.matches(TType::Equal) {
                    initializer = Some(self.expression()?);
                }
            }

            _ => {
                self.error_at_current("Expected ':' or '=' after class member name.")?;
            }
        }
        self.consume_semi_or_nl("Expected newline or ';' after variable declaration.")?;

        Some(ADTMember {
            name,
            visibility: self.get_visibility()?,
            mutable,
            ty,
            initializer,
        })
    }

    fn constructor(&mut self) -> Option<Constructor> {
        self.check_mods(&METHOD_MODIFIERS, "constructor")?;
        let visibility = self.get_visibility()?;

        self.consume(TType::LeftParen, "Expected '(' after 'construct'.")?;
        let mut parameters: Vec<ConstructorParam> = Vec::new();
        if !self.check(TType::RightParen) {
            loop {
                let name = self.consume(TType::Identifier, "Expected parameter name.")?;
                let ty = if self.matches(TType::Colon) {
                    Some(self.type_("Expected parameter type.")?)
                } else {
                    None
                };
                parameters.push((name, ty));
                if !self.matches(TType::Comma) {
                    break;
                }
            }
        }
        self.consume(TType::RightParen, "Expected ')' after parameters.")?;

        Some(Constructor {
            visibility,
            parameters,
            body: self.maybe_fn_body()?,
        })
    }

    fn maybe_fn_body(&mut self) -> Option<Option<Expression>> {
        Some(if START_OF_FN_BODY.contains(&self.current.t_type) {
            if !self.check(TType::Colon) {
                self.consume(TType::Equal, "Expected start of block or '='.")?;
            }
            Some(self.expression()?)
        } else {
            None
        })
    }

    fn import_declaration(&mut self, name: &'static str) -> Option<Import> {
        self.check_mods(&IMPORT_MODIFIERS, name)?;
        let mut path = Vec::new();
        if !self.check(TType::Identifier) {
            self.error_at_current(&format!("Expected path after '{}'.", name))?
        }

        let mut symbol = self.advance();
        let mut consumed_slash = self.matches(TType::ColonColon);
        while self.check(TType::Identifier) || self.check(TType::Star) {
            path.push(std::mem::replace(&mut symbol, self.advance()).lexeme);
            consumed_slash = self.matches(TType::ColonColon);
        }
        if consumed_slash {
            self.error_at_current(&format!("Trailing '::' in {}.", name))?
        }

        let path = Rc::new(ModulePath(path));
        Some(Import { path, symbol })
    }

    fn iface_declaration(&mut self) -> Option<ADT> {
        self.check_mods(&IFACE_MODIFIERS, "interface")?;
        let visibility = self.get_visibility()?;
        let (name, generics) = self.generic_ident()?;

        self.consume(TType::Colon, "Expected '{' before interface body.")?;

        let mut methods = Vec::new();
        while !self.check(TType::End) && !self.is_at_end() {
            match self.advance().t_type {
                TType::Func => {
                    let sig = self.func_signature()?;
                    let body = self.maybe_fn_body()?;
                    methods.push(Function { sig, body })
                }
                _ => self.error_at_current("Encountered invalid declaration inside interface.")?,
            }
        }

        self.consume(TType::End, "Expected '}' after interface body.")?;
        Some(ADT {
            name,
            visibility,
            generics,
            methods,
            ty: ADTType::Interface,
        })
    }

    fn iface_impl(&mut self) -> Option<IFaceImpl> {
        let iface = self.type_("Expected interface.")?;
        self.consume(TType::For, "Expected 'for' after interface name.")?;
        let implementor = self.type_("Expected interface implementor type.")?;
        self.consume(TType::Colon, "Expected '{' before impl body.")?;

        let mut methods: Vec<Function> = Vec::new();
        while !self.check(TType::End) && !self.is_at_end() {
            match self.advance().t_type {
                TType::Func => methods.push(self.function()?),
                _ => self.error_at_current("Encountered invalid declaration inside impl.")?,
            }
        }
        self.consume(TType::End, "Expected '}' after impl body.")?;

        Some(IFaceImpl {
            iface,
            implementor,
            methods,
        })
    }

    fn function(&mut self) -> Option<Function> {
        let sig = self.func_signature()?;

        let body = if self.modifiers.iter().any(|t| t.t_type == TType::Extern) {
            None
        } else {
            if !self.check(TType::Colon) {
                self.consume(TType::Equal, "Expected start of block or '='.");
            }

            Some(self.expression()?)
        };

        Some(Function { sig, body })
    }

    fn variable(&mut self, mutable: bool) -> Option<Variable> {
        let name = self.consume(TType::Identifier, "Expected variable name.")?;
        self.consume(TType::Equal, "Expected '=' after variable name.")?;
        let initializer = self.expression()?;
        self.consume_semi_or_nl("Expected newline or ';' after variable declaration.")?;

        Some(Variable {
            name,
            mutable,
            initializer,
        })
    }

    /// A 'higher' expression is an expression that is only allowed to appear
    /// as top-level inside a block.
    /// This function can also produce a top-level non-higher expression.
    fn higher_expression(&mut self) -> Option<Expression> {
        Some(match () {
            _ if self.matches(TType::Var) => Expression::VarDef(Box::new(self.variable(true)?)),
            _ if self.matches(TType::Val) => Expression::VarDef(Box::new(self.variable(false)?)),
            _ => {
                let requires_semicolon = !NO_SEMICOLON.contains(&self.current.t_type);
                let expression = self.expression()?;
                if requires_semicolon {
                    self.consume_semi_or_nl("Expected newline or ';' after expression.")?;
                }
                expression
            }
        })
    }

    fn expression(&mut self) -> Option<Expression> {
        match () {
            _ if self.matches(TType::Colon) => self.block(),
            _ if self.matches(TType::If) => self.if_expression(),
            _ if self.check(TType::Return) => self.return_expression(),
            _ if self.check(TType::Break) => self.break_expression(),
            _ if self.matches(TType::Loop) => self.for_expression(),
            _ if self.matches(TType::Switch) => self.switch_expression(),
            _ => self.assignment(),
        }
    }

    fn block(&mut self) -> Option<Expression> {
        let mut expressions: Vec<Expression> = Vec::new();
        while !self.check(TType::End) && !self.is_at_end() {
            expressions.push(self.higher_expression()?);
        }

        let tok = self.consume(TType::End, "Expected '}' after block.")?;
        Some(Expression::Block(expressions, tok))
    }

    fn if_expression(&mut self) -> Option<Expression> {
        self.consume(TType::LeftParen, "Expected '(' after 'if'.")?;
        let condition = Box::new(self.expression()?);
        self.consume(TType::RightParen, "Expected ')' after if condition.")?;
        let then_branch = Box::new(self.expression()?);

        let else_branch = if self.matches(TType::Else) {
            Some(Box::new(self.expression()?))
        } else {
            None
        };

        Some(Expression::If {
            condition,
            then_branch,
            else_branch,
        })
    }

    fn for_expression(&mut self) -> Option<Expression> {
        self.consume(TType::LeftParen, "Expected '(' after 'loop'.")?;

        if self.check_next(TType::From) {
            // for (var from x to y)
            let variable_name = self.consume(TType::Identifier, "Expected identifier after '('")?;
            self.consume(TType::From, "Expected 'from' after identifier.")?;

            let initial_value = self.expression()?;
            self.consume(TType::To, "Expected 'to' after starting value.")?;

            let last_value = self.expression()?;
            self.consume(TType::RightParen, "Expected ')' after loop condition.")?;

            let last_value = Expression::Binary {
                left: Box::new(last_value),
                operator: Token::generic_token(TType::Minus),
                right: Box::new(Expression::Literal(
                    Literal::I64(1),
                    Token::generic_token(TType::Int),
                )),
            };

            let variable = Expression::VarDef(Box::new(Variable {
                name: variable_name.clone(),
                mutable: true,
                initializer: Expression::Binary {
                    left: Box::new(initial_value),
                    operator: Token::generic_token(TType::Minus),
                    right: Box::new(Expression::Literal(
                        Literal::I64(1),
                        Token::generic_token(TType::Int),
                    )),
                },
            }));

            let var_increment = Expression::Assignment {
                name: variable_name.clone(),
                value: Box::new(Expression::Binary {
                    left: Box::new(Expression::Variable(variable_name.clone())),
                    operator: Token::generic_token(TType::Plus),
                    right: Box::new(Expression::Literal(
                        Literal::I64(1),
                        Token::generic_token(TType::Int),
                    )),
                }),
            };

            let body = self.expression()?;
            let else_b = if self.matches(TType::Else) {
                Some(Box::new(self.expression()?))
            } else {
                None
            };

            let for_loop = Expression::For {
                condition: Box::new(Expression::Binary {
                    left: Box::new(Expression::Variable(variable_name)),
                    operator: Token::generic_token(TType::BangEqual),
                    right: Box::new(last_value),
                }),
                body: Box::new(Expression::Block(
                    vec![var_increment, body],
                    Token::generic_token(TType::End),
                )),
                else_b,
            };

            Some(Expression::Block(
                vec![variable, for_loop],
                Token::generic_token(TType::End),
            ))
        } else {
            // for (condition)
            let condition = Box::new(self.expression()?);
            self.consume(TType::RightParen, "Expected ')' after loop condition.")?;
            let body = Box::new(self.expression()?);

            let else_b = if self.matches(TType::Else) {
                Some(Box::new(self.expression()?))
            } else {
                None
            };

            Some(Expression::For {
                condition,
                body,
                else_b,
            })
        }
    }

    fn return_expression(&mut self) -> Option<Expression> {
        let tok = self.advance();
        let value = if !self.check_semi_or_nl() {
            Some(Box::new(self.expression()?))
        } else {
            None
        };

        Some(Expression::Return(value, tok))
    }

    fn break_expression(&mut self) -> Option<Expression> {
        let tok = self.advance();
        let value = if !self.check_semi_or_nl() {
            Some(Box::new(self.expression()?))
        } else {
            None
        };

        Some(Expression::Break(value, tok))
    }

    fn switch_expression(&mut self) -> Option<Expression> {
        self.consume(TType::LeftParen, "Expected '(' after 'match'.")?;
        let value = Box::new(self.expression()?);
        self.consume(TType::RightParen, "Expected ')' after match value.")?;
        self.consume(TType::Colon, "Expected '{' after match value.")?;

        let mut branches: Vec<(Expression, Expression)> = Vec::new();
        let mut else_branch = None;
        while !self.matches(TType::End) {
            if self.matches(TType::Else) {
                if else_branch.is_some() {
                    self.error_at_current("'match' expression can only have 1 'else' branch.");
                }
                self.consume(TType::Arrow, "Expected '->' after match condition.")?;
                else_branch = Some(self.expression()?);
            } else {
                let condition = self.expression()?;
                self.consume(TType::Arrow, "Expected '->' after match condition.")?;
                let expression = self.expression()?;
                branches.push((condition, expression));
            }
        }

        Some(Expression::Switch {
            value,
            branches,
            else_branch: else_branch.map(Box::new),
        })
    }

    fn assignment(&mut self) -> Option<Expression> {
        let expression = self.logic_or()?;

        if self.matches(TType::Equal) {
            let value = Box::new(self.expression()?);
            match expression {
                Expression::Variable(name) => Some(Expression::Assignment { name, value }),
                Expression::Get { object, name } => Some(Expression::Set {
                    object,
                    name,
                    value,
                }),
                Expression::IndexGet { indexed, index, .. } => Some(Expression::IndexSet {
                    indexed,
                    index,
                    value,
                }),
                _ => {
                    self.error_at_current("Invalid assignment target.");
                    None
                }
            }
        } else {
            Some(expression)
        }
    }

    /// See the macro at the top of the file for info on how this works.
    binary_op!(logic_or, logic_and, [TType::Or]);
    binary_op!(logic_and, equality, [TType::And]);
    binary_op!(equality, comparison, [TType::BangEqual, TType::EqualEqual]);
    binary_op!(
        comparison,
        addition,
        [
            TType::Less,
            TType::LessEqual,
            TType::Greater,
            TType::GreaterEqual
        ]
    );
    binary_op!(addition, multiplication, [TType::Plus, TType::Minus]);
    binary_op!(multiplication, identity, [TType::Star, TType::Slash]);
    binary_op!(identity, unary, [TType::Is]);

    fn unary(&mut self) -> Option<Expression> {
        Some(
            if let Some(operator) = self.match_tokens(&[TType::Bang, TType::Minus]) {
                let right = Box::new(self.unary()?);
                Expression::Unary { operator, right }
            } else {
                self.call()?
            },
        )
    }

    fn call(&mut self) -> Option<Expression> {
        let mut expression = self.primary()?;
        loop {
            match () {
                _ if self.matches(TType::LeftParen) => {
                    let mut arguments: Vec<Expression> = Vec::new();
                    if !self.check(TType::RightParen) {
                        loop {
                            arguments.push(self.expression()?);
                            if !self.matches(TType::Comma) {
                                break;
                            }
                        }
                    }

                    self.consume(TType::RightParen, "Expected ')' after call arguments.")?;
                    expression = Expression::Call {
                        callee: Box::new(expression),
                        arguments,
                    }
                }

                _ if self.check(TType::LeftBracket) => {
                    let bracket = self.advance();
                    let index = self.expression()?;
                    self.consume(TType::RightBracket, "Expected ']' after index.")?;
                    expression = Expression::IndexGet {
                        indexed: Box::new(expression),
                        index: Box::new(index),
                        bracket,
                    }
                }

                _ if self.matches(TType::Dot) => {
                    let (name, generics) = self.generic_identifier()?;
                    if let Some(params) = generics {
                        expression = Expression::GetGeneric {
                            object: Box::new(expression),
                            name,
                            params,
                        }
                    } else {
                        expression = Expression::Get {
                            object: Box::new(expression),
                            name,
                        }
                    }
                }

                _ if self.matches(TType::Colon) => {
                    expression = Expression::GetStatic {
                        object: Box::new(expression),
                        name: self
                            .consume(TType::Identifier, "Expected property name after ':'.")?,
                    }
                }

                _ => break,
            }
        }
        Some(expression)
    }

    fn primary(&mut self) -> Option<Expression> {
        Some(match () {
            _ if self.check(TType::False) => {
                Expression::Literal(Literal::Bool(false), self.advance())
            }
            _ if self.check(TType::True) => {
                Expression::Literal(Literal::Bool(true), self.advance())
            }
            _ if self.matches(TType::LeftParen) => self.grouping_or_closure()?,
            _ if self.check(TType::Identifier) => self.identifier()?,
            _ if self.check(TType::Int) => self.integer()?,
            _ if self.check(TType::Float) => self.float()?,
            _ if self.check(TType::String) => self.string(),
            _ if self.matches(TType::LeftBracket) => self.array()?,
            _ => {
                self.error_at_current("Expected expression.");
                None?
            }
        })
    }

    fn identifier(&mut self) -> Option<Expression> {
        let (name, generics) = self.generic_identifier()?;
        Some(if let Some(generics) = generics {
            Expression::VarWithGenerics { name, generics }
        } else {
            Expression::Variable(name)
        })
    }

    fn generic_identifier(&mut self) -> Option<(Token, Option<Vec<Type>>)> {
        let name = self.advance();

        Some(if self.matches(TType::ColonColon) {
            self.consume(TType::Less, "Expected '<' after '::'.")?;
            let mut generics = Vec::new();
            loop {
                generics.push(self.type_("Expected generic type.")?);
                if !self.matches(TType::Comma) {
                    break;
                }
            }
            self.consume(TType::Greater, "Expected '>' after type parameters.")?;
            (name, Some(generics))
        } else {
            (name, None)
        })
    }

    fn grouping_or_closure(&mut self) -> Option<Expression> {
        if (self.check(TType::Identifier)
            && (self.check_next(TType::Colon) || self.check_next(TType::Comma)))
            || self.check(TType::RightParen)
        {
            self.closure()
        } else {
            self.grouping()
        }
    }

    fn grouping(&mut self) -> Option<Expression> {
        let expression = self.expression()?;
        self.consume(TType::RightParen, "Expected ')' after expression.")?;
        Some(expression)
    }

    fn closure(&mut self) -> Option<Expression> {
        let mut parameters: Vec<ClosureParameter> = Vec::new();
        if !self.check(TType::RightParen) {
            loop {
                let name = self.consume(TType::Identifier, "Expected parameter name.")?;
                let type_ = if self.matches(TType::Colon) {
                    Some(self.type_("Expected parameter type.")?)
                } else {
                    None
                };
                parameters.push(ClosureParameter { type_, name });
                if !self.matches(TType::Comma) {
                    break;
                }
            }
        }
        let tok = self.consume(TType::RightParen, "Expected ')' after parameters.")?;
        let ret_ty = if self.matches(TType::Colon) {
            Some(self.type_("Expected return type after ':'.")?)
        } else {
            None
        };

        self.consume(TType::Arrow, "Expected '->' after closure signature.")?;
        let body = self.expression()?;
        Some(Expression::Literal(
            Literal::Closure(Box::new(Closure {
                parameters,
                ret_ty,
                body,
            })),
            tok,
        ))
    }

    fn array(&mut self) -> Option<Expression> {
        let mut values: Vec<Expression> = Vec::new();
        loop {
            values.push(self.expression()?);
            if self.check(TType::RightBracket) {
                break;
            }
            self.consume(TType::Comma, "Expected ']' or ',' after array value.")?;
        }
        Some(Expression::Literal(
            Literal::Array(Either::Left(Rc::new(values))),
            self.advance(),
        ))
    }

    fn integer(&mut self) -> Option<Expression> {
        let token = self.advance();
        let clone = Rc::clone(&token.lexeme);

        // Search for 'i' or 'u' indicating literal type
        let search = clone
            .chars()
            .enumerate()
            .find(|(_, c)| *c == 'i' || *c == 'u')
            .unwrap_or((clone.len(), 'i'));
        let signed = search.1 == 'i';
        let int = &clone[0..search.0];
        let width = clone.get((search.0 + 1)..);

        self.make_int_literal(int, width.unwrap_or("size"), signed, token)
    }

    fn make_int_literal(
        &mut self,
        num: &str,
        type_: &str,
        signed: bool,
        tok: Token,
    ) -> Option<Expression> {
        Some(Expression::Literal(
            match (&type_[..], signed) {
                ("8", true) => Literal::I8(num.parse().ok()?),
                ("16", true) => Literal::I16(num.parse().ok()?),
                ("32", true) => Literal::I32(num.parse().ok()?),
                ("64", true) => Literal::I64(num.parse().ok()?),
                #[cfg(target_pointer_width = "64")]
                ("size", true) => Literal::I64(num.parse().ok()?),
                #[cfg(not(target_pointer_width = "64"))]
                ("size", true) => Literal::I32(num.parse().ok()?),

                ("8", false) => Literal::U8(num.parse().ok()?),
                ("16", false) => Literal::U16(num.parse().ok()?),
                ("32", false) => Literal::U32(num.parse().ok()?),
                ("64", false) => Literal::U64(num.parse().ok()?),
                #[cfg(target_pointer_width = "64")]
                ("size", false) => Literal::U64(num.parse().ok()?),
                #[cfg(not(target_pointer_width = "64"))]
                ("size", false) => Literal::U32(num.parse().ok()?),

                _ => {
                    self.error_at_current("Invalid integer size.")?;
                    return None;
                }
            },
            tok,
        ))
    }

    fn float(&mut self) -> Option<Expression> {
        let token = self.advance();
        Some(Expression::Literal(
            match &token.lexeme[..1] {
                "f" => Literal::F32(token.lexeme.parse().ok()?),
                _ => Literal::F64(token.lexeme.parse().ok()?),
            },
            token,
        ))
    }

    fn string(&mut self) -> Expression {
        let token = self.advance();
        Expression::Literal(Literal::String(Rc::clone(&token.lexeme)), token)
    }

    // Reads an identifier followed by optional generic type parameters.
    fn generic_ident(&mut self) -> Option<(Token, Option<Vec<GenericParam>>)> {
        let name = self.consume(TType::Identifier, "Expected a name.")?;
        let mut generics = None;
        if self.matches(TType::Less) {
            let mut generics_vec = Vec::with_capacity(1);
            while let Some(type_) = self.match_tokens(&[TType::Identifier]) {
                if self.matches(TType::Colon) {
                    generics_vec.push(GenericParam {
                        name: type_,
                        bound: Some(self.type_("Expected bound after ':'.")?),
                    });
                } else {
                    generics_vec.push(GenericParam {
                        name: type_,
                        bound: None,
                    })
                }
                if !self.matches(TType::Comma) {
                    break;
                }
            }
            self.consume(TType::Greater, "Expected '>' after type parameters.")?;
            generics = Some(generics_vec)
        }
        Some((name, generics))
    }

    fn consume_mods(&mut self) {
        self.modifiers.clear();
        while MODIFIERS.contains(&self.current.t_type) {
            let tok = self.advance();
            self.modifiers.push(tok)
        }
    }

    fn check_mods(&mut self, allowed: &'static [TType], name: &'static str) -> Option<()> {
        let mut msgs = vec![];
        for mod_ in self
            .modifiers
            .iter()
            .filter(|m| !allowed.contains(&m.t_type) && !GLOBAL_MODIFIERS.contains(&m.t_type))
        {
            msgs.push(format!(
                "Cannot have '{}' modifier on {}.",
                mod_.lexeme, name
            ));
        }
        msgs.into_iter().try_for_each(|m| self.error_at_current(&m))
    }

    fn get_visibility(&mut self) -> Option<Visibility> {
        let mut count = 0;
        let mut visibility = Visibility::Module;
        for tok in &self.modifiers {
            let vis = match tok.t_type {
                TType::Public => Visibility::Public,
                TType::Private => Visibility::Private,
                _ => Visibility::Module,
            };
            if vis != Visibility::Module {
                count += 1;
                visibility = vis;
            }
        }
        if count > 1 {
            self.error_at_current("Cannot have more than 1 visibility modifier.")?;
            None
        } else {
            Some(visibility)
        }
    }

    /// Reads a type name.
    fn type_(&mut self, msg: &str) -> Option<Type> {
        let token = self.advance();
        Some(match token.t_type {
            TType::Identifier => {
                if self.matches(TType::Less) {
                    let mut types = Vec::new();
                    loop {
                        types.push(self.type_("Expected generic type.")?);
                        if !self.matches(TType::Comma) {
                            break;
                        }
                    }
                    self.consume(TType::Greater, "Expected '>' after type parameters.")?;

                    Type::Generic { token, types }
                } else {
                    Type::Ident(token)
                }
            }

            TType::Caret => {
                let inner = self.type_(msg)?;
                Type::Value(Box::new(inner))
            }

            TType::Star => {
                let inner = self.type_(msg)?;
                Type::Pointer(Box::new(inner))
            }

            TType::LeftBracket => {
                let arr_type = self.type_("Expected type after '[' in array type.")?;
                self.consume(TType::RightBracket, "Expected ']' after array type.")?;
                Type::Array(Box::new(arr_type))
            }

            TType::LeftParen => {
                let mut params = Vec::new();
                if !self.check(TType::RightParen) {
                    loop {
                        params.push(self.type_("Expected closure parameter type.")?);
                        if !self.matches(TType::Comma) {
                            break;
                        }
                    }
                }

                let closing_paren =
                    self.consume(TType::RightParen, "Expected ')' after closure parameters.")?;

                let ret_type = if self.matches(TType::Colon) {
                    Some(Box::new(self.type_("Expected return type after ':'.")?))
                } else {
                    None
                };

                Type::Closure {
                    params,
                    ret_type,
                    closing_paren,
                }
            }

            _ => {
                self.error_at_current(msg)?;
                None?
            }
        })
    }
}
