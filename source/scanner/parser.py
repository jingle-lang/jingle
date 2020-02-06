# Jingle Parser

from scanner import Lark_StandAlone
parser = Lark_StandAlone()
input = open("testfile.jn", "r")
input = input.read()
tree = parser.parse(input)
print(tree.pretty())