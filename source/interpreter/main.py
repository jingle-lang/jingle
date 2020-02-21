import sys
import time
from lark import Lark
from lark.tree import Tree

from src import environment, visitor

start_time = time.time()

if __name__ == '__main__':
    program = open(sys.argv[1]).read()

    rule = open('jingleLite.txt').read()
    parser = Lark(rule, start='program', parser='lalr')

    tree = parser.parse(program)

    global_env = environment.Environment(None)

    _visitor = visitor.Visitor()
    result = _visitor.visit(tree, global_env)

    print(f'\njingle result => {result}\n')
    final_time = time.time() - start_time
    final_time = round(final_time, 3)
    print("--- Complete after %s seconds ---" % (final_time))
