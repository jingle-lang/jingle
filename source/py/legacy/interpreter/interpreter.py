import sys
import time
from lark import Lark

import src

start_time = time.time()

def RunMain(input):
    input = open(sys.argv[1]).read()

    rule = open('jingleLite.txt').read()
    parser = Lark(rule, start='program', parser='lalr')

    tree = parser.parse(input)

    global_env = src.environment.Environment(None)

    _visitor = src.visitor.Visitor()
    result = _visitor.visit(tree, global_env)

    print(f'\njingle => {result}\n')
    final_time = time.time() - start_time
    final_time = round(final_time, 3)
    print("--- Complete after %s seconds ---" % (final_time))

class JnInterp:
    def Run(input):
        rule = open('jingleLite.txt').read()
        parser = Lark(rule, start='program', parser='lalr')

        tree = parser.parse(input)

        global_env = src.environment.Environment(None)

        _visitor = src.visitor.Visitor()
        result = _visitor.visit(tree, global_env)

        print(f'\njingle => {result}\n')
        final_time = time.time() - start_time
        final_time = round(final_time, 3)
        print("--- Complete after %s seconds ---" % (final_time))

if __name__ == '__main__':
    RunMain(input)
else:
    JnInterp.Run(input)