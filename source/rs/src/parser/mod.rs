/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:54 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{iter::Peekable, mem, rc::Rc};

use crate::{
    scanner::{
        token::{TType, Token},
        Lexer,
    },
    parser::parsing::MODIFIERS,
    Error, ModulePath,
};

mod parsing;

/// A parser that turns a stream of [Token]s into an AST.
pub struct Parser {
    /// The path of the module this parser is parsing.
    /// Required for error display.
    module_path: Rc<ModulePath>,

    /// The token stream used.
    tokens: Peekable<Lexer>,

    /// The token currently being processed.
    current: Token,
    /// The line of the token before the current one.
    previous_line: usize,

    /// If an error occurred while creating a declaration, it will be put in this Vec.
    /// If it is empty, parsing was successful.
    errors: Vec<Error>,

    /// Stores the modifiers of the current global declaration.
    modifiers: Vec<Token>,
}

/// This impl block contains all 'helper' functions of the parser.
/// These functions do not generate AST themselves, and are only used by other functions
/// to manipulate the stream of tokens.
impl Parser {
    /// Checks if the current token is the given type. If yes, it consumes it.
    fn matches(&mut self, t_type: TType) -> bool {
        let matches = self.check(t_type);
        if matches {
            self.advance();
        }
        matches
    }

    /// Same as `match_token`, but checks for multiple types. Returns the token consumed.
    fn match_tokens(&mut self, types: &[TType]) -> Option<Token> {
        if types.iter().any(|&t| self.check(t)) {
            Some(self.advance())
        } else {
            None
        }
    }

    /// Consumes the current token if it is the type given.
    /// Will return None if the token was not the one that was expected.
    fn consume(&mut self, t_type: TType, message: &'static str) -> Option<Token> {
        if self.check(t_type) {
            Some(self.advance())
        } else {
            self.error_at_current(message);
            None
        }
    }

    /// Same as consume, but consumes semicolons or newlines.
    /// Also does not return a token, since newlines are not tokens.
    /// (This special function is needed because of this)
    fn consume_semi_or_nl(&mut self, message: &'static str) -> Option<()> {
        if self.matches(TType::Semicolon) || self.previous_line != self.current.line {
            Some(())
        } else {
            self.error_at_current(message);
            None
        }
    }

    /// Sets self.current to the next token and returns the last token.
    /// If at the end of tokens, self.current is set to an `EndOfFile` token.
    /// Advancing after the end will simply return `EndOfFile` tokens indefinitely.
    fn advance(&mut self) -> Token {
        self.previous_line = self.current.line;

        let next_token = self
            .tokens
            .next()
            .unwrap_or_else(|| Token::eof_token(self.current.line + 1));
        let old_token = mem::replace(&mut self.current, next_token);

        if self.check(TType::ScanError) {
            self.lexer_error();
        }

        old_token
    }

    /// Is the current token the given token?
    fn check(&self, t_type: TType) -> bool {
        self.current.t_type == t_type
    }

    /// Is the next token the given token?
    fn check_next(&mut self, t_type: TType) -> bool {
        self.tokens.peek().unwrap_or(&Token::eof_token(0)).t_type == t_type
    }

    /// Same as check, but checks for ; or newlines
    /// (This special function is needed since newlines are not a token)
    fn check_semi_or_nl(&mut self) -> bool {
        self.check(TType::Semicolon) || self.previous_line != self.current.line
    }

    /// Is the parser at the end of the token stream?
    fn is_at_end(&self) -> bool {
        self.current.t_type == TType::EndOfFile
    }

    /// Causes an error at the current token with the given message.
    /// Will set appropriate state.
    /// Returns None; allows returning from calling function with ?
    fn error_at_current(&mut self, message: &str) -> Option<()> {
        let error = Error::new(
            &self.current,
            "Parser",
            message.to_string(),
            &self.module_path,
        );
        self.errors.push(error);
        None
    }

    /// Reports an error produced by the lexer.
    fn lexer_error(&mut self) {
        let error = Error::new(
            &self.current,
            "Lexer",
            (*self.current.lexeme).clone(),
            &self.module_path,
        );
        self.errors.push(error);
    }

    /// Will attempt to sync after an error to allow compilation to continue.
    /// This allows displaying more than 1 error at a time.
    /// To re-sync, the parser looks for tokens that could indicate the start of a new declaration.
    fn synchronize(&mut self) {
        // Prevents not properly syncing when a declaration was inside another one
        self.advance();

        while !self.is_at_end() {
            match self.current.t_type {
                TType::Impl | TType::Import | TType::Class | TType::Enum | TType::Func => return,
                _ if MODIFIERS.contains(&self.current.t_type) => return,
                _ => (),
            }
            self.advance();
        }
    }

    /// Creates a new parser for parsing the given tokens.
    pub fn new(tokens: Lexer, module_path: Rc<ModulePath>) -> Parser {
        let mut parser = Parser {
            module_path,
            tokens: tokens.peekable(),

            current: Token::eof_token(0),
            previous_line: 0,

            errors: vec![],
            modifiers: vec![],
        };

        // Set state correctly.
        parser.advance();
        parser
    }
}
