from llvmlite import ir
from typing import Optional

class ASTNode:
    """
    Base type for all AST nodes, with helper functions.
    """

    def __init__(self, index):
        self.child = None
        self.index = index

    def __eq__(self, other):
        raise NotImplementedError

    def flatten(self):
        return [self.__class__.__name__, "flatten unimplemented"]

class Expression(ASTNode):
    """
    Base type for all expressions.
    """

    pass

class Keyword(ASTNode):
    """
    Base type for keywords.
    """

    pass

class TopLevel(ASTNode):
    """
    Mixin type for top-level AST nodes.
    """

    pass

class VarTypeNode(Expression):
    name: Optional[str] = None

class Block(Expression):
    """
    {}-delimeted set of expressions, stored as a list in `body`.
    """

    def __init__(self, p, body):
        super().__init__(p)
        self.body = body

    def __eq__(self, other):
        return self.body == other.body

    def flatten(self):
        return [self.__class__.__name__, [_.flatten() for _ in self.body]]