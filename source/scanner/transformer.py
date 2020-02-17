from llvmlite import ir
import sys
from typing import Optional
from scanner import Lark_StandAlone, Transformer, inline_args
from syntaxtree import (
    Block
)

class JingleAST(Transformer):
    def start(self, node):
        return node

    def top_level_decl(self, node):
        return node[0]

    def expression(self, node):
        return node[0]

    def block(self, node):
        return Block(node[0].pos_in_stream, node[1:-1])

    def atom(self, node):
        return node[0]

    def parenthetical(self, node):
        return node[1]

    def opt_arglist(self, node):
        if not node:
            return node
        return node[0]

    def arglist(self, node):
        return node