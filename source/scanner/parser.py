# Jingle Parser
import time
start_time = time.time()

def parseScan():
    from scanner import Lark_StandAlone
    parser = Lark_StandAlone()
    input = open("testfile.jn", "r")
    input = input.read()
    tree = parser.parse(input)
    print(tree.pretty())

parseScan()

final_time = time.time() - start_time
final_time = round(final_time, 3)
print("--- %s seconds ---" % (final_time))