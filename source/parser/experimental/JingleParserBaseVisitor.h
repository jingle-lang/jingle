
// Generated from JingleParser.g4 by ANTLR 4.7.2

#pragma once


#include "../cpp/antlr4-runtime/antlr4-runtime.h"
#include "JingleParserVisitor.h"


namespace Jingle {

/**
 * This class provides an empty implementation of JingleParserVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  JingleParserBaseVisitor : public JingleParserVisitor {
public:

  virtual antlrcpp::Any visitJingleFile(JingleParser::JingleFileContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitPackagePhrase(JingleParser::PackagePhraseContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitImportDecl(JingleParser::ImportDeclContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitImportSpec(JingleParser::ImportSpecContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitTopLevelDecl(JingleParser::TopLevelDeclContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitLine(JingleParser::LineContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitEndOfStatement(JingleParser::EndOfStatementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitStatement(JingleParser::StatementContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitDeclaration(JingleParser::DeclarationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitVarDecl(JingleParser::VarDeclContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitFuncDecl(JingleParser::FuncDeclContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitEchoDisplay(JingleParser::EchoDisplayContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitParams(JingleParser::ParamsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitIdentifierList(JingleParser::IdentifierListContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitExpressionList(JingleParser::ExpressionListContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitParamList(JingleParser::ParamListContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitParamDecl(JingleParser::ParamDeclContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitIfStmt(JingleParser::IfStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitForStmt(JingleParser::ForStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitWhileStmt(JingleParser::WhileStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitReturnStmt(JingleParser::ReturnStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitSimpleStmt(JingleParser::SimpleStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitIncDecStmt(JingleParser::IncDecStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitAssign_op(JingleParser::Assign_opContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitShortVarDecl(JingleParser::ShortVarDeclContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitEmptyStmt(JingleParser::EmptyStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitBlock(JingleParser::BlockContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitStatementList(JingleParser::StatementListContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitForClause(JingleParser::ForClauseContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitParenExpression(JingleParser::ParenExpressionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitBinaryOperation(JingleParser::BinaryOperationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitTypeConversion(JingleParser::TypeConversionContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual antlrcpp::Any visitDataType(JingleParser::DataTypeContext *ctx) override {
    return visitChildren(ctx);
  }


};

}  // namespace Jingle
