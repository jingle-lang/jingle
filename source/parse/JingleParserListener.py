# Generated from JingleParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JingleParser import JingleParser
else:
    from JingleParser import JingleParser

# This class defines a complete listener for a parse tree produced by JingleParser.
class JingleParserListener(ParseTreeListener):

    # Enter a parse tree produced by JingleParser#jingleFile.
    def enterJingleFile(self, ctx:JingleParser.JingleFileContext):
        pass

    # Exit a parse tree produced by JingleParser#jingleFile.
    def exitJingleFile(self, ctx:JingleParser.JingleFileContext):
        pass


    # Enter a parse tree produced by JingleParser#packagePhrase.
    def enterPackagePhrase(self, ctx:JingleParser.PackagePhraseContext):
        pass

    # Exit a parse tree produced by JingleParser#packagePhrase.
    def exitPackagePhrase(self, ctx:JingleParser.PackagePhraseContext):
        pass


    # Enter a parse tree produced by JingleParser#importDecl.
    def enterImportDecl(self, ctx:JingleParser.ImportDeclContext):
        pass

    # Exit a parse tree produced by JingleParser#importDecl.
    def exitImportDecl(self, ctx:JingleParser.ImportDeclContext):
        pass


    # Enter a parse tree produced by JingleParser#importSpec.
    def enterImportSpec(self, ctx:JingleParser.ImportSpecContext):
        pass

    # Exit a parse tree produced by JingleParser#importSpec.
    def exitImportSpec(self, ctx:JingleParser.ImportSpecContext):
        pass


    # Enter a parse tree produced by JingleParser#topLevelDecl.
    def enterTopLevelDecl(self, ctx:JingleParser.TopLevelDeclContext):
        pass

    # Exit a parse tree produced by JingleParser#topLevelDecl.
    def exitTopLevelDecl(self, ctx:JingleParser.TopLevelDeclContext):
        pass


    # Enter a parse tree produced by JingleParser#line.
    def enterLine(self, ctx:JingleParser.LineContext):
        pass

    # Exit a parse tree produced by JingleParser#line.
    def exitLine(self, ctx:JingleParser.LineContext):
        pass


    # Enter a parse tree produced by JingleParser#endOfStatement.
    def enterEndOfStatement(self, ctx:JingleParser.EndOfStatementContext):
        pass

    # Exit a parse tree produced by JingleParser#endOfStatement.
    def exitEndOfStatement(self, ctx:JingleParser.EndOfStatementContext):
        pass


    # Enter a parse tree produced by JingleParser#statement.
    def enterStatement(self, ctx:JingleParser.StatementContext):
        pass

    # Exit a parse tree produced by JingleParser#statement.
    def exitStatement(self, ctx:JingleParser.StatementContext):
        pass


    # Enter a parse tree produced by JingleParser#declaration.
    def enterDeclaration(self, ctx:JingleParser.DeclarationContext):
        pass

    # Exit a parse tree produced by JingleParser#declaration.
    def exitDeclaration(self, ctx:JingleParser.DeclarationContext):
        pass


    # Enter a parse tree produced by JingleParser#varDecl.
    def enterVarDecl(self, ctx:JingleParser.VarDeclContext):
        pass

    # Exit a parse tree produced by JingleParser#varDecl.
    def exitVarDecl(self, ctx:JingleParser.VarDeclContext):
        pass


    # Enter a parse tree produced by JingleParser#funcDecl.
    def enterFuncDecl(self, ctx:JingleParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by JingleParser#funcDecl.
    def exitFuncDecl(self, ctx:JingleParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by JingleParser#echoDisplay.
    def enterEchoDisplay(self, ctx:JingleParser.EchoDisplayContext):
        pass

    # Exit a parse tree produced by JingleParser#echoDisplay.
    def exitEchoDisplay(self, ctx:JingleParser.EchoDisplayContext):
        pass


    # Enter a parse tree produced by JingleParser#params.
    def enterParams(self, ctx:JingleParser.ParamsContext):
        pass

    # Exit a parse tree produced by JingleParser#params.
    def exitParams(self, ctx:JingleParser.ParamsContext):
        pass


    # Enter a parse tree produced by JingleParser#identifierList.
    def enterIdentifierList(self, ctx:JingleParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by JingleParser#identifierList.
    def exitIdentifierList(self, ctx:JingleParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by JingleParser#expressionList.
    def enterExpressionList(self, ctx:JingleParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by JingleParser#expressionList.
    def exitExpressionList(self, ctx:JingleParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by JingleParser#paramList.
    def enterParamList(self, ctx:JingleParser.ParamListContext):
        pass

    # Exit a parse tree produced by JingleParser#paramList.
    def exitParamList(self, ctx:JingleParser.ParamListContext):
        pass


    # Enter a parse tree produced by JingleParser#paramDecl.
    def enterParamDecl(self, ctx:JingleParser.ParamDeclContext):
        pass

    # Exit a parse tree produced by JingleParser#paramDecl.
    def exitParamDecl(self, ctx:JingleParser.ParamDeclContext):
        pass


    # Enter a parse tree produced by JingleParser#ifStmt.
    def enterIfStmt(self, ctx:JingleParser.IfStmtContext):
        pass

    # Exit a parse tree produced by JingleParser#ifStmt.
    def exitIfStmt(self, ctx:JingleParser.IfStmtContext):
        pass


    # Enter a parse tree produced by JingleParser#forStmt.
    def enterForStmt(self, ctx:JingleParser.ForStmtContext):
        pass

    # Exit a parse tree produced by JingleParser#forStmt.
    def exitForStmt(self, ctx:JingleParser.ForStmtContext):
        pass


    # Enter a parse tree produced by JingleParser#returnStmt.
    def enterReturnStmt(self, ctx:JingleParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by JingleParser#returnStmt.
    def exitReturnStmt(self, ctx:JingleParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by JingleParser#simpleStmt.
    def enterSimpleStmt(self, ctx:JingleParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by JingleParser#simpleStmt.
    def exitSimpleStmt(self, ctx:JingleParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by JingleParser#incDecStmt.
    def enterIncDecStmt(self, ctx:JingleParser.IncDecStmtContext):
        pass

    # Exit a parse tree produced by JingleParser#incDecStmt.
    def exitIncDecStmt(self, ctx:JingleParser.IncDecStmtContext):
        pass


    # Enter a parse tree produced by JingleParser#assign_op.
    def enterAssign_op(self, ctx:JingleParser.Assign_opContext):
        pass

    # Exit a parse tree produced by JingleParser#assign_op.
    def exitAssign_op(self, ctx:JingleParser.Assign_opContext):
        pass


    # Enter a parse tree produced by JingleParser#shortVarDecl.
    def enterShortVarDecl(self, ctx:JingleParser.ShortVarDeclContext):
        pass

    # Exit a parse tree produced by JingleParser#shortVarDecl.
    def exitShortVarDecl(self, ctx:JingleParser.ShortVarDeclContext):
        pass


    # Enter a parse tree produced by JingleParser#emptyStmt.
    def enterEmptyStmt(self, ctx:JingleParser.EmptyStmtContext):
        pass

    # Exit a parse tree produced by JingleParser#emptyStmt.
    def exitEmptyStmt(self, ctx:JingleParser.EmptyStmtContext):
        pass


    # Enter a parse tree produced by JingleParser#block.
    def enterBlock(self, ctx:JingleParser.BlockContext):
        pass

    # Exit a parse tree produced by JingleParser#block.
    def exitBlock(self, ctx:JingleParser.BlockContext):
        pass


    # Enter a parse tree produced by JingleParser#statementList.
    def enterStatementList(self, ctx:JingleParser.StatementListContext):
        pass

    # Exit a parse tree produced by JingleParser#statementList.
    def exitStatementList(self, ctx:JingleParser.StatementListContext):
        pass


    # Enter a parse tree produced by JingleParser#forClause.
    def enterForClause(self, ctx:JingleParser.ForClauseContext):
        pass

    # Exit a parse tree produced by JingleParser#forClause.
    def exitForClause(self, ctx:JingleParser.ForClauseContext):
        pass


    # Enter a parse tree produced by JingleParser#parenExpression.
    def enterParenExpression(self, ctx:JingleParser.ParenExpressionContext):
        pass

    # Exit a parse tree produced by JingleParser#parenExpression.
    def exitParenExpression(self, ctx:JingleParser.ParenExpressionContext):
        pass


    # Enter a parse tree produced by JingleParser#binaryOperation.
    def enterBinaryOperation(self, ctx:JingleParser.BinaryOperationContext):
        pass

    # Exit a parse tree produced by JingleParser#binaryOperation.
    def exitBinaryOperation(self, ctx:JingleParser.BinaryOperationContext):
        pass


    # Enter a parse tree produced by JingleParser#typeConversion.
    def enterTypeConversion(self, ctx:JingleParser.TypeConversionContext):
        pass

    # Exit a parse tree produced by JingleParser#typeConversion.
    def exitTypeConversion(self, ctx:JingleParser.TypeConversionContext):
        pass


    # Enter a parse tree produced by JingleParser#dataType.
    def enterDataType(self, ctx:JingleParser.DataTypeContext):
        pass

    # Exit a parse tree produced by JingleParser#dataType.
    def exitDataType(self, ctx:JingleParser.DataTypeContext):
        pass


