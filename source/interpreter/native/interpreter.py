import sys
import antlr4 
# -- These imports only work for local files, 
# -- once interpreter is functional work on, 
# -- allowing imports from other folders
import JingleLexer
import JingleParser
import JingleParserVisitor
import JingleParserListener

testfile = 'var test = 5'

class yourGrammarNameParser(object):
    """
    Debugger class - accepts a single input script and processes
    all subsequent requirements
    """
def __init__(self): # this method creates the class object.
    pass
              
#function used to parse an input file
def parse(argv):
    if len(sys.argv) > 1:
        input = antlr4.FileStream(sys.argv[1])
        lexer = JingleLexer(input) 
        stream = antlr4.TokenStream(lexer)
        parser = JingleParser(stream)
        tree = parser.program() 
        printer = JingleParserVisitor(tree,input)
        walker = antlr4.ParseTreeWalker()
        walker.walk(printer, tree)
    else:
        print('Error : Expected a valid file')


#def __main__():
#    inputs = FileStream(sys.argv[1])
#    lexer = JingleLexer(inputs)
#    tokens = CommonTokenStream(lexer)
#    parser = JingleParser(tokens)
#    tree = parser.expression()
#    r = parser.prog()
#    root = r.tree

#def main(argv):
#    input_stream = FileStream(argv[1])
#    lexer = JingleLexer(input_stream)
#    stream = antlr4.CommonTokenStream(lexer)
#    parser = JingleParser(stream)
#    tree = parser.startRule()
 
#if __name__ == '__main__':
#    main(sys.argv)
    
