
// Generated from JingleParser.g4 by ANTLR 4.7.2

#pragma once


#include "../cpp/antlr4-runtime/antlr4-runtime.h"
#include "JingleParser.h"


namespace Jingle {

/**
 * This class defines an abstract visitor for a parse tree
 * produced by JingleParser.
 */
class  JingleParserVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by JingleParser.
   */
    virtual antlrcpp::Any visitJingleFile(JingleParser::JingleFileContext *context) = 0;

    virtual antlrcpp::Any visitPackagePhrase(JingleParser::PackagePhraseContext *context) = 0;

    virtual antlrcpp::Any visitImportDecl(JingleParser::ImportDeclContext *context) = 0;

    virtual antlrcpp::Any visitImportSpec(JingleParser::ImportSpecContext *context) = 0;

    virtual antlrcpp::Any visitTopLevelDecl(JingleParser::TopLevelDeclContext *context) = 0;

    virtual antlrcpp::Any visitLine(JingleParser::LineContext *context) = 0;

    virtual antlrcpp::Any visitEndOfStatement(JingleParser::EndOfStatementContext *context) = 0;

    virtual antlrcpp::Any visitStatement(JingleParser::StatementContext *context) = 0;

    virtual antlrcpp::Any visitDeclaration(JingleParser::DeclarationContext *context) = 0;

    virtual antlrcpp::Any visitVarDecl(JingleParser::VarDeclContext *context) = 0;

    virtual antlrcpp::Any visitFuncDecl(JingleParser::FuncDeclContext *context) = 0;

    virtual antlrcpp::Any visitEchoDisplay(JingleParser::EchoDisplayContext *context) = 0;

    virtual antlrcpp::Any visitParams(JingleParser::ParamsContext *context) = 0;

    virtual antlrcpp::Any visitIdentifierList(JingleParser::IdentifierListContext *context) = 0;

    virtual antlrcpp::Any visitExpressionList(JingleParser::ExpressionListContext *context) = 0;

    virtual antlrcpp::Any visitParamList(JingleParser::ParamListContext *context) = 0;

    virtual antlrcpp::Any visitParamDecl(JingleParser::ParamDeclContext *context) = 0;

    virtual antlrcpp::Any visitIfStmt(JingleParser::IfStmtContext *context) = 0;

    virtual antlrcpp::Any visitForStmt(JingleParser::ForStmtContext *context) = 0;

    virtual antlrcpp::Any visitWhileStmt(JingleParser::WhileStmtContext *context) = 0;

    virtual antlrcpp::Any visitReturnStmt(JingleParser::ReturnStmtContext *context) = 0;

    virtual antlrcpp::Any visitSimpleStmt(JingleParser::SimpleStmtContext *context) = 0;

    virtual antlrcpp::Any visitIncDecStmt(JingleParser::IncDecStmtContext *context) = 0;

    virtual antlrcpp::Any visitAssign_op(JingleParser::Assign_opContext *context) = 0;

    virtual antlrcpp::Any visitShortVarDecl(JingleParser::ShortVarDeclContext *context) = 0;

    virtual antlrcpp::Any visitEmptyStmt(JingleParser::EmptyStmtContext *context) = 0;

    virtual antlrcpp::Any visitBlock(JingleParser::BlockContext *context) = 0;

    virtual antlrcpp::Any visitStatementList(JingleParser::StatementListContext *context) = 0;

    virtual antlrcpp::Any visitForClause(JingleParser::ForClauseContext *context) = 0;

    virtual antlrcpp::Any visitParenExpression(JingleParser::ParenExpressionContext *context) = 0;

    virtual antlrcpp::Any visitBinaryOperation(JingleParser::BinaryOperationContext *context) = 0;

    virtual antlrcpp::Any visitTypeConversion(JingleParser::TypeConversionContext *context) = 0;

    virtual antlrcpp::Any visitDataType(JingleParser::DataTypeContext *context) = 0;


};

}  // namespace Jingle
