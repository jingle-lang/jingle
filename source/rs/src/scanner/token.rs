/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 1:32 AM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::rc::Rc;

/// A token in the gelix language. These are produced by a lexer.
/// Cloning a Token is cheap, since the lexemes are refcounted.
#[derive(Debug, Clone)]
pub struct Token {
    /// The type of the token.
    pub t_type: TType,
    /// The lexeme of the token. Does not include escape chars (ex. String lexeme is <i>I'm a string!</i>)
    pub lexeme: Rc<String>,
    /// The index of the last char of the token inside the source.
    /// This is used for error reporting.
    pub index: usize,
    /// The line of the token.
    pub line: usize,
    /// The length of the token. Even though this can be taken from
    /// the lexeme in most cases, it sometimes differs because the
    /// lexeme was modified.
    pub len: usize,
}

impl Token {
    pub fn eof_token(line: usize) -> Token {
        Token {
            t_type: TType::EndOfFile,
            lexeme: Rc::new("\0".to_string()),
            index: 1,
            line,
            len: 0,
        }
    }

    pub fn generic_identifier(lexeme: String) -> Token {
        let index = lexeme.len();
        Token {
            t_type: TType::Identifier,
            lexeme: Rc::new(lexeme),
            index,
            line: 0,
            len: 0,
        }
    }

    pub fn generic_token(token: TType) -> Token {
        Token {
            t_type: token,
            lexeme: Rc::new("".to_string()),
            index: 0,
            line: 0,
            len: 0,
        }
    }
}

impl PartialEq for Token {
    fn eq(&self, other: &Self) -> bool {
        self.lexeme == other.lexeme
    }
}

/// All types of tokens available. Most are keywords or special chars.
/// The `ScanError` token is a special token signifying a syntax error.
/// Its lexeme is an error message to be displayed to the user.
#[derive(PartialEq, Eq, Debug, Clone, Copy, Hash)]
pub enum TType {
    LeftParen,
    RightParen,
    LeftBracket,
    RightBracket,
    LeftBrace,
    RightBrace,
    Caret,
    Comma,
    Dot,
    Minus,
    Plus,
    Semicolon,
    Colon,
    ColonColon,
    Slash,
    Star,
    Modulo,
    Arrow,

    Bang,
    BangEqual,
    Equal,
    EqualEqual,
    Greater,
    GreaterEqual,
    Less,
    LessEqual,

    Identifier,
    String,
    Int,
    Float,
    Char,

    And,
    Break,
    Case,
    Class,
    Construct,
    Else,
    End,
    Enum,
    Error,
    Export,
    Ext,
    False,
    For,
    Loop,
    From,
    Func,
    If,
    Impl,
    Import,
    In,
    Interface,
    Is,
    Or,
    Return,
    To,
    True,
    Var,
    Val,
    Switch,
    While,

    Public,
    Private,
    Extern,
    Variadic,

    ScanError,
    EndOfFile,
}
