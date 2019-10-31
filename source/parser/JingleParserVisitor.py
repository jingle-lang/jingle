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


    # Visit a parse tree produced by JingleParser#packagePhrase.
    def visitPackagePhrase(self, ctx:JingleParser.PackagePhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#importDecl.
    def visitImportDecl(self, ctx:JingleParser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#importSpec.
    def visitImportSpec(self, ctx:JingleParser.ImportSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#topLevelDecl.
    def visitTopLevelDecl(self, ctx:JingleParser.TopLevelDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#line.
    def visitLine(self, ctx:JingleParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#endOfStatement.
    def visitEndOfStatement(self, ctx:JingleParser.EndOfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#statement.
    def visitStatement(self, ctx:JingleParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#declaration.
    def visitDeclaration(self, ctx:JingleParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#varDecl.
    def visitVarDecl(self, ctx:JingleParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#funcDecl.
    def visitFuncDecl(self, ctx:JingleParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#echoDisplay.
    def visitEchoDisplay(self, ctx:JingleParser.EchoDisplayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#params.
    def visitParams(self, ctx:JingleParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#identifierList.
    def visitIdentifierList(self, ctx:JingleParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#expressionList.
    def visitExpressionList(self, ctx:JingleParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#paramList.
    def visitParamList(self, ctx:JingleParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#paramDecl.
    def visitParamDecl(self, ctx:JingleParser.ParamDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#ifStmt.
    def visitIfStmt(self, ctx:JingleParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#forStmt.
    def visitForStmt(self, ctx:JingleParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#returnStmt.
    def visitReturnStmt(self, ctx:JingleParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#simpleStmt.
    def visitSimpleStmt(self, ctx:JingleParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#incDecStmt.
    def visitIncDecStmt(self, ctx:JingleParser.IncDecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#assign_op.
    def visitAssign_op(self, ctx:JingleParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#shortVarDecl.
    def visitShortVarDecl(self, ctx:JingleParser.ShortVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#emptyStmt.
    def visitEmptyStmt(self, ctx:JingleParser.EmptyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#block.
    def visitBlock(self, ctx:JingleParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#statementList.
    def visitStatementList(self, ctx:JingleParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JingleParser#forClause.
    def visitForClause(self, ctx:JingleParser.ForClauseContext):
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


    # Visit a parse tree produced by JingleParser#dataType.
    def visitDataType(self, ctx:JingleParser.DataTypeContext):
        return self.visitChildren(ctx)



del JingleParser