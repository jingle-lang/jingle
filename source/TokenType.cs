using System;
using System.Collections.Generic;
using System.Text;

namespace Jingle
{
    public enum TokenType
    {
        LEFT_PAREN, RIGHT_PAREN, COLON, MODULO, INTDIV,
        COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR,

        BANG, BANG_EQUAL,
        EQUAL, EQUAL_EQUAL,
        GREATER, GREATER_EQUAL,
        LESS, LESS_EQUAL,

        IDENTIFIER, STRING, NUMBER,

        AND, CLASS, ECHO, ELSE, END, FALSE, FOR, FN, IF,
        NIL, OR, RETURN, SUPER, THIS, TRUE, VAR, WHILE,

        EOF
    }
}
