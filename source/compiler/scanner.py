# scanner.py
from .errors import error
from sly import Lexer

class JingleLexer(Lexer):

    tokens = {
        # Keywords
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

    ignore = ' \t\r'

    @_(r'/\*(.|\n)*?\*/')
    def BLOCK_COMMENT(self, token):
        self.lineno += token.value.count('\n')
        return None

    @_(r'//.*')
    def LINE_COMMENT(self, token):
        return None

    @_(r'\n+')
    def NEWLINE(self, token):
        self.lineno += token.value.count('\n')

    LE = r'<='
    LT = r'<'
    GE = r'>='
    GT = r'>'
    EQ = r'=='
    NE = r'!='
    AND = r'&&'
    OR = r'\|\|'
    NOT = r'!'

    PLUS = r'\+'
    MINUS = r'-'
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

    FLOAT = r'(((\d+\.\d*)|(\.\d+))([eE][+-]?\d+)?)|(\d+[eE][+-]?\d+)'

    INTEGER = r'(0x[0-9ABCDEF]+)|(0b[01]+)|(0o[0-5]+)|\d+'

    CHAR = r"'((\\n)|(\\x[0-9a-f]{2})|(\\')|(\\\\)|.)'"

    BOOL = r'(true)|(false)'

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
#    bash % python3 -m jingle.scanner filename.jn
#
# ----------------------------------------------------------------------
def main():
    '''
    Main program. For debugging purposes.
    '''
    import sys

    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python3 -m jingle.scanner filename\n")
        raise SystemExit(1)

    lexer = JingleLexer()
    text = open(sys.argv[1]).read()
    for tok in lexer.tokenize(text):
        print(tok)

if __name__ == '__main__':
    main()

