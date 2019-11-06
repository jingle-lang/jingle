import sys
from antlr4 import *
from llvmlite import ir
from JingleLexer import *
from JingleParser import *
from JingleParserVisitor import *

class SymbolTable:
    def __init__(self):
        self._symbols = [dict()]

    def push_frame(self, symbols=None):
        symbols = dict() if symbols is None else symbols
        self._symbols.append(symbols)

    def pop_frame(self):
        self._symbols.pop()

    def resolve(self, ide):
        for frame in reversed(self._symbols):
            try:
                return frame[ide]
            except KeyError:
                pass
        raise IndexError

    def bind(self, ide, ptr):
        self._symbols[-1][ide] = ptr

class CodeGenerator(JingleParserVisitor):
    def __init__(self):
        self.types = {
            'void': ir.VoidType(),
            'int': ir.IntType(32),
            'float': ir.FloatType,
            
        }
        self.module = ir.module()
        self.symbols = SymbolTable()

if __name__ == '__main__':
    inputs = FileStream(sys.argv[1])
    lexer = JingleLexer(inputs)
    tokens = CommonTokenStream(lexer)
    parser = JingleParser(tokens)
    tree = parser.program()
    codegen = CodeGenerator()
    codegen.visit(tree)
    print(codegen.module)
    