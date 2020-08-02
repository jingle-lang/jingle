/*
 * Developed by Felix Ang. (felix.ang@pm.me).
 * Last modified on 12/27/19 6:50 PM.
 * This file is under the Apache 2.0 license. See LICENSE in the root of this repository for details.
 */

use std::{convert::TryInto, iter::FromIterator, rc::Rc};

use token::{TType, Token};

pub mod token;

/// A lexer is an iterator that turns gelix source code into [Token]s.
pub struct Lexer {
    /// The chars of the source
    chars: Vec<char>,
    /// The start position of the token currently being scanned
    start: usize,
    /// The current position of the scan
    current: usize,
    /// The line of the current position
    line: usize,
    /// The index of the current position on the current line
    line_index: usize,
}

impl Lexer {
    /// Returns the next token, or None if at EOF.
    fn next_token(&mut self) -> Option<Token> {
        if let Err(tok) = self.skip_whitespace() {
            return Some(tok);
        }

        self.start = self.current;
        let ch = self.advance()?;

        Some(match ch {
            // Single-char
            '(' => self.make_token(TType::LeftParen),
            ')' => self.make_token(TType::RightParen),
            '[' => self.make_token(TType::LeftBracket),
            ']' => self.make_token(TType::RightBracket),
            '{' => self.make_token(TType::LeftBrace),
            '}' => self.make_token(TType::RightBrace),
            ';' => self.make_token(TType::Semicolon),
            ',' => self.make_token(TType::Comma),
            '.' => self.make_token(TType::Dot),
            '+' => self.make_token(TType::Plus),
            '*' => self.make_token(TType::Star),
            '/' => self.make_token(TType::Slash),
            '%' => self.make_token(TType::Modulo),
            '^' => self.make_token(TType::Caret),

            // Double-char
            '!' => self.check_double_token('=', TType::BangEqual, TType::Bang),
            '=' => self.check_double_token('=', TType::EqualEqual, TType::Equal),
            '<' => self.check_double_token('=', TType::LessEqual, TType::Less),
            '>' => self.check_double_token('=', TType::GreaterEqual, TType::Greater),
            '-' => self.check_double_token('>', TType::Arrow, TType::Minus),
            ':' => self.check_double_token(':', TType::ColonColon, TType::Colon),

            // Literals
            '"' => self.string(),
            '\'' => self.ch(),
            _ if ch.is_ascii_digit() => self.number(),

            // Identifiers/Keywords
            _ if (ch.is_alphabetic() || ch == '_') => self.identifier(),

            _ => self.error_token("Unexpected symbol."),
        })
    }

    /// Matches the next char to check for double-char tokens. Will emit token based on match.
    fn check_double_token(&mut self, next: char, matched: TType, not_matched: TType) -> Token {
        let token = if self.match_next(next) {
            matched
        } else {
            not_matched
        };
        self.make_token(token)
    }

    /// Creates an identifier or keyword token.
    fn identifier(&mut self) -> Token {
        while self.peek().is_alphanumeric() || self.check('_') {
            self.advance();
        }
        let mut token = self.make_token(TType::Identifier);

        token.t_type = match &token.lexeme[..] {
            "and" => TType::And,
            "break" => TType::Break,
            "case" => TType::Case,
            "class" => TType::Class,
            "init" => TType::Construct,
            "else" => TType::Else,
            "enum" => TType::Enum,
            "end" => TType::End,
            "error" => TType::Error,
            "export" => TType::Export,
            "ext" => TType::Ext,
            "false" => TType::False,
            "for" => TType::For,
            "from" => TType::From,
            "fn" => TType::Func,
            "if" => TType::If,
            "impl" => TType::Impl,
            "loop" => TType::Loop,
            "using" => TType::Import,
            "in" => TType::In,
            "interface" => TType::Interface,
            "is" => TType::Is,
            "or" => TType::Or,
            "return" => TType::Return,
            "to" => TType::To,
            "true" => TType::True,
            "let" => TType::Val,
            "var" => TType::Var,
            "match" => TType::Switch,

            "public" => TType::Public,
            "private" => TType::Private,
            "extern" => TType::Extern,
            "variadic" => TType::Variadic,

            _ => TType::Identifier,
        };

        token
    }

    /// Creates a Int or Float token
    fn number(&mut self) -> Token {
        while self.peek().is_ascii_digit() {
            self.advance();
        }

        if self.check('.') && self.peek_twice().is_ascii_digit() {
            self.advance();
            while self.peek().is_ascii_digit() {
                self.advance();
            }
            self.match_next('f');
            self.make_token(TType::Float)
        } else {
            if self.match_next('i') || self.match_next('u') {
                while self.peek().is_ascii_alphanumeric() {
                    self.advance();
                }
            }
            self.make_token(TType::Int)
        }
    }

    /// Creates a string token
    fn string(&mut self) -> Token {
        let start_line = self.line;
        while !self.check('"') && !self.is_at_end() {
            if self.check('\n') {
                self.line += 1;
                self.line_index = 0;
            }
            self.advance();
        }

        if self.is_at_end() {
            let mut token = self.error_token("Unterminated string!");
            token.line = start_line;
            token
        } else {
            // Ensure the quotes are not included in the literal
            self.start += 1;
            let token = self.str_escape_seq();
            self.advance();
            token
        }
    }

    /// Replace all escape sequences inside a string literal with their proper char
    /// and return either an error or the finished string token
    fn str_escape_seq(&mut self) -> Token {
        for i in self.start..self.current {
            if self.char_at(i) == '\\' {
                self.chars.remove(i);
                self.current -= 1;
                if self.chars.len() == i {
                    return self.error_token("Unterminated string!");
                }

                self.chars[i] = match self.char_at(i) {
                    'n' => '\n',
                    'r' => '\r',
                    't' => '\t',
                    '\\' => '\\',
                    '0' => '\0',
                    '"' => '"',

                    'u' => {
                        let mut chars = Vec::with_capacity(6);
                        while self.char_at(i + 1).is_ascii_hexdigit() {
                            chars.push(self.chars.remove(i + 1));
                            self.current -= 1;
                        }
                        u32::from_str_radix(&String::from_iter(chars), 16)
                            .unwrap()
                            .try_into()
                            .unwrap()
                    }

                    _ => return self.error_token("Unknown escape sequence."),
                }
            }
        }
        self.make_token(TType::String)
    }

    /// Creates a char token
    fn ch(&mut self) -> Token {
        self.advance();
        if self.match_next('\'') {
            self.make_token(TType::Char)
        } else {
            self.advance();
            self.error_token("Unterminated char literal!")
        }
    }

    /// Creates a token based on the current position of self.start and self.current
    fn make_token(&mut self, t_type: TType) -> Token {
        Token {
            t_type,
            lexeme: Rc::new(self.chars[(self.start)..(self.current)].iter().collect()),
            index: self.line_index,
            line: self.line,
            len: self.current - self.start,
        }
    }

    /// Creates a `ScanError` token with the given message at the current location
    fn error_token(&mut self, message: &'static str) -> Token {
        Token {
            t_type: TType::ScanError,
            lexeme: Rc::new(message.to_string()),
            index: self.line_index + message.len(),
            line: self.line,
            len: message.len(),
        }
    }

    /// Skips all whitespace and comments
    fn skip_whitespace(&mut self) -> Result<(), Token> {
        loop {
            match self.peek() {
                ' ' | '\r' | '\t' => {
                    self.advance();
                }

                '\n' => {
                    self.line += 1;
                    self.line_index = 0;
                    self.advance();
                }

                '#' => {
                    while !self.check('\n') && !self.is_at_end() {
                        self.advance();
                    }
                }

                '/' => match self.peek_twice() {
                    '/' => {
                        while !self.check('\n') && !self.is_at_end() {
                            self.advance();
                        }
                    }

                    '*' => {
                        self.advance();
                        let mut nest_level = 1;

                        while nest_level > 0 && !self.is_at_end() {
                            if self.check_two('*', '/') {
                                nest_level -= 1;
                            } else if self.check_two('/', '*') {
                                nest_level += 1;
                            } else if self.check('\n') {
                                self.line += 1;
                            }
                            self.advance();
                        }

                        if self.is_at_end() {
                            return Err(self.error_token("Unterminated comment"));
                        }

                        self.advance();
                    }

                    _ => return Ok(()),
                },

                _ => return Ok(()),
            }
        }
    }

    /// Is the current cursor at the EOF?
    fn is_at_end(&self) -> bool {
        self.check('\0')
    }

    /// Matches the next char and consumes it if it matches. Returns if it matched.
    fn match_next(&mut self, expected: char) -> bool {
        let matches = self.check(expected);
        if matches {
            self.advance();
        }
        matches
    }

    /// Checks if the next char matches.
    fn check(&self, expected: char) -> bool {
        self.peek() == expected
    }

    /// Checks if the next 2 char match.
    fn check_two(&self, expected: char, expected_second: char) -> bool {
        self.peek() == expected && self.peek_twice() == expected_second
    }

    /// Advances the char pointer by 1 and returns the consumed char, or None at EOF.
    fn advance(&mut self) -> Option<char> {
        if self.is_at_end() {
            None
        } else {
            self.current += 1;
            self.line_index += 1;
            Some(self.char_at(self.current - 1))
        }
    }

    /// Returns the current char without consuming it.
    fn peek(&self) -> char {
        self.char_at(self.current)
    }

    /// Returns the next char without consuming it.
    fn peek_twice(&self) -> char {
        self.char_at(self.current + 1)
    }

    /// Returns the char at the given position or \0 for OOB.
    fn char_at(&self, pos: usize) -> char {
        **self.chars.get(pos).get_or_insert(&'\0')
    }

    /// Create a new lexer for scanning the given source.
    pub fn new(source: &Rc<String>) -> Lexer {
        let chars: Vec<char> = source.chars().collect();
        Lexer {
            chars,
            start: 0,
            current: 0,
            line: 1,
            line_index: 0,
        }
    }
}

impl Iterator for Lexer {
    type Item = Token;

    fn next(&mut self) -> Option<Self::Item> {
        self.next_token()
    }
}
