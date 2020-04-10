# gone/tokenizer.py
r'''
Project 1 - Write a Lexer
=========================
In the first project, you are going to write a simple lexer for a
subset of the Gone language.  The project is presented as code that
you must read and extend (this file).  Please read the complete
contents of this file and carefully complete the steps indicated by
comments.

Overview:
---------
The process of lexing is that of taking input text and breaking it
down into a stream of tokens. Each token is like a valid word from the
dictionary.  Essentially, the role of the lexer is to simply make sure
that the input text consists of valid symbols and tokens prior to any
further processing related to parsing.

Each token is defined by a regular expression.  Thus, your primary task
in this first project is to define a set of regular expressions for
the language.  The actual job of lexing will be handled by SLY
(https://github.com/dabeaz/sly)

Specification:
--------------
Your lexer must recognize the following symbols and tokens.  The name
on the left is the token name, the value on the right is the matching
text.  Note: Additional features will be added in later projects.

Reserved Keywords:
    CONST   : 'const'
    VAR     : 'var'
    PRINT   : 'print'

Identifiers (Same rules as for Python):
    ID      : Text starting with a letter or '_', followed by any number
              number of letters, digits, or underscores.
              Examples:  'abc' 'ABC' 'abc123' '_abc' 'a_b_c'

Operators and Delimiters:
    PLUS     : '+'
    MINUS    : '-'
    TIMES    : '*'
    DIVIDE   : '/'
    ASSIGN   : '='
    SEMI     : ';'
    LPAREN   : '('
    RPAREN   : ')'

Literals:
    INTEGER :  123   (decimal)

    FLOAT   : 1.234
              .1234
              1234.

    CHAR    : 'a'     (a single character - byte)
              '\''    The quote
              '\n'    Newline
              '\\'    Backslash
              '\xhh'  (byte value)


Comments:  To be ignored by your lexer
     //             Skips the rest of the line
     /* ... */      Skips a block (no nesting allowed)

Errors: Your lexer must recognized and report the following error messages:

     lineno: Illegal char 'c'
     lineno: Unterminated character constant
     lineno: Unterminated comment

Testing
-------
To get started, look at Tests/lextest[0-5].g.  Work through each file
in sequence.  Run your tokenize like this:

     bash % python3 -m gone.tokenizer lextest0.g
     bash % python3 -m gone.tokenizer lextest1.g

Bonus: Think about how to write proper unit tests.
'''

# ----------------------------------------------------------------------
# The following import loads a function error(lineno, msg) that should be
# used to report all error messages issued by your lexer.  Unit tests and
# other features of the compiler will rely on this function.  See the
# file errors.py for more documentation about the error handling mechanism.
from .errors import error

# -----------------------------------------------------------------------
# The SLY package. https://github.com/dabeaz/sly
from sly import Lexer

# -----------------------------------------------------------------------
# Lexers are defined by a class that inherits from sly.Lexer.  Follow
# the instructions contained in the class below.

class GoneLexer(Lexer):
    # ----------------------------------------------------------------------
    # Token set. This set identifies the complete list of token names
    # to be recognized by your lexer.  A few tokens have been given, you'll
    # need to add more (see description above)

    tokens = {
        # keywords
        'ECHO', 'CONST', 'ELSE', 'EXTERN', 'FN', 'IF', 'RETURN', 'WHILE', 'VAR', 'END',

        # Identifiers
        'ID',

        # Literals
        'INTEGER', 'FLOAT', 'CHAR', 'BOOL',

        # Operators
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN', 'SEMI', 'COMA',

        # Bool operators
        'LE', 'LT', 'GE', 'GT', 'EQ', 'NE', 'AND', 'OR', 'NOT',

        # Other symbols
        'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COLON',
    }

    # ----------------------------------------------------------------------
    # Ignored characters (whitespace)
    #
    # The following individual characters are ignored completely by the lexer
    # when they appear between tokens.  Do not change.
    ignore = ' \t\r'

    # ----------------------------------------------------------------------
    # Ignored patterns.  You'll need to supply appropriate regexes.
    # For example:
    #
    #    ignore_COMMENT = r'regex for a block-style-comment'
    #
    # or
    #
    #    @_(r'regex for a block-style comment')
    #    def COMMENT(self, t):
    #        ... some processing ...
    #        return None
    #

    @_(r'/\*(.|\n)*?\*/')
    def BLOCK_COMMENT(self, token):
        # We must make sure to move forward the line count for multiline
        # comments !
        self.lineno += token.value.count('\n')
        return None

    @_(r'//.*')
    def LINE_COMMENT(self, token):
        # For this case, it's not necessary to parse any newline
        return None

    @_(r'\n+')
    def NEWLINE(self, token):
        self.lineno += token.value.count('\n')

    # ----------------------------------------------------------------------
    # *** YOU MUST COMPLETE : write the regexs indicated below ***
    #
    # Tokens for simple symbols: + - * / = ( ) ;
    #
    # Caution: Definition order matters. Longer symbols should appear
    # before shorter symbols that are a substring (for example, the
    # pattern for <= should go before <).

    LE = r'<='
    LT = r'<'
    GE = r'>='
    GT = r'>'
    EQ = r'=='
    NE = r'!='
    AND = r'&&'
    OR = r'\|\|'
    NOT = r'!'

    PLUS = r'\+'      # Regex for a single plus sign
    MINUS = r'-'      # Regex for a single minur sign
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    SEMI = r';'
    COMA = r','
    LPAREN = r'\('
    RPAREN = r'\)'

    LBRACE = r'{'
    RBRACE = r'}'
    COLON = r':'

    # ----------------------------------------------------------------------
    # *** YOU MUST COMPLETE : write the regexs and additional code below ***
    #
    # Tokens for literals, INTEGER, FLOAT, STRING.

    # Floating point constant.   You must recognize floating point numbers in
    # the following formats:
    #
    #   1.23
    #   123.
    #   .123
    #
    # Bonus: Recognize floating point numbers in scientific notation
    #
    #   1.23e1
    #   1.23e+1
    #   1.23e-1
    #   1e1

    FLOAT = r'(((\d+\.\d*)|(\.\d+))([eE][+-]?\d+)?)|(\d+[eE][+-]?\d+)'

    # Integer literal
    #
    #     1234             (decimal)
    #
    # Bonus: Recognize integers in different bases such as 0x1a, 0o13 or 0b111011.

    INTEGER = r'(0x[0-9ABCDEF]+)|(0b[01]+)|(0o[0-5]+)|\d+'

    # Character constant. You must recognize a single letter enclosed in single quotes
    # For example:
    #
    #     'a'
    #
    # Escape codes should also be be recognized:
    #
    #     '\n'    - Newline
    #     '\\'    - Backslash
    #     '\''    - Quote
    #     '\xhh'  - Generic byte

    CHAR = r"'((\\n)|(\\x[0-9a-f]{2})|(\\')|(\\\\)|.)'"

    BOOL = r'(true)|(false)'

    # ----------------------------------------------------------------------
    # *** YOU MUST COMPLETE : Write the regex and add keywords ***
    #
    # Identifiers and keywords.
    #
    # Match a raw identifier. Identifiers follow the same rules as Python.
    # That is, they start with a letter or underscore (_) and can contain
    # an arbitrary number of letters, digits, or underscores after that.
    # Language keywords such as "if" and "while" are also matched as
    # identifiers. You need to catch these and change their token type
    # to match the appropriate keyword.

    @_(r'[a-zA-Z_][a-zA-Z0-9_]*')
    def ID(self, t):
        keywords = {
            'const',
            'else',
            'extern',
            'fn',
            'if',
            'echo',
            'return',
            'while',
            'var',
            'end'
        }
        if t.value in keywords:
            t.type = t.value.upper()
        return t

    # ----------------------------------------------------------------------
    # Bad character error handling
    def error(self, t):
        error(self.lineno,"Illegal character %r" % t.value[0])
        self.index += 1

# ----------------------------------------------------------------------
#                DO NOT CHANGE ANYTHING BELOW THIS PART
#
# Use this main program to test/debug your lexer.  Run it using the -m option
#
#    bash % python3 -m gone.tokenizer filename.g
#
# ----------------------------------------------------------------------
def main():
    '''
    Main program. For debugging purposes.
    '''
    import sys

    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 -m gone.tokenizer filename\n")
        raise SystemExit(1)

    lexer = GoneLexer()
    text = open(sys.argv[1]).read()
    for tok in lexer.tokenize(text):
        print(tok)

if __name__ == '__main__':
    main()

