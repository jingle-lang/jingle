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


    # Visit a parse tree produced by JingleParser#varDeclarationStatement.
    def visitVarDeclarationStatement(self, ctx:JingleParser.VarDeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:JingleParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#displayStatement.
    def visitDisplayStatement(self, ctx:JingleParser.DisplayStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#display.
    def visitDisplay(self, ctx:JingleParser.DisplayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#varDeclaration.
    def visitVarDeclaration(self, ctx:JingleParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#assignment.
    def visitAssignment(self, ctx:JingleParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:JingleParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#minusExpression.
    def visitMinusExpression(self, ctx:JingleParser.MinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#intLiteral.
    def visitIntLiteral(self, ctx:JingleParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#parenExpression.
    def visitParenExpression(self, ctx:JingleParser.ParenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#binaryOperation.
    def visitBinaryOperation(self, ctx:JingleParser.BinaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#typeConversion.
    def visitTypeConversion(self, ctx:JingleParser.TypeConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#varReference.
    def visitVarReference(self, ctx:JingleParser.VarReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#integer.
    def visitInteger(self, ctx:JingleParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#decimal.
    def visitDecimal(self, ctx:JingleParser.DecimalContext):
        return self.visitChildren(ctx)



del JingleParser