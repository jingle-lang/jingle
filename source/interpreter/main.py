import sys
from lark import Lark
from lark.tree import Tree

from src import environment, visitor

if __name__ == '__main__':
    program = open(sys.argv[1]).read()

    rule = open('liteGrammar.lark').read()
    parser = Lark(rule, start='start', parser='lalr')

    tree = parser.parse(program)

    global_env = environment.Environment(None)

    _visitor = visitor.Visitor()
    result = _visitor.visit(tree, global_env)

    print(f'Result: {result}')
