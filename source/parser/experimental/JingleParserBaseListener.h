
// Generated from JingleParser.g4 by ANTLR 4.7.2

#pragma once


#include "../cpp/antlr4-runtime/antlr4-runtime.h"
#include "JingleParserListener.h"


namespace Jingle {

/**
 * This class provides an empty implementation of JingleParserListener,
 * which can be extended to create a listener which only needs to handle a subset
 * of the available methods.
 */
class  JingleParserBaseListener : public JingleParserListener {
public:

  virtual void enterJingleFile(JingleParser::JingleFileContext * /*ctx*/) override { }
  virtual void exitJingleFile(JingleParser::JingleFileContext * /*ctx*/) override { }

  virtual void enterPackagePhrase(JingleParser::PackagePhraseContext * /*ctx*/) override { }
  virtual void exitPackagePhrase(JingleParser::PackagePhraseContext * /*ctx*/) override { }

  virtual void enterImportDecl(JingleParser::ImportDeclContext * /*ctx*/) override { }
  virtual void exitImportDecl(JingleParser::ImportDeclContext * /*ctx*/) override { }

  virtual void enterImportSpec(JingleParser::ImportSpecContext * /*ctx*/) override { }
  virtual void exitImportSpec(JingleParser::ImportSpecContext * /*ctx*/) override { }

  virtual void enterTopLevelDecl(JingleParser::TopLevelDeclContext * /*ctx*/) override { }
  virtual void exitTopLevelDecl(JingleParser::TopLevelDeclContext * /*ctx*/) override { }

  virtual void enterLine(JingleParser::LineContext * /*ctx*/) override { }
  virtual void exitLine(JingleParser::LineContext * /*ctx*/) override { }

  virtual void enterEndOfStatement(JingleParser::EndOfStatementContext * /*ctx*/) override { }
  virtual void exitEndOfStatement(JingleParser::EndOfStatementContext * /*ctx*/) override { }

  virtual void enterStatement(JingleParser::StatementContext * /*ctx*/) override { }
  virtual void exitStatement(JingleParser::StatementContext * /*ctx*/) override { }

  virtual void enterDeclaration(JingleParser::DeclarationContext * /*ctx*/) override { }
  virtual void exitDeclaration(JingleParser::DeclarationContext * /*ctx*/) override { }

  virtual void enterVarDecl(JingleParser::VarDeclContext * /*ctx*/) override { }
  virtual void exitVarDecl(JingleParser::VarDeclContext * /*ctx*/) override { }

  virtual void enterFuncDecl(JingleParser::FuncDeclContext * /*ctx*/) override { }
  virtual void exitFuncDecl(JingleParser::FuncDeclContext * /*ctx*/) override { }

  virtual void enterEchoDisplay(JingleParser::EchoDisplayContext * /*ctx*/) override { }
  virtual void exitEchoDisplay(JingleParser::EchoDisplayContext * /*ctx*/) override { }

  virtual void enterParams(JingleParser::ParamsContext * /*ctx*/) override { }
  virtual void exitParams(JingleParser::ParamsContext * /*ctx*/) override { }

  virtual void enterIdentifierList(JingleParser::IdentifierListContext * /*ctx*/) override { }
  virtual void exitIdentifierList(JingleParser::IdentifierListContext * /*ctx*/) override { }

  virtual void enterExpressionList(JingleParser::ExpressionListContext * /*ctx*/) override { }
  virtual void exitExpressionList(JingleParser::ExpressionListContext * /*ctx*/) override { }

  virtual void enterParamList(JingleParser::ParamListContext * /*ctx*/) override { }
  virtual void exitParamList(JingleParser::ParamListContext * /*ctx*/) override { }

  virtual void enterParamDecl(JingleParser::ParamDeclContext * /*ctx*/) override { }
  virtual void exitParamDecl(JingleParser::ParamDeclContext * /*ctx*/) override { }

  virtual void enterIfStmt(JingleParser::IfStmtContext * /*ctx*/) override { }
  virtual void exitIfStmt(JingleParser::IfStmtContext * /*ctx*/) override { }

  virtual void enterForStmt(JingleParser::ForStmtContext * /*ctx*/) override { }
  virtual void exitForStmt(JingleParser::ForStmtContext * /*ctx*/) override { }

  virtual void enterWhileStmt(JingleParser::WhileStmtContext * /*ctx*/) override { }
  virtual void exitWhileStmt(JingleParser::WhileStmtContext * /*ctx*/) override { }

  virtual void enterReturnStmt(JingleParser::ReturnStmtContext * /*ctx*/) override { }
  virtual void exitReturnStmt(JingleParser::ReturnStmtContext * /*ctx*/) override { }

  virtual void enterSimpleStmt(JingleParser::SimpleStmtContext * /*ctx*/) override { }
  virtual void exitSimpleStmt(JingleParser::SimpleStmtContext * /*ctx*/) override { }

  virtual void enterIncDecStmt(JingleParser::IncDecStmtContext * /*ctx*/) override { }
  virtual void exitIncDecStmt(JingleParser::IncDecStmtContext * /*ctx*/) override { }

  virtual void enterAssign_op(JingleParser::Assign_opContext * /*ctx*/) override { }
  virtual void exitAssign_op(JingleParser::Assign_opContext * /*ctx*/) override { }

  virtual void enterShortVarDecl(JingleParser::ShortVarDeclContext * /*ctx*/) override { }
  virtual void exitShortVarDecl(JingleParser::ShortVarDeclContext * /*ctx*/) override { }

  virtual void enterEmptyStmt(JingleParser::EmptyStmtContext * /*ctx*/) override { }
  virtual void exitEmptyStmt(JingleParser::EmptyStmtContext * /*ctx*/) override { }

  virtual void enterBlock(JingleParser::BlockContext * /*ctx*/) override { }
  virtual void exitBlock(JingleParser::BlockContext * /*ctx*/) override { }

  virtual void enterStatementList(JingleParser::StatementListContext * /*ctx*/) override { }
  virtual void exitStatementList(JingleParser::StatementListContext * /*ctx*/) override { }

  virtual void enterForClause(JingleParser::ForClauseContext * /*ctx*/) override { }
  virtual void exitForClause(JingleParser::ForClauseContext * /*ctx*/) override { }

  virtual void enterParenExpression(JingleParser::ParenExpressionContext * /*ctx*/) override { }
  virtual void exitParenExpression(JingleParser::ParenExpressionContext * /*ctx*/) override { }

  virtual void enterBinaryOperation(JingleParser::BinaryOperationContext * /*ctx*/) override { }
  virtual void exitBinaryOperation(JingleParser::BinaryOperationContext * /*ctx*/) override { }

  virtual void enterTypeConversion(JingleParser::TypeConversionContext * /*ctx*/) override { }
  virtual void exitTypeConversion(JingleParser::TypeConversionContext * /*ctx*/) override { }

  virtual void enterDataType(JingleParser::DataTypeContext * /*ctx*/) override { }
  virtual void exitDataType(JingleParser::DataTypeContext * /*ctx*/) override { }


  virtual void enterEveryRule(antlr4::ParserRuleContext * /*ctx*/) override { }
  virtual void exitEveryRule(antlr4::ParserRuleContext * /*ctx*/) override { }
  virtual void visitTerminal(antlr4::tree::TerminalNode * /*node*/) override { }
  virtual void visitErrorNode(antlr4::tree::ErrorNode * /*node*/) override { }

};

}  // namespace Jingle
