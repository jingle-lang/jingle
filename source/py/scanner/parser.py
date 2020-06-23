###
###
###

# Required Imports
from scanner import LALRParser # Remember to update this in generated parser!

#Optional Imports
import time
from lark import Lark, Transformer, Tree, Discard, v_args, UnexpectedInput, exceptions
start_time = time.time()


def parseScan():
    parser = Lark_StandAlone()
    input = open("testfile.jn", "r")
    input = input.read()
    tree = parser.parse(input)
    print(tree.pretty())
    final_time = time.time() - start_time
    final_time = round(final_time, 3)
    print("--- Parsing complete after %s seconds ---" % (final_time))

# Singular Parse Testing
#
parseScan()

# Repeated parse testing
#
#parseCounts = 100
#while parseCounts > 0:
#    parseScan()
#    parseCounts = parseCounts - 1

# Infinite parse testing
#
#while True:
#    parseScan()
