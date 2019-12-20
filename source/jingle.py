## Jingle Language v0.01

import sys
from antlr4 import *
from parse.JingleLexer import JingleLexer
from parse.JingleParser import JingleParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JingleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JingleParser(stream)
    tree = parser.top_level_decl()
 
if __name__ == '__main__':
    main(sys.argv)