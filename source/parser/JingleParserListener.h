
// Generated from JingleParser.g4 by ANTLR 4.7.2

#pragma once


#include "../cpp/antlr4-runtime/antlr4-runtime.h"
#include "JingleParser.h"


namespace Jingle {

/**
 * This interface defines an abstract listener for a parse tree produced by JingleParser.
 */
class  JingleParserListener : public antlr4::tree::ParseTreeListener {
public:

  virtual void enterJingleFile(JingleParser::JingleFileContext *ctx) = 0;
  virtual void exitJingleFile(JingleParser::JingleFileContext *ctx) = 0;

  virtual void enterPackagePhrase(JingleParser::PackagePhraseContext *ctx) = 0;
  virtual void exitPackagePhrase(JingleParser::PackagePhraseContext *ctx) = 0;

  virtual void enterImportDecl(JingleParser::ImportDeclContext *ctx) = 0;
  virtual void exitImportDecl(JingleParser::ImportDeclContext *ctx) = 0;

  virtual void enterImportSpec(JingleParser::ImportSpecContext *ctx) = 0;
  virtual void exitImportSpec(JingleParser::ImportSpecContext *ctx) = 0;

  virtual void enterTopLevelDecl(JingleParser::TopLevelDeclContext *ctx) = 0;
  virtual void exitTopLevelDecl(JingleParser::TopLevelDeclContext *ctx) = 0;

  virtual void enterLine(JingleParser::LineContext *ctx) = 0;
  virtual void exitLine(JingleParser::LineContext *ctx) = 0;

  virtual void enterEndOfStatement(JingleParser::EndOfStatementContext *ctx) = 0;
  virtual void exitEndOfStatement(JingleParser::EndOfStatementContext *ctx) = 0;

  virtual void enterStatement(JingleParser::StatementContext *ctx) = 0;
  virtual void exitStatement(JingleParser::StatementContext *ctx) = 0;

  virtual void enterDeclaration(JingleParser::DeclarationContext *ctx) = 0;
  virtual void exitDeclaration(JingleParser::DeclarationContext *ctx) = 0;

  virtual void enterVarDecl(JingleParser::VarDeclContext *ctx) = 0;
  virtual void exitVarDecl(JingleParser::VarDeclContext *ctx) = 0;

  virtual void enterFuncDecl(JingleParser::FuncDeclContext *ctx) = 0;
  virtual void exitFuncDecl(JingleParser::FuncDeclContext *ctx) = 0;

  virtual void enterEchoDisplay(JingleParser::EchoDisplayContext *ctx) = 0;
  virtual void exitEchoDisplay(JingleParser::EchoDisplayContext *ctx) = 0;

  virtual void enterParams(JingleParser::ParamsContext *ctx) = 0;
  virtual void exitParams(JingleParser::ParamsContext *ctx) = 0;

  virtual void enterIdentifierList(JingleParser::IdentifierListContext *ctx) = 0;
  virtual void exitIdentifierList(JingleParser::IdentifierListContext *ctx) = 0;

  virtual void enterExpressionList(JingleParser::ExpressionListContext *ctx) = 0;
  virtual void exitExpressionList(JingleParser::ExpressionListContext *ctx) = 0;

  virtual void enterParamList(JingleParser::ParamListContext *ctx) = 0;
  virtual void exitParamList(JingleParser::ParamListContext *ctx) = 0;

  virtual void enterParamDecl(JingleParser::ParamDeclContext *ctx) = 0;
  virtual void exitParamDecl(JingleParser::ParamDeclContext *ctx) = 0;

  virtual void enterIfStmt(JingleParser::IfStmtContext *ctx) = 0;
  virtual void exitIfStmt(JingleParser::IfStmtContext *ctx) = 0;

  virtual void enterForStmt(JingleParser::ForStmtContext *ctx) = 0;
  virtual void exitForStmt(JingleParser::ForStmtContext *ctx) = 0;

  virtual void enterWhileStmt(JingleParser::WhileStmtContext *ctx) = 0;
  virtual void exitWhileStmt(JingleParser::WhileStmtContext *ctx) = 0;

  virtual void enterReturnStmt(JingleParser::ReturnStmtContext *ctx) = 0;
  virtual void exitReturnStmt(JingleParser::ReturnStmtContext *ctx) = 0;

  virtual void enterSimpleStmt(JingleParser::SimpleStmtContext *ctx) = 0;
  virtual void exitSimpleStmt(JingleParser::SimpleStmtContext *ctx) = 0;

  virtual void enterIncDecStmt(JingleParser::IncDecStmtContext *ctx) = 0;
  virtual void exitIncDecStmt(JingleParser::IncDecStmtContext *ctx) = 0;

  virtual void enterAssign_op(JingleParser::Assign_opContext *ctx) = 0;
  virtual void exitAssign_op(JingleParser::Assign_opContext *ctx) = 0;

  virtual void enterShortVarDecl(JingleParser::ShortVarDeclContext *ctx) = 0;
  virtual void exitShortVarDecl(JingleParser::ShortVarDeclContext *ctx) = 0;

  virtual void enterEmptyStmt(JingleParser::EmptyStmtContext *ctx) = 0;
  virtual void exitEmptyStmt(JingleParser::EmptyStmtContext *ctx) = 0;

  virtual void enterBlock(JingleParser::BlockContext *ctx) = 0;
  virtual void exitBlock(JingleParser::BlockContext *ctx) = 0;

  virtual void enterStatementList(JingleParser::StatementListContext *ctx) = 0;
  virtual void exitStatementList(JingleParser::StatementListContext *ctx) = 0;

  virtual void enterForClause(JingleParser::ForClauseContext *ctx) = 0;
  virtual void exitForClause(JingleParser::ForClauseContext *ctx) = 0;

  virtual void enterParenExpression(JingleParser::ParenExpressionContext *ctx) = 0;
  virtual void exitParenExpression(JingleParser::ParenExpressionContext *ctx) = 0;

  virtual void enterBinaryOperation(JingleParser::BinaryOperationContext *ctx) = 0;
  virtual void exitBinaryOperation(JingleParser::BinaryOperationContext *ctx) = 0;

  virtual void enterTypeConversion(JingleParser::TypeConversionContext *ctx) = 0;
  virtual void exitTypeConversion(JingleParser::TypeConversionContext *ctx) = 0;

  virtual void enterDataType(JingleParser::DataTypeContext *ctx) = 0;
  virtual void exitDataType(JingleParser::DataTypeContext *ctx) = 0;


};

}  // namespace Jingle
