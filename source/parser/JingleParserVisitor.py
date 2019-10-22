# Generated from JingleParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JingleParser import JingleParser
else:
    from JingleParser import JingleParser

# This class defines a complete generic visitor for a parse tree produced by JingleParser.

class JingleParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JingleParser#jingleFile.
    def visitJingleFile(self, ctx:JingleParser.JingleFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#line.
    def visitLine(self, ctx:JingleParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#statement.
    def visitStatement(self, ctx:JingleParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#varDeclaration.
    def visitVarDeclaration(self, ctx:JingleParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#stmtDisplay.
    def visitStmtDisplay(self, ctx:JingleParser.StmtDisplayContext):
        return self.visitChildren(ctx)



del JingleParser