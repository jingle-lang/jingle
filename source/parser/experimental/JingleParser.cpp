
// Generated from JingleParser.g4 by ANTLR 4.7.2


#include "JingleParserListener.h"
#include "JingleParserVisitor.h"

#include "JingleParser.h"


using namespace antlrcpp;
using namespace Jingle;
using namespace antlr4;

JingleParser::JingleParser(TokenStream *input) : Parser(input) {
  _interpreter = new atn::ParserATNSimulator(this, _atn, _decisionToDFA, _sharedContextCache);
}

JingleParser::~JingleParser() {
  delete _interpreter;
}

std::string JingleParser::getGrammarFileName() const {
  return "JingleParser.g4";
}

const std::vector<std::string>& JingleParser::getRuleNames() const {
  return _ruleNames;
}

dfa::Vocabulary& JingleParser::getVocabulary() const {
  return _vocabulary;
}


//----------------- JingleFileContext ------------------------------------------------------------------

JingleParser::JingleFileContext::JingleFileContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::PackagePhraseContext* JingleParser::JingleFileContext::packagePhrase() {
  return getRuleContext<JingleParser::PackagePhraseContext>(0);
}

std::vector<JingleParser::EndOfStatementContext *> JingleParser::JingleFileContext::endOfStatement() {
  return getRuleContexts<JingleParser::EndOfStatementContext>();
}

JingleParser::EndOfStatementContext* JingleParser::JingleFileContext::endOfStatement(size_t i) {
  return getRuleContext<JingleParser::EndOfStatementContext>(i);
}

std::vector<JingleParser::ImportDeclContext *> JingleParser::JingleFileContext::importDecl() {
  return getRuleContexts<JingleParser::ImportDeclContext>();
}

JingleParser::ImportDeclContext* JingleParser::JingleFileContext::importDecl(size_t i) {
  return getRuleContext<JingleParser::ImportDeclContext>(i);
}

std::vector<JingleParser::TopLevelDeclContext *> JingleParser::JingleFileContext::topLevelDecl() {
  return getRuleContexts<JingleParser::TopLevelDeclContext>();
}

JingleParser::TopLevelDeclContext* JingleParser::JingleFileContext::topLevelDecl(size_t i) {
  return getRuleContext<JingleParser::TopLevelDeclContext>(i);
}


size_t JingleParser::JingleFileContext::getRuleIndex() const {
  return JingleParser::RuleJingleFile;
}

void JingleParser::JingleFileContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterJingleFile(this);
}

void JingleParser::JingleFileContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitJingleFile(this);
}


antlrcpp::Any JingleParser::JingleFileContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitJingleFile(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::JingleFileContext* JingleParser::jingleFile() {
  JingleFileContext *_localctx = _tracker.createInstance<JingleFileContext>(_ctx, getState());
  enterRule(_localctx, 0, JingleParser::RuleJingleFile);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(62);
    packagePhrase();
    setState(63);
    endOfStatement();
    setState(69);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == JingleParser::IMPORT) {
      setState(64);
      importDecl();
      setState(65);
      endOfStatement();
      setState(71);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(77);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(72);
        topLevelDecl();
        setState(73);
        endOfStatement(); 
      }
      setState(79);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 1, _ctx);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- PackagePhraseContext ------------------------------------------------------------------

JingleParser::PackagePhraseContext::PackagePhraseContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::PackagePhraseContext::PACKAGE() {
  return getToken(JingleParser::PACKAGE, 0);
}

tree::TerminalNode* JingleParser::PackagePhraseContext::NOUNICODEID() {
  return getToken(JingleParser::NOUNICODEID, 0);
}


size_t JingleParser::PackagePhraseContext::getRuleIndex() const {
  return JingleParser::RulePackagePhrase;
}

void JingleParser::PackagePhraseContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterPackagePhrase(this);
}

void JingleParser::PackagePhraseContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitPackagePhrase(this);
}


antlrcpp::Any JingleParser::PackagePhraseContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitPackagePhrase(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::PackagePhraseContext* JingleParser::packagePhrase() {
  PackagePhraseContext *_localctx = _tracker.createInstance<PackagePhraseContext>(_ctx, getState());
  enterRule(_localctx, 2, JingleParser::RulePackagePhrase);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(80);
    match(JingleParser::PACKAGE);
    setState(81);
    match(JingleParser::NOUNICODEID);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ImportDeclContext ------------------------------------------------------------------

JingleParser::ImportDeclContext::ImportDeclContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::ImportDeclContext::IMPORT() {
  return getToken(JingleParser::IMPORT, 0);
}

std::vector<JingleParser::ImportSpecContext *> JingleParser::ImportDeclContext::importSpec() {
  return getRuleContexts<JingleParser::ImportSpecContext>();
}

JingleParser::ImportSpecContext* JingleParser::ImportDeclContext::importSpec(size_t i) {
  return getRuleContext<JingleParser::ImportSpecContext>(i);
}

tree::TerminalNode* JingleParser::ImportDeclContext::LBRACKET() {
  return getToken(JingleParser::LBRACKET, 0);
}

tree::TerminalNode* JingleParser::ImportDeclContext::RBRACKET() {
  return getToken(JingleParser::RBRACKET, 0);
}

std::vector<JingleParser::EndOfStatementContext *> JingleParser::ImportDeclContext::endOfStatement() {
  return getRuleContexts<JingleParser::EndOfStatementContext>();
}

JingleParser::EndOfStatementContext* JingleParser::ImportDeclContext::endOfStatement(size_t i) {
  return getRuleContext<JingleParser::EndOfStatementContext>(i);
}


size_t JingleParser::ImportDeclContext::getRuleIndex() const {
  return JingleParser::RuleImportDecl;
}

void JingleParser::ImportDeclContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterImportDecl(this);
}

void JingleParser::ImportDeclContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitImportDecl(this);
}


antlrcpp::Any JingleParser::ImportDeclContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitImportDecl(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ImportDeclContext* JingleParser::importDecl() {
  ImportDeclContext *_localctx = _tracker.createInstance<ImportDeclContext>(_ctx, getState());
  enterRule(_localctx, 4, JingleParser::RuleImportDecl);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(83);
    match(JingleParser::IMPORT);
    setState(95);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case JingleParser::STRING_LIT: {
        setState(84);
        importSpec();
        break;
      }

      case JingleParser::LBRACKET: {
        setState(85);
        match(JingleParser::LBRACKET);
        setState(91);
        _errHandler->sync(this);
        _la = _input->LA(1);
        while (_la == JingleParser::STRING_LIT) {
          setState(86);
          importSpec();
          setState(87);
          endOfStatement();
          setState(93);
          _errHandler->sync(this);
          _la = _input->LA(1);
        }
        setState(94);
        match(JingleParser::RBRACKET);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ImportSpecContext ------------------------------------------------------------------

JingleParser::ImportSpecContext::ImportSpecContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::ImportSpecContext::STRING_LIT() {
  return getToken(JingleParser::STRING_LIT, 0);
}


size_t JingleParser::ImportSpecContext::getRuleIndex() const {
  return JingleParser::RuleImportSpec;
}

void JingleParser::ImportSpecContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterImportSpec(this);
}

void JingleParser::ImportSpecContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitImportSpec(this);
}


antlrcpp::Any JingleParser::ImportSpecContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitImportSpec(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ImportSpecContext* JingleParser::importSpec() {
  ImportSpecContext *_localctx = _tracker.createInstance<ImportSpecContext>(_ctx, getState());
  enterRule(_localctx, 6, JingleParser::RuleImportSpec);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(97);
    match(JingleParser::STRING_LIT);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TopLevelDeclContext ------------------------------------------------------------------

JingleParser::TopLevelDeclContext::TopLevelDeclContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::StatementContext* JingleParser::TopLevelDeclContext::statement() {
  return getRuleContext<JingleParser::StatementContext>(0);
}

JingleParser::FuncDeclContext* JingleParser::TopLevelDeclContext::funcDecl() {
  return getRuleContext<JingleParser::FuncDeclContext>(0);
}


size_t JingleParser::TopLevelDeclContext::getRuleIndex() const {
  return JingleParser::RuleTopLevelDecl;
}

void JingleParser::TopLevelDeclContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterTopLevelDecl(this);
}

void JingleParser::TopLevelDeclContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitTopLevelDecl(this);
}


antlrcpp::Any JingleParser::TopLevelDeclContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitTopLevelDecl(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::TopLevelDeclContext* JingleParser::topLevelDecl() {
  TopLevelDeclContext *_localctx = _tracker.createInstance<TopLevelDeclContext>(_ctx, getState());
  enterRule(_localctx, 8, JingleParser::RuleTopLevelDecl);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(101);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 4, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(99);
      statement();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(100);
      funcDecl();
      break;
    }

    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LineContext ------------------------------------------------------------------

JingleParser::LineContext::LineContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::StatementContext* JingleParser::LineContext::statement() {
  return getRuleContext<JingleParser::StatementContext>(0);
}

tree::TerminalNode* JingleParser::LineContext::ENDSTATEMENT() {
  return getToken(JingleParser::ENDSTATEMENT, 0);
}

tree::TerminalNode* JingleParser::LineContext::EOF() {
  return getToken(JingleParser::EOF, 0);
}


size_t JingleParser::LineContext::getRuleIndex() const {
  return JingleParser::RuleLine;
}

void JingleParser::LineContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterLine(this);
}

void JingleParser::LineContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitLine(this);
}


antlrcpp::Any JingleParser::LineContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitLine(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::LineContext* JingleParser::line() {
  LineContext *_localctx = _tracker.createInstance<LineContext>(_ctx, getState());
  enterRule(_localctx, 10, JingleParser::RuleLine);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(103);
    statement();
    setState(104);
    _la = _input->LA(1);
    if (!(_la == JingleParser::EOF

    || _la == JingleParser::ENDSTATEMENT)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- EndOfStatementContext ------------------------------------------------------------------

JingleParser::EndOfStatementContext::EndOfStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::EndOfStatementContext::ENDSTATEMENT() {
  return getToken(JingleParser::ENDSTATEMENT, 0);
}

tree::TerminalNode* JingleParser::EndOfStatementContext::EOF() {
  return getToken(JingleParser::EOF, 0);
}


size_t JingleParser::EndOfStatementContext::getRuleIndex() const {
  return JingleParser::RuleEndOfStatement;
}

void JingleParser::EndOfStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterEndOfStatement(this);
}

void JingleParser::EndOfStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitEndOfStatement(this);
}


antlrcpp::Any JingleParser::EndOfStatementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitEndOfStatement(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::EndOfStatementContext* JingleParser::endOfStatement() {
  EndOfStatementContext *_localctx = _tracker.createInstance<EndOfStatementContext>(_ctx, getState());
  enterRule(_localctx, 12, JingleParser::RuleEndOfStatement);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(106);
    _la = _input->LA(1);
    if (!(_la == JingleParser::EOF

    || _la == JingleParser::ENDSTATEMENT)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StatementContext ------------------------------------------------------------------

JingleParser::StatementContext::StatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::DeclarationContext* JingleParser::StatementContext::declaration() {
  return getRuleContext<JingleParser::DeclarationContext>(0);
}

JingleParser::IfStmtContext* JingleParser::StatementContext::ifStmt() {
  return getRuleContext<JingleParser::IfStmtContext>(0);
}

JingleParser::ForStmtContext* JingleParser::StatementContext::forStmt() {
  return getRuleContext<JingleParser::ForStmtContext>(0);
}

JingleParser::ReturnStmtContext* JingleParser::StatementContext::returnStmt() {
  return getRuleContext<JingleParser::ReturnStmtContext>(0);
}

JingleParser::SimpleStmtContext* JingleParser::StatementContext::simpleStmt() {
  return getRuleContext<JingleParser::SimpleStmtContext>(0);
}

JingleParser::BlockContext* JingleParser::StatementContext::block() {
  return getRuleContext<JingleParser::BlockContext>(0);
}

JingleParser::EchoDisplayContext* JingleParser::StatementContext::echoDisplay() {
  return getRuleContext<JingleParser::EchoDisplayContext>(0);
}


size_t JingleParser::StatementContext::getRuleIndex() const {
  return JingleParser::RuleStatement;
}

void JingleParser::StatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterStatement(this);
}

void JingleParser::StatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitStatement(this);
}


antlrcpp::Any JingleParser::StatementContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitStatement(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::StatementContext* JingleParser::statement() {
  StatementContext *_localctx = _tracker.createInstance<StatementContext>(_ctx, getState());
  enterRule(_localctx, 14, JingleParser::RuleStatement);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(116);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 5, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);

      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(109);
      declaration();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(110);
      ifStmt();
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(111);
      forStmt();
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(112);
      returnStmt();
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(113);
      simpleStmt();
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(114);
      block();
      break;
    }

    case 8: {
      enterOuterAlt(_localctx, 8);
      setState(115);
      echoDisplay();
      break;
    }

    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DeclarationContext ------------------------------------------------------------------

JingleParser::DeclarationContext::DeclarationContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::VarDeclContext* JingleParser::DeclarationContext::varDecl() {
  return getRuleContext<JingleParser::VarDeclContext>(0);
}

JingleParser::FuncDeclContext* JingleParser::DeclarationContext::funcDecl() {
  return getRuleContext<JingleParser::FuncDeclContext>(0);
}


size_t JingleParser::DeclarationContext::getRuleIndex() const {
  return JingleParser::RuleDeclaration;
}

void JingleParser::DeclarationContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterDeclaration(this);
}

void JingleParser::DeclarationContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitDeclaration(this);
}


antlrcpp::Any JingleParser::DeclarationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitDeclaration(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::DeclarationContext* JingleParser::declaration() {
  DeclarationContext *_localctx = _tracker.createInstance<DeclarationContext>(_ctx, getState());
  enterRule(_localctx, 16, JingleParser::RuleDeclaration);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(121);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case JingleParser::EOF:
      case JingleParser::ENDSTATEMENT: {
        enterOuterAlt(_localctx, 1);

        break;
      }

      case JingleParser::VAR: {
        enterOuterAlt(_localctx, 2);
        setState(119);
        varDecl();
        break;
      }

      case JingleParser::FUNCTION: {
        enterOuterAlt(_localctx, 3);
        setState(120);
        funcDecl();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- VarDeclContext ------------------------------------------------------------------

JingleParser::VarDeclContext::VarDeclContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::VarDeclContext::VAR() {
  return getToken(JingleParser::VAR, 0);
}

std::vector<tree::TerminalNode *> JingleParser::VarDeclContext::NOUNICODEID() {
  return getTokens(JingleParser::NOUNICODEID);
}

tree::TerminalNode* JingleParser::VarDeclContext::NOUNICODEID(size_t i) {
  return getToken(JingleParser::NOUNICODEID, i);
}

tree::TerminalNode* JingleParser::VarDeclContext::WHITESPACE() {
  return getToken(JingleParser::WHITESPACE, 0);
}

tree::TerminalNode* JingleParser::VarDeclContext::EQUALS() {
  return getToken(JingleParser::EQUALS, 0);
}

tree::TerminalNode* JingleParser::VarDeclContext::INT_LITERAL() {
  return getToken(JingleParser::INT_LITERAL, 0);
}


size_t JingleParser::VarDeclContext::getRuleIndex() const {
  return JingleParser::RuleVarDecl;
}

void JingleParser::VarDeclContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterVarDecl(this);
}

void JingleParser::VarDeclContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitVarDecl(this);
}


antlrcpp::Any JingleParser::VarDeclContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitVarDecl(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::VarDeclContext* JingleParser::varDecl() {
  VarDeclContext *_localctx = _tracker.createInstance<VarDeclContext>(_ctx, getState());
  enterRule(_localctx, 18, JingleParser::RuleVarDecl);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(123);
    match(JingleParser::VAR);
    setState(124);
    match(JingleParser::NOUNICODEID);
    setState(125);
    match(JingleParser::WHITESPACE);
    setState(126);
    match(JingleParser::EQUALS);
    setState(127);
    _la = _input->LA(1);
    if (!(_la == JingleParser::INT_LITERAL

    || _la == JingleParser::NOUNICODEID)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FuncDeclContext ------------------------------------------------------------------

JingleParser::FuncDeclContext::FuncDeclContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::FuncDeclContext::FUNCTION() {
  return getToken(JingleParser::FUNCTION, 0);
}

std::vector<tree::TerminalNode *> JingleParser::FuncDeclContext::WHITESPACE() {
  return getTokens(JingleParser::WHITESPACE);
}

tree::TerminalNode* JingleParser::FuncDeclContext::WHITESPACE(size_t i) {
  return getToken(JingleParser::WHITESPACE, i);
}

tree::TerminalNode* JingleParser::FuncDeclContext::NOUNICODEID() {
  return getToken(JingleParser::NOUNICODEID, 0);
}

tree::TerminalNode* JingleParser::FuncDeclContext::LBRACKET() {
  return getToken(JingleParser::LBRACKET, 0);
}

JingleParser::ParamsContext* JingleParser::FuncDeclContext::params() {
  return getRuleContext<JingleParser::ParamsContext>(0);
}

tree::TerminalNode* JingleParser::FuncDeclContext::RBRACKET() {
  return getToken(JingleParser::RBRACKET, 0);
}

tree::TerminalNode* JingleParser::FuncDeclContext::COLON() {
  return getToken(JingleParser::COLON, 0);
}


size_t JingleParser::FuncDeclContext::getRuleIndex() const {
  return JingleParser::RuleFuncDecl;
}

void JingleParser::FuncDeclContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterFuncDecl(this);
}

void JingleParser::FuncDeclContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitFuncDecl(this);
}


antlrcpp::Any JingleParser::FuncDeclContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitFuncDecl(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::FuncDeclContext* JingleParser::funcDecl() {
  FuncDeclContext *_localctx = _tracker.createInstance<FuncDeclContext>(_ctx, getState());
  enterRule(_localctx, 20, JingleParser::RuleFuncDecl);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(129);
    match(JingleParser::FUNCTION);
    setState(130);
    match(JingleParser::WHITESPACE);
    setState(131);
    match(JingleParser::NOUNICODEID);
    setState(132);
    match(JingleParser::WHITESPACE);
    setState(133);
    match(JingleParser::LBRACKET);
    setState(134);
    params();
    setState(135);
    match(JingleParser::RBRACKET);
    setState(136);
    match(JingleParser::WHITESPACE);
    setState(137);
    match(JingleParser::COLON);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- EchoDisplayContext ------------------------------------------------------------------

JingleParser::EchoDisplayContext::EchoDisplayContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::EchoDisplayContext::ECHO() {
  return getToken(JingleParser::ECHO, 0);
}

tree::TerminalNode* JingleParser::EchoDisplayContext::WHITESPACE() {
  return getToken(JingleParser::WHITESPACE, 0);
}

tree::TerminalNode* JingleParser::EchoDisplayContext::LBRACKET() {
  return getToken(JingleParser::LBRACKET, 0);
}

tree::TerminalNode* JingleParser::EchoDisplayContext::RBRACKET() {
  return getToken(JingleParser::RBRACKET, 0);
}

tree::TerminalNode* JingleParser::EchoDisplayContext::INT_LITERAL() {
  return getToken(JingleParser::INT_LITERAL, 0);
}

tree::TerminalNode* JingleParser::EchoDisplayContext::NOUNICODEID() {
  return getToken(JingleParser::NOUNICODEID, 0);
}


size_t JingleParser::EchoDisplayContext::getRuleIndex() const {
  return JingleParser::RuleEchoDisplay;
}

void JingleParser::EchoDisplayContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterEchoDisplay(this);
}

void JingleParser::EchoDisplayContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitEchoDisplay(this);
}


antlrcpp::Any JingleParser::EchoDisplayContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitEchoDisplay(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::EchoDisplayContext* JingleParser::echoDisplay() {
  EchoDisplayContext *_localctx = _tracker.createInstance<EchoDisplayContext>(_ctx, getState());
  enterRule(_localctx, 22, JingleParser::RuleEchoDisplay);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(139);
    match(JingleParser::ECHO);
    setState(140);
    match(JingleParser::WHITESPACE);
    setState(141);
    match(JingleParser::LBRACKET);
    setState(142);
    _la = _input->LA(1);
    if (!(_la == JingleParser::INT_LITERAL

    || _la == JingleParser::NOUNICODEID)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
    setState(143);
    match(JingleParser::RBRACKET);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ParamsContext ------------------------------------------------------------------

JingleParser::ParamsContext::ParamsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::ParamsContext::LBRACKET() {
  return getToken(JingleParser::LBRACKET, 0);
}

tree::TerminalNode* JingleParser::ParamsContext::RBRACKET() {
  return getToken(JingleParser::RBRACKET, 0);
}

JingleParser::ParamListContext* JingleParser::ParamsContext::paramList() {
  return getRuleContext<JingleParser::ParamListContext>(0);
}

tree::TerminalNode* JingleParser::ParamsContext::COMMA() {
  return getToken(JingleParser::COMMA, 0);
}


size_t JingleParser::ParamsContext::getRuleIndex() const {
  return JingleParser::RuleParams;
}

void JingleParser::ParamsContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterParams(this);
}

void JingleParser::ParamsContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitParams(this);
}


antlrcpp::Any JingleParser::ParamsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitParams(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ParamsContext* JingleParser::params() {
  ParamsContext *_localctx = _tracker.createInstance<ParamsContext>(_ctx, getState());
  enterRule(_localctx, 24, JingleParser::RuleParams);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(145);
    match(JingleParser::LBRACKET);
    setState(150);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 8, _ctx)) {
    case 1: {
      setState(146);
      paramList();
      setState(148);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == JingleParser::COMMA) {
        setState(147);
        match(JingleParser::COMMA);
      }
      break;
    }

    }
    setState(152);
    match(JingleParser::RBRACKET);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- IdentifierListContext ------------------------------------------------------------------

JingleParser::IdentifierListContext::IdentifierListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> JingleParser::IdentifierListContext::NOUNICODEID() {
  return getTokens(JingleParser::NOUNICODEID);
}

tree::TerminalNode* JingleParser::IdentifierListContext::NOUNICODEID(size_t i) {
  return getToken(JingleParser::NOUNICODEID, i);
}

std::vector<tree::TerminalNode *> JingleParser::IdentifierListContext::COMMA() {
  return getTokens(JingleParser::COMMA);
}

tree::TerminalNode* JingleParser::IdentifierListContext::COMMA(size_t i) {
  return getToken(JingleParser::COMMA, i);
}


size_t JingleParser::IdentifierListContext::getRuleIndex() const {
  return JingleParser::RuleIdentifierList;
}

void JingleParser::IdentifierListContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterIdentifierList(this);
}

void JingleParser::IdentifierListContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitIdentifierList(this);
}


antlrcpp::Any JingleParser::IdentifierListContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitIdentifierList(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::IdentifierListContext* JingleParser::identifierList() {
  IdentifierListContext *_localctx = _tracker.createInstance<IdentifierListContext>(_ctx, getState());
  enterRule(_localctx, 26, JingleParser::RuleIdentifierList);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(154);
    match(JingleParser::NOUNICODEID);
    setState(159);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(155);
        match(JingleParser::COMMA);
        setState(156);
        match(JingleParser::NOUNICODEID); 
      }
      setState(161);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 9, _ctx);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ExpressionListContext ------------------------------------------------------------------

JingleParser::ExpressionListContext::ExpressionListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::ExpressionContext* JingleParser::ExpressionListContext::expression() {
  return getRuleContext<JingleParser::ExpressionContext>(0);
}

std::vector<tree::TerminalNode *> JingleParser::ExpressionListContext::COMMA() {
  return getTokens(JingleParser::COMMA);
}

tree::TerminalNode* JingleParser::ExpressionListContext::COMMA(size_t i) {
  return getToken(JingleParser::COMMA, i);
}

std::vector<tree::TerminalNode *> JingleParser::ExpressionListContext::NOUNICODEID() {
  return getTokens(JingleParser::NOUNICODEID);
}

tree::TerminalNode* JingleParser::ExpressionListContext::NOUNICODEID(size_t i) {
  return getToken(JingleParser::NOUNICODEID, i);
}


size_t JingleParser::ExpressionListContext::getRuleIndex() const {
  return JingleParser::RuleExpressionList;
}

void JingleParser::ExpressionListContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterExpressionList(this);
}

void JingleParser::ExpressionListContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitExpressionList(this);
}


antlrcpp::Any JingleParser::ExpressionListContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitExpressionList(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ExpressionListContext* JingleParser::expressionList() {
  ExpressionListContext *_localctx = _tracker.createInstance<ExpressionListContext>(_ctx, getState());
  enterRule(_localctx, 28, JingleParser::RuleExpressionList);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(162);
    expression(0);
    setState(167);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == JingleParser::COMMA) {
      setState(163);
      match(JingleParser::COMMA);
      setState(164);
      match(JingleParser::NOUNICODEID);
      setState(169);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ParamListContext ------------------------------------------------------------------

JingleParser::ParamListContext::ParamListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<JingleParser::ParamDeclContext *> JingleParser::ParamListContext::paramDecl() {
  return getRuleContexts<JingleParser::ParamDeclContext>();
}

JingleParser::ParamDeclContext* JingleParser::ParamListContext::paramDecl(size_t i) {
  return getRuleContext<JingleParser::ParamDeclContext>(i);
}

std::vector<tree::TerminalNode *> JingleParser::ParamListContext::COMMA() {
  return getTokens(JingleParser::COMMA);
}

tree::TerminalNode* JingleParser::ParamListContext::COMMA(size_t i) {
  return getToken(JingleParser::COMMA, i);
}


size_t JingleParser::ParamListContext::getRuleIndex() const {
  return JingleParser::RuleParamList;
}

void JingleParser::ParamListContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterParamList(this);
}

void JingleParser::ParamListContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitParamList(this);
}


antlrcpp::Any JingleParser::ParamListContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitParamList(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ParamListContext* JingleParser::paramList() {
  ParamListContext *_localctx = _tracker.createInstance<ParamListContext>(_ctx, getState());
  enterRule(_localctx, 30, JingleParser::RuleParamList);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(170);
    paramDecl();
    setState(175);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(171);
        match(JingleParser::COMMA);
        setState(172);
        paramDecl(); 
      }
      setState(177);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 11, _ctx);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ParamDeclContext ------------------------------------------------------------------

JingleParser::ParamDeclContext::ParamDeclContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::IdentifierListContext* JingleParser::ParamDeclContext::identifierList() {
  return getRuleContext<JingleParser::IdentifierListContext>(0);
}

tree::TerminalNode* JingleParser::ParamDeclContext::ELLIPSIS() {
  return getToken(JingleParser::ELLIPSIS, 0);
}


size_t JingleParser::ParamDeclContext::getRuleIndex() const {
  return JingleParser::RuleParamDecl;
}

void JingleParser::ParamDeclContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterParamDecl(this);
}

void JingleParser::ParamDeclContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitParamDecl(this);
}


antlrcpp::Any JingleParser::ParamDeclContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitParamDecl(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ParamDeclContext* JingleParser::paramDecl() {
  ParamDeclContext *_localctx = _tracker.createInstance<ParamDeclContext>(_ctx, getState());
  enterRule(_localctx, 32, JingleParser::RuleParamDecl);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(179);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == JingleParser::NOUNICODEID) {
      setState(178);
      identifierList();
    }
    setState(182);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == JingleParser::ELLIPSIS) {
      setState(181);
      match(JingleParser::ELLIPSIS);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- IfStmtContext ------------------------------------------------------------------

JingleParser::IfStmtContext::IfStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::IfStmtContext::IF() {
  return getToken(JingleParser::IF, 0);
}

JingleParser::ExpressionContext* JingleParser::IfStmtContext::expression() {
  return getRuleContext<JingleParser::ExpressionContext>(0);
}

std::vector<JingleParser::BlockContext *> JingleParser::IfStmtContext::block() {
  return getRuleContexts<JingleParser::BlockContext>();
}

JingleParser::BlockContext* JingleParser::IfStmtContext::block(size_t i) {
  return getRuleContext<JingleParser::BlockContext>(i);
}

JingleParser::SimpleStmtContext* JingleParser::IfStmtContext::simpleStmt() {
  return getRuleContext<JingleParser::SimpleStmtContext>(0);
}

tree::TerminalNode* JingleParser::IfStmtContext::ELSE() {
  return getToken(JingleParser::ELSE, 0);
}

JingleParser::IfStmtContext* JingleParser::IfStmtContext::ifStmt() {
  return getRuleContext<JingleParser::IfStmtContext>(0);
}


size_t JingleParser::IfStmtContext::getRuleIndex() const {
  return JingleParser::RuleIfStmt;
}

void JingleParser::IfStmtContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterIfStmt(this);
}

void JingleParser::IfStmtContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitIfStmt(this);
}


antlrcpp::Any JingleParser::IfStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitIfStmt(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::IfStmtContext* JingleParser::ifStmt() {
  IfStmtContext *_localctx = _tracker.createInstance<IfStmtContext>(_ctx, getState());
  enterRule(_localctx, 34, JingleParser::RuleIfStmt);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(184);
    match(JingleParser::IF);
    setState(186);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 14, _ctx)) {
    case 1: {
      setState(185);
      simpleStmt();
      break;
    }

    }
    setState(188);
    expression(0);
    setState(189);
    block();
    setState(195);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == JingleParser::ELSE) {
      setState(190);
      match(JingleParser::ELSE);
      setState(193);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case JingleParser::IF: {
          setState(191);
          ifStmt();
          break;
        }

        case JingleParser::INDENT: {
          setState(192);
          block();
          break;
        }

      default:
        throw NoViableAltException(this);
      }
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ForStmtContext ------------------------------------------------------------------

JingleParser::ForStmtContext::ForStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::ForStmtContext::FOR() {
  return getToken(JingleParser::FOR, 0);
}

JingleParser::ExpressionContext* JingleParser::ForStmtContext::expression() {
  return getRuleContext<JingleParser::ExpressionContext>(0);
}

JingleParser::ForClauseContext* JingleParser::ForStmtContext::forClause() {
  return getRuleContext<JingleParser::ForClauseContext>(0);
}


size_t JingleParser::ForStmtContext::getRuleIndex() const {
  return JingleParser::RuleForStmt;
}

void JingleParser::ForStmtContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterForStmt(this);
}

void JingleParser::ForStmtContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitForStmt(this);
}


antlrcpp::Any JingleParser::ForStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitForStmt(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ForStmtContext* JingleParser::forStmt() {
  ForStmtContext *_localctx = _tracker.createInstance<ForStmtContext>(_ctx, getState());
  enterRule(_localctx, 36, JingleParser::RuleForStmt);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(197);
    match(JingleParser::FOR);
    setState(200);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 17, _ctx)) {
    case 1: {
      setState(198);
      expression(0);
      break;
    }

    case 2: {
      setState(199);
      forClause();
      break;
    }

    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- WhileStmtContext ------------------------------------------------------------------

JingleParser::WhileStmtContext::WhileStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::WhileStmtContext::WHILE() {
  return getToken(JingleParser::WHILE, 0);
}

JingleParser::ExpressionContext* JingleParser::WhileStmtContext::expression() {
  return getRuleContext<JingleParser::ExpressionContext>(0);
}

JingleParser::ForClauseContext* JingleParser::WhileStmtContext::forClause() {
  return getRuleContext<JingleParser::ForClauseContext>(0);
}


size_t JingleParser::WhileStmtContext::getRuleIndex() const {
  return JingleParser::RuleWhileStmt;
}

void JingleParser::WhileStmtContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterWhileStmt(this);
}

void JingleParser::WhileStmtContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitWhileStmt(this);
}


antlrcpp::Any JingleParser::WhileStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitWhileStmt(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::WhileStmtContext* JingleParser::whileStmt() {
  WhileStmtContext *_localctx = _tracker.createInstance<WhileStmtContext>(_ctx, getState());
  enterRule(_localctx, 38, JingleParser::RuleWhileStmt);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(202);
    match(JingleParser::WHILE);
    setState(205);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 18, _ctx)) {
    case 1: {
      setState(203);
      expression(0);
      break;
    }

    case 2: {
      setState(204);
      forClause();
      break;
    }

    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ReturnStmtContext ------------------------------------------------------------------

JingleParser::ReturnStmtContext::ReturnStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::ReturnStmtContext::RETURN() {
  return getToken(JingleParser::RETURN, 0);
}

JingleParser::ExpressionListContext* JingleParser::ReturnStmtContext::expressionList() {
  return getRuleContext<JingleParser::ExpressionListContext>(0);
}


size_t JingleParser::ReturnStmtContext::getRuleIndex() const {
  return JingleParser::RuleReturnStmt;
}

void JingleParser::ReturnStmtContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterReturnStmt(this);
}

void JingleParser::ReturnStmtContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitReturnStmt(this);
}


antlrcpp::Any JingleParser::ReturnStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitReturnStmt(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ReturnStmtContext* JingleParser::returnStmt() {
  ReturnStmtContext *_localctx = _tracker.createInstance<ReturnStmtContext>(_ctx, getState());
  enterRule(_localctx, 40, JingleParser::RuleReturnStmt);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(207);
    match(JingleParser::RETURN);
    setState(209);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == JingleParser::LBRACKET) {
      setState(208);
      expressionList();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SimpleStmtContext ------------------------------------------------------------------

JingleParser::SimpleStmtContext::SimpleStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::ExpressionContext* JingleParser::SimpleStmtContext::expression() {
  return getRuleContext<JingleParser::ExpressionContext>(0);
}

JingleParser::IncDecStmtContext* JingleParser::SimpleStmtContext::incDecStmt() {
  return getRuleContext<JingleParser::IncDecStmtContext>(0);
}

JingleParser::Assign_opContext* JingleParser::SimpleStmtContext::assign_op() {
  return getRuleContext<JingleParser::Assign_opContext>(0);
}

JingleParser::ShortVarDeclContext* JingleParser::SimpleStmtContext::shortVarDecl() {
  return getRuleContext<JingleParser::ShortVarDeclContext>(0);
}

JingleParser::EmptyStmtContext* JingleParser::SimpleStmtContext::emptyStmt() {
  return getRuleContext<JingleParser::EmptyStmtContext>(0);
}


size_t JingleParser::SimpleStmtContext::getRuleIndex() const {
  return JingleParser::RuleSimpleStmt;
}

void JingleParser::SimpleStmtContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterSimpleStmt(this);
}

void JingleParser::SimpleStmtContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitSimpleStmt(this);
}


antlrcpp::Any JingleParser::SimpleStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitSimpleStmt(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::SimpleStmtContext* JingleParser::simpleStmt() {
  SimpleStmtContext *_localctx = _tracker.createInstance<SimpleStmtContext>(_ctx, getState());
  enterRule(_localctx, 42, JingleParser::RuleSimpleStmt);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    setState(216);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 20, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(211);
      expression(0);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(212);
      incDecStmt();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(213);
      assign_op();
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(214);
      shortVarDecl();
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(215);
      emptyStmt();
      break;
    }

    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- IncDecStmtContext ------------------------------------------------------------------

JingleParser::IncDecStmtContext::IncDecStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::ExpressionContext* JingleParser::IncDecStmtContext::expression() {
  return getRuleContext<JingleParser::ExpressionContext>(0);
}

tree::TerminalNode* JingleParser::IncDecStmtContext::PLUSPLUS() {
  return getToken(JingleParser::PLUSPLUS, 0);
}

tree::TerminalNode* JingleParser::IncDecStmtContext::MINUSMINUS() {
  return getToken(JingleParser::MINUSMINUS, 0);
}


size_t JingleParser::IncDecStmtContext::getRuleIndex() const {
  return JingleParser::RuleIncDecStmt;
}

void JingleParser::IncDecStmtContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterIncDecStmt(this);
}

void JingleParser::IncDecStmtContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitIncDecStmt(this);
}


antlrcpp::Any JingleParser::IncDecStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitIncDecStmt(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::IncDecStmtContext* JingleParser::incDecStmt() {
  IncDecStmtContext *_localctx = _tracker.createInstance<IncDecStmtContext>(_ctx, getState());
  enterRule(_localctx, 44, JingleParser::RuleIncDecStmt);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(218);
    expression(0);
    setState(219);
    _la = _input->LA(1);
    if (!(_la == JingleParser::PLUSPLUS

    || _la == JingleParser::MINUSMINUS)) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- Assign_opContext ------------------------------------------------------------------

JingleParser::Assign_opContext::Assign_opContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::Assign_opContext::EQUALS() {
  return getToken(JingleParser::EQUALS, 0);
}

tree::TerminalNode* JingleParser::Assign_opContext::PLUS() {
  return getToken(JingleParser::PLUS, 0);
}

tree::TerminalNode* JingleParser::Assign_opContext::MINUS() {
  return getToken(JingleParser::MINUS, 0);
}

tree::TerminalNode* JingleParser::Assign_opContext::MULTIPLY() {
  return getToken(JingleParser::MULTIPLY, 0);
}

tree::TerminalNode* JingleParser::Assign_opContext::DIVIDE() {
  return getToken(JingleParser::DIVIDE, 0);
}

tree::TerminalNode* JingleParser::Assign_opContext::MODULUS() {
  return getToken(JingleParser::MODULUS, 0);
}

tree::TerminalNode* JingleParser::Assign_opContext::ANDSYMBOL() {
  return getToken(JingleParser::ANDSYMBOL, 0);
}


size_t JingleParser::Assign_opContext::getRuleIndex() const {
  return JingleParser::RuleAssign_op;
}

void JingleParser::Assign_opContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterAssign_op(this);
}

void JingleParser::Assign_opContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitAssign_op(this);
}


antlrcpp::Any JingleParser::Assign_opContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitAssign_op(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::Assign_opContext* JingleParser::assign_op() {
  Assign_opContext *_localctx = _tracker.createInstance<Assign_opContext>(_ctx, getState());
  enterRule(_localctx, 46, JingleParser::RuleAssign_op);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(222);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (((((_la - 52) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 52)) & ((1ULL << (JingleParser::PLUS - 52))
      | (1ULL << (JingleParser::MINUS - 52))
      | (1ULL << (JingleParser::MULTIPLY - 52))
      | (1ULL << (JingleParser::DIVIDE - 52))
      | (1ULL << (JingleParser::MODULUS - 52))
      | (1ULL << (JingleParser::ANDSYMBOL - 52)))) != 0)) {
      setState(221);
      _la = _input->LA(1);
      if (!(((((_la - 52) & ~ 0x3fULL) == 0) &&
        ((1ULL << (_la - 52)) & ((1ULL << (JingleParser::PLUS - 52))
        | (1ULL << (JingleParser::MINUS - 52))
        | (1ULL << (JingleParser::MULTIPLY - 52))
        | (1ULL << (JingleParser::DIVIDE - 52))
        | (1ULL << (JingleParser::MODULUS - 52))
        | (1ULL << (JingleParser::ANDSYMBOL - 52)))) != 0))) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
    }
    setState(224);
    match(JingleParser::EQUALS);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ShortVarDeclContext ------------------------------------------------------------------

JingleParser::ShortVarDeclContext::ShortVarDeclContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::IdentifierListContext* JingleParser::ShortVarDeclContext::identifierList() {
  return getRuleContext<JingleParser::IdentifierListContext>(0);
}

tree::TerminalNode* JingleParser::ShortVarDeclContext::WALRUS() {
  return getToken(JingleParser::WALRUS, 0);
}

JingleParser::ExpressionListContext* JingleParser::ShortVarDeclContext::expressionList() {
  return getRuleContext<JingleParser::ExpressionListContext>(0);
}


size_t JingleParser::ShortVarDeclContext::getRuleIndex() const {
  return JingleParser::RuleShortVarDecl;
}

void JingleParser::ShortVarDeclContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterShortVarDecl(this);
}

void JingleParser::ShortVarDeclContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitShortVarDecl(this);
}


antlrcpp::Any JingleParser::ShortVarDeclContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitShortVarDecl(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ShortVarDeclContext* JingleParser::shortVarDecl() {
  ShortVarDeclContext *_localctx = _tracker.createInstance<ShortVarDeclContext>(_ctx, getState());
  enterRule(_localctx, 48, JingleParser::RuleShortVarDecl);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(226);
    identifierList();
    setState(227);
    match(JingleParser::WALRUS);
    setState(228);
    expressionList();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- EmptyStmtContext ------------------------------------------------------------------

JingleParser::EmptyStmtContext::EmptyStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::EndOfStatementContext* JingleParser::EmptyStmtContext::endOfStatement() {
  return getRuleContext<JingleParser::EndOfStatementContext>(0);
}


size_t JingleParser::EmptyStmtContext::getRuleIndex() const {
  return JingleParser::RuleEmptyStmt;
}

void JingleParser::EmptyStmtContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterEmptyStmt(this);
}

void JingleParser::EmptyStmtContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitEmptyStmt(this);
}


antlrcpp::Any JingleParser::EmptyStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitEmptyStmt(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::EmptyStmtContext* JingleParser::emptyStmt() {
  EmptyStmtContext *_localctx = _tracker.createInstance<EmptyStmtContext>(_ctx, getState());
  enterRule(_localctx, 50, JingleParser::RuleEmptyStmt);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(230);
    endOfStatement();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- BlockContext ------------------------------------------------------------------

JingleParser::BlockContext::BlockContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::BlockContext::INDENT() {
  return getToken(JingleParser::INDENT, 0);
}

JingleParser::StatementListContext* JingleParser::BlockContext::statementList() {
  return getRuleContext<JingleParser::StatementListContext>(0);
}

tree::TerminalNode* JingleParser::BlockContext::DEDENT() {
  return getToken(JingleParser::DEDENT, 0);
}


size_t JingleParser::BlockContext::getRuleIndex() const {
  return JingleParser::RuleBlock;
}

void JingleParser::BlockContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterBlock(this);
}

void JingleParser::BlockContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitBlock(this);
}


antlrcpp::Any JingleParser::BlockContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitBlock(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::BlockContext* JingleParser::block() {
  BlockContext *_localctx = _tracker.createInstance<BlockContext>(_ctx, getState());
  enterRule(_localctx, 52, JingleParser::RuleBlock);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(232);
    match(JingleParser::INDENT);
    setState(233);
    statementList();
    setState(234);
    match(JingleParser::DEDENT);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StatementListContext ------------------------------------------------------------------

JingleParser::StatementListContext::StatementListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

JingleParser::StatementContext* JingleParser::StatementListContext::statement() {
  return getRuleContext<JingleParser::StatementContext>(0);
}

JingleParser::EndOfStatementContext* JingleParser::StatementListContext::endOfStatement() {
  return getRuleContext<JingleParser::EndOfStatementContext>(0);
}


size_t JingleParser::StatementListContext::getRuleIndex() const {
  return JingleParser::RuleStatementList;
}

void JingleParser::StatementListContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterStatementList(this);
}

void JingleParser::StatementListContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitStatementList(this);
}


antlrcpp::Any JingleParser::StatementListContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitStatementList(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::StatementListContext* JingleParser::statementList() {
  StatementListContext *_localctx = _tracker.createInstance<StatementListContext>(_ctx, getState());
  enterRule(_localctx, 54, JingleParser::RuleStatementList);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(236);
    statement();
    setState(237);
    endOfStatement();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ForClauseContext ------------------------------------------------------------------

JingleParser::ForClauseContext::ForClauseContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t JingleParser::ForClauseContext::getRuleIndex() const {
  return JingleParser::RuleForClause;
}

void JingleParser::ForClauseContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterForClause(this);
}

void JingleParser::ForClauseContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitForClause(this);
}


antlrcpp::Any JingleParser::ForClauseContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitForClause(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ForClauseContext* JingleParser::forClause() {
  ForClauseContext *_localctx = _tracker.createInstance<ForClauseContext>(_ctx, getState());
  enterRule(_localctx, 56, JingleParser::RuleForClause);

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);

   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ExpressionContext ------------------------------------------------------------------

JingleParser::ExpressionContext::ExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t JingleParser::ExpressionContext::getRuleIndex() const {
  return JingleParser::RuleExpression;
}

void JingleParser::ExpressionContext::copyFrom(ExpressionContext *ctx) {
  ParserRuleContext::copyFrom(ctx);
}

//----------------- ParenExpressionContext ------------------------------------------------------------------

tree::TerminalNode* JingleParser::ParenExpressionContext::LBRACKET() {
  return getToken(JingleParser::LBRACKET, 0);
}

JingleParser::ExpressionContext* JingleParser::ParenExpressionContext::expression() {
  return getRuleContext<JingleParser::ExpressionContext>(0);
}

tree::TerminalNode* JingleParser::ParenExpressionContext::RBRACKET() {
  return getToken(JingleParser::RBRACKET, 0);
}

JingleParser::ParenExpressionContext::ParenExpressionContext(ExpressionContext *ctx) { copyFrom(ctx); }

void JingleParser::ParenExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterParenExpression(this);
}
void JingleParser::ParenExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitParenExpression(this);
}

antlrcpp::Any JingleParser::ParenExpressionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitParenExpression(this);
  else
    return visitor->visitChildren(this);
}
//----------------- BinaryOperationContext ------------------------------------------------------------------

std::vector<JingleParser::ExpressionContext *> JingleParser::BinaryOperationContext::expression() {
  return getRuleContexts<JingleParser::ExpressionContext>();
}

JingleParser::ExpressionContext* JingleParser::BinaryOperationContext::expression(size_t i) {
  return getRuleContext<JingleParser::ExpressionContext>(i);
}

tree::TerminalNode* JingleParser::BinaryOperationContext::DIVIDE() {
  return getToken(JingleParser::DIVIDE, 0);
}

tree::TerminalNode* JingleParser::BinaryOperationContext::MULTIPLY() {
  return getToken(JingleParser::MULTIPLY, 0);
}

tree::TerminalNode* JingleParser::BinaryOperationContext::PLUS() {
  return getToken(JingleParser::PLUS, 0);
}

tree::TerminalNode* JingleParser::BinaryOperationContext::MINUS() {
  return getToken(JingleParser::MINUS, 0);
}

JingleParser::BinaryOperationContext::BinaryOperationContext(ExpressionContext *ctx) { copyFrom(ctx); }

void JingleParser::BinaryOperationContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterBinaryOperation(this);
}
void JingleParser::BinaryOperationContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitBinaryOperation(this);
}

antlrcpp::Any JingleParser::BinaryOperationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitBinaryOperation(this);
  else
    return visitor->visitChildren(this);
}
//----------------- TypeConversionContext ------------------------------------------------------------------

tree::TerminalNode* JingleParser::TypeConversionContext::AS() {
  return getToken(JingleParser::AS, 0);
}

JingleParser::ExpressionContext* JingleParser::TypeConversionContext::expression() {
  return getRuleContext<JingleParser::ExpressionContext>(0);
}

JingleParser::DataTypeContext* JingleParser::TypeConversionContext::dataType() {
  return getRuleContext<JingleParser::DataTypeContext>(0);
}

JingleParser::TypeConversionContext::TypeConversionContext(ExpressionContext *ctx) { copyFrom(ctx); }

void JingleParser::TypeConversionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterTypeConversion(this);
}
void JingleParser::TypeConversionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitTypeConversion(this);
}

antlrcpp::Any JingleParser::TypeConversionContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitTypeConversion(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::ExpressionContext* JingleParser::expression() {
   return expression(0);
}

JingleParser::ExpressionContext* JingleParser::expression(int precedence) {
  ParserRuleContext *parentContext = _ctx;
  size_t parentState = getState();
  JingleParser::ExpressionContext *_localctx = _tracker.createInstance<ExpressionContext>(_ctx, parentState);
  JingleParser::ExpressionContext *previousContext = _localctx;
  (void)previousContext; // Silence compiler, in case the context is not used by generated code.
  size_t startState = 58;
  enterRecursionRule(_localctx, 58, JingleParser::RuleExpression, precedence);

    size_t _la = 0;

  auto onExit = finally([=] {
    unrollRecursionContexts(parentContext);
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    _localctx = _tracker.createInstance<ParenExpressionContext>(_localctx);
    _ctx = _localctx;
    previousContext = _localctx;

    setState(242);
    match(JingleParser::LBRACKET);
    setState(243);
    expression(0);
    setState(244);
    match(JingleParser::RBRACKET);
    _ctx->stop = _input->LT(-1);
    setState(257);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        if (!_parseListeners.empty())
          triggerExitRuleEvent();
        previousContext = _localctx;
        setState(255);
        _errHandler->sync(this);
        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 22, _ctx)) {
        case 1: {
          auto newContext = _tracker.createInstance<BinaryOperationContext>(_tracker.createInstance<ExpressionContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpression);
          setState(246);

          if (!(precpred(_ctx, 4))) throw FailedPredicateException(this, "precpred(_ctx, 4)");
          setState(247);
          dynamic_cast<BinaryOperationContext *>(_localctx)->operator = _input->LT(1);
          _la = _input->LA(1);
          if (!(_la == JingleParser::MULTIPLY

          || _la == JingleParser::DIVIDE)) {
            dynamic_cast<BinaryOperationContext *>(_localctx)->operator = _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(248);
          dynamic_cast<BinaryOperationContext *>(_localctx)->right = expression(5);
          break;
        }

        case 2: {
          auto newContext = _tracker.createInstance<BinaryOperationContext>(_tracker.createInstance<ExpressionContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->left = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpression);
          setState(249);

          if (!(precpred(_ctx, 3))) throw FailedPredicateException(this, "precpred(_ctx, 3)");
          setState(250);
          dynamic_cast<BinaryOperationContext *>(_localctx)->operator = _input->LT(1);
          _la = _input->LA(1);
          if (!(_la == JingleParser::PLUS

          || _la == JingleParser::MINUS)) {
            dynamic_cast<BinaryOperationContext *>(_localctx)->operator = _errHandler->recoverInline(this);
          }
          else {
            _errHandler->reportMatch(this);
            consume();
          }
          setState(251);
          dynamic_cast<BinaryOperationContext *>(_localctx)->right = expression(4);
          break;
        }

        case 3: {
          auto newContext = _tracker.createInstance<TypeConversionContext>(_tracker.createInstance<ExpressionContext>(parentContext, parentState));
          _localctx = newContext;
          newContext->value = previousContext;
          pushNewRecursionContext(newContext, startState, RuleExpression);
          setState(252);

          if (!(precpred(_ctx, 2))) throw FailedPredicateException(this, "precpred(_ctx, 2)");
          setState(253);
          match(JingleParser::AS);
          setState(254);
          dynamic_cast<TypeConversionContext *>(_localctx)->targetType = dataType();
          break;
        }

        } 
      }
      setState(259);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx);
    }
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }
  return _localctx;
}

//----------------- DataTypeContext ------------------------------------------------------------------

JingleParser::DataTypeContext::DataTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* JingleParser::DataTypeContext::TYPE_INT() {
  return getToken(JingleParser::TYPE_INT, 0);
}

tree::TerminalNode* JingleParser::DataTypeContext::TYPE_DECIMAL() {
  return getToken(JingleParser::TYPE_DECIMAL, 0);
}

tree::TerminalNode* JingleParser::DataTypeContext::TYPE_STRING() {
  return getToken(JingleParser::TYPE_STRING, 0);
}


size_t JingleParser::DataTypeContext::getRuleIndex() const {
  return JingleParser::RuleDataType;
}

void JingleParser::DataTypeContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterDataType(this);
}

void JingleParser::DataTypeContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<JingleParserListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitDataType(this);
}


antlrcpp::Any JingleParser::DataTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<JingleParserVisitor*>(visitor))
    return parserVisitor->visitDataType(this);
  else
    return visitor->visitChildren(this);
}

JingleParser::DataTypeContext* JingleParser::dataType() {
  DataTypeContext *_localctx = _tracker.createInstance<DataTypeContext>(_ctx, getState());
  enterRule(_localctx, 60, JingleParser::RuleDataType);
  size_t _la = 0;

  auto onExit = finally([=] {
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(260);
    _la = _input->LA(1);
    if (!(((((_la - 66) & ~ 0x3fULL) == 0) &&
      ((1ULL << (_la - 66)) & ((1ULL << (JingleParser::TYPE_INT - 66))
      | (1ULL << (JingleParser::TYPE_DECIMAL - 66))
      | (1ULL << (JingleParser::TYPE_STRING - 66)))) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

bool JingleParser::sempred(RuleContext *context, size_t ruleIndex, size_t predicateIndex) {
  switch (ruleIndex) {
    case 29: return expressionSempred(dynamic_cast<ExpressionContext *>(context), predicateIndex);

  default:
    break;
  }
  return true;
}

bool JingleParser::expressionSempred(ExpressionContext *_localctx, size_t predicateIndex) {
  switch (predicateIndex) {
    case 0: return precpred(_ctx, 4);
    case 1: return precpred(_ctx, 3);
    case 2: return precpred(_ctx, 2);

  default:
    break;
  }
  return true;
}

// Static vars and initialization.
std::vector<dfa::DFA> JingleParser::_decisionToDFA;
atn::PredictionContextCache JingleParser::_sharedContextCache;

// We own the ATN which in turn owns the ATN states.
atn::ATN JingleParser::_atn;
std::vector<uint16_t> JingleParser::_serializedATN;

std::vector<std::string> JingleParser::_ruleNames = {
  "jingleFile", "packagePhrase", "importDecl", "importSpec", "topLevelDecl", 
  "line", "endOfStatement", "statement", "declaration", "varDecl", "funcDecl", 
  "echoDisplay", "params", "identifierList", "expressionList", "paramList", 
  "paramDecl", "ifStmt", "forStmt", "whileStmt", "returnStmt", "simpleStmt", 
  "incDecStmt", "assign_op", "shortVarDecl", "emptyStmt", "block", "statementList", 
  "forClause", "expression", "dataType"
};

std::vector<std::string> JingleParser::_literalNames = {
  "", "", "", "", "", "", "'var'", "'arr'", "'con'", "'loc'", "'echo'", 
  "'return'", "'if'", "'then'", "'and'", "'or'", "'in'", "'else'", "'elif'", 
  "'while'", "'for'", "'true'", "'false'", "'fn'", "'class'", "'let'", "'bind'", 
  "'trait'", "'def'", "'proto'", "'enum'", "'import'", "'from'", "'package'", 
  "'as'", "'break'", "'abstract'", "'select'", "'input'", "'each'", "'new'", 
  "'continue'", "'export'", "'include'", "'require'", "'summon'", "':='", 
  "'='", "'=='", "'!='", "'<='", "'>='", "'+'", "'-'", "'*'", "'/'", "'<'", 
  "'>'", "'!'", "'^'", "'%'", "'|'", "'||'", "'#'", "'&'", "'&&'", "", "", 
  "", "", "','", "'('", "')'", "'{'", "", "'['", "']'", "'->'", "':'", "'.'", 
  "'...'", "'++'", "'--'", "'float'", "'string'", "'bool'", "'null'", "'char'", 
  "", "", "", "", "", "", "", "'\\\"'", "'\\\\'", "'\\n'", "'\\#'", "", 
  "'#{'"
};

std::vector<std::string> JingleParser::_symbolicNames = {
  "", "INDENT", "DEDENT", "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", 
  "VAR", "ARRAY", "CONST", "LOCAL", "ECHO", "RETURN", "IF", "THEN", "AND", 
  "OR", "IN", "ELSE", "ELSEIF", "WHILE", "FOR", "TRUE", "FALSE", "FUNCTION", 
  "CLASS", "LET", "BIND", "TRAIT", "DEFINE", "PROTOCOL", "ENUM", "IMPORT", 
  "FROM", "PACKAGE", "AS", "BREAK", "ABSTRACT", "SELECT", "INPUT", "EACH", 
  "NEW", "CONTINUE", "EXPORT", "INCLUDE", "REQUIRE", "SUMMON", "WALRUS", 
  "EQUALS", "EQEQ", "NOTEQUAL", "LTEQUALS", "GTEQUALS", "PLUS", "MINUS", 
  "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN", "BANG", "POWER", "MODULUS", 
  "VERTICAL", "ORSYMBOL", "HASH", "AMBERSAND", "ANDSYMBOL", "TYPE_INT", 
  "TYPE_DECIMAL", "TYPE_STRING", "TYPE_BOOLEAN", "COMMA", "LBRACKET", "RBRACKET", 
  "LBRACE", "RBRACE", "LSQRBRACKET", "RSQRBRACKET", "ARROW", "COLON", "DOT", 
  "ELLIPSIS", "PLUSPLUS", "MINUSMINUS", "FLOAT", "STRING", "BOOLEAN", "NULL", 
  "CHAR", "INT_LITERAL", "FLOAT_LITERAL", "WHITESPACE", "COMMENT", "TERMINATOR", 
  "STRING_OPEN", "UNMATCHED", "SCAPE_STRING_DELIMITER", "ESCAPE_SLASH", 
  "ESCAPE_NEWLINE", "ESCAPE_SHARP", "STRING_CLOSE", "INTERPOLATION_OPEN", 
  "STRING_CONTENT", "INTERPOLATION_CLOSE", "NOUNICODEID", "IDENTIFIER", 
  "BINARY_OP", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "RUNE_LIT", "LITTLE_U_VALUE", 
  "BIG_U_VALUE"
};

dfa::Vocabulary JingleParser::_vocabulary(_literalNames, _symbolicNames);

std::vector<std::string> JingleParser::_tokenNames;

JingleParser::Initializer::Initializer() {
	for (size_t i = 0; i < _symbolicNames.size(); ++i) {
		std::string name = _vocabulary.getLiteralName(i);
		if (name.empty()) {
			name = _vocabulary.getSymbolicName(i);
		}

		if (name.empty()) {
			_tokenNames.push_back("<INVALID>");
		} else {
      _tokenNames.push_back(name);
    }
	}

  _serializedATN = {
    0x3, 0x608b, 0xa72a, 0x8133, 0xb9ed, 0x417c, 0x3be7, 0x7786, 0x5964, 
    0x3, 0x71, 0x109, 0x4, 0x2, 0x9, 0x2, 0x4, 0x3, 0x9, 0x3, 0x4, 0x4, 
    0x9, 0x4, 0x4, 0x5, 0x9, 0x5, 0x4, 0x6, 0x9, 0x6, 0x4, 0x7, 0x9, 0x7, 
    0x4, 0x8, 0x9, 0x8, 0x4, 0x9, 0x9, 0x9, 0x4, 0xa, 0x9, 0xa, 0x4, 0xb, 
    0x9, 0xb, 0x4, 0xc, 0x9, 0xc, 0x4, 0xd, 0x9, 0xd, 0x4, 0xe, 0x9, 0xe, 
    0x4, 0xf, 0x9, 0xf, 0x4, 0x10, 0x9, 0x10, 0x4, 0x11, 0x9, 0x11, 0x4, 
    0x12, 0x9, 0x12, 0x4, 0x13, 0x9, 0x13, 0x4, 0x14, 0x9, 0x14, 0x4, 0x15, 
    0x9, 0x15, 0x4, 0x16, 0x9, 0x16, 0x4, 0x17, 0x9, 0x17, 0x4, 0x18, 0x9, 
    0x18, 0x4, 0x19, 0x9, 0x19, 0x4, 0x1a, 0x9, 0x1a, 0x4, 0x1b, 0x9, 0x1b, 
    0x4, 0x1c, 0x9, 0x1c, 0x4, 0x1d, 0x9, 0x1d, 0x4, 0x1e, 0x9, 0x1e, 0x4, 
    0x1f, 0x9, 0x1f, 0x4, 0x20, 0x9, 0x20, 0x3, 0x2, 0x3, 0x2, 0x3, 0x2, 
    0x3, 0x2, 0x3, 0x2, 0x7, 0x2, 0x46, 0xa, 0x2, 0xc, 0x2, 0xe, 0x2, 0x49, 
    0xb, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3, 0x2, 0x7, 0x2, 0x4e, 0xa, 0x2, 0xc, 
    0x2, 0xe, 0x2, 0x51, 0xb, 0x2, 0x3, 0x3, 0x3, 0x3, 0x3, 0x3, 0x3, 0x4, 
    0x3, 0x4, 0x3, 0x4, 0x3, 0x4, 0x3, 0x4, 0x3, 0x4, 0x7, 0x4, 0x5c, 0xa, 
    0x4, 0xc, 0x4, 0xe, 0x4, 0x5f, 0xb, 0x4, 0x3, 0x4, 0x5, 0x4, 0x62, 0xa, 
    0x4, 0x3, 0x5, 0x3, 0x5, 0x3, 0x6, 0x3, 0x6, 0x5, 0x6, 0x68, 0xa, 0x6, 
    0x3, 0x7, 0x3, 0x7, 0x3, 0x7, 0x3, 0x8, 0x3, 0x8, 0x3, 0x9, 0x3, 0x9, 
    0x3, 0x9, 0x3, 0x9, 0x3, 0x9, 0x3, 0x9, 0x3, 0x9, 0x3, 0x9, 0x5, 0x9, 
    0x77, 0xa, 0x9, 0x3, 0xa, 0x3, 0xa, 0x3, 0xa, 0x5, 0xa, 0x7c, 0xa, 0xa, 
    0x3, 0xb, 0x3, 0xb, 0x3, 0xb, 0x3, 0xb, 0x3, 0xb, 0x3, 0xb, 0x3, 0xc, 
    0x3, 0xc, 0x3, 0xc, 0x3, 0xc, 0x3, 0xc, 0x3, 0xc, 0x3, 0xc, 0x3, 0xc, 
    0x3, 0xc, 0x3, 0xc, 0x3, 0xd, 0x3, 0xd, 0x3, 0xd, 0x3, 0xd, 0x3, 0xd, 
    0x3, 0xd, 0x3, 0xe, 0x3, 0xe, 0x3, 0xe, 0x5, 0xe, 0x97, 0xa, 0xe, 0x5, 
    0xe, 0x99, 0xa, 0xe, 0x3, 0xe, 0x3, 0xe, 0x3, 0xf, 0x3, 0xf, 0x3, 0xf, 
    0x7, 0xf, 0xa0, 0xa, 0xf, 0xc, 0xf, 0xe, 0xf, 0xa3, 0xb, 0xf, 0x3, 0x10, 
    0x3, 0x10, 0x3, 0x10, 0x7, 0x10, 0xa8, 0xa, 0x10, 0xc, 0x10, 0xe, 0x10, 
    0xab, 0xb, 0x10, 0x3, 0x11, 0x3, 0x11, 0x3, 0x11, 0x7, 0x11, 0xb0, 0xa, 
    0x11, 0xc, 0x11, 0xe, 0x11, 0xb3, 0xb, 0x11, 0x3, 0x12, 0x5, 0x12, 0xb6, 
    0xa, 0x12, 0x3, 0x12, 0x5, 0x12, 0xb9, 0xa, 0x12, 0x3, 0x13, 0x3, 0x13, 
    0x5, 0x13, 0xbd, 0xa, 0x13, 0x3, 0x13, 0x3, 0x13, 0x3, 0x13, 0x3, 0x13, 
    0x3, 0x13, 0x5, 0x13, 0xc4, 0xa, 0x13, 0x5, 0x13, 0xc6, 0xa, 0x13, 0x3, 
    0x14, 0x3, 0x14, 0x3, 0x14, 0x5, 0x14, 0xcb, 0xa, 0x14, 0x3, 0x15, 0x3, 
    0x15, 0x3, 0x15, 0x5, 0x15, 0xd0, 0xa, 0x15, 0x3, 0x16, 0x3, 0x16, 0x5, 
    0x16, 0xd4, 0xa, 0x16, 0x3, 0x17, 0x3, 0x17, 0x3, 0x17, 0x3, 0x17, 0x3, 
    0x17, 0x5, 0x17, 0xdb, 0xa, 0x17, 0x3, 0x18, 0x3, 0x18, 0x3, 0x18, 0x3, 
    0x19, 0x5, 0x19, 0xe1, 0xa, 0x19, 0x3, 0x19, 0x3, 0x19, 0x3, 0x1a, 0x3, 
    0x1a, 0x3, 0x1a, 0x3, 0x1a, 0x3, 0x1b, 0x3, 0x1b, 0x3, 0x1c, 0x3, 0x1c, 
    0x3, 0x1c, 0x3, 0x1c, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1d, 0x3, 0x1e, 0x3, 
    0x1e, 0x3, 0x1f, 0x3, 0x1f, 0x3, 0x1f, 0x3, 0x1f, 0x3, 0x1f, 0x3, 0x1f, 
    0x3, 0x1f, 0x3, 0x1f, 0x3, 0x1f, 0x3, 0x1f, 0x3, 0x1f, 0x3, 0x1f, 0x3, 
    0x1f, 0x3, 0x1f, 0x7, 0x1f, 0x102, 0xa, 0x1f, 0xc, 0x1f, 0xe, 0x1f, 
    0x105, 0xb, 0x1f, 0x3, 0x20, 0x3, 0x20, 0x3, 0x20, 0x2, 0x3, 0x3c, 0x21, 
    0x2, 0x4, 0x6, 0x8, 0xa, 0xc, 0xe, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 
    0x1c, 0x1e, 0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 
    0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e, 0x2, 0x9, 0x3, 0x3, 0x5, 0x5, 0x4, 
    0x2, 0x5a, 0x5a, 0x69, 0x69, 0x3, 0x2, 0x53, 0x54, 0x5, 0x2, 0x36, 0x39, 
    0x3e, 0x3e, 0x43, 0x43, 0x3, 0x2, 0x38, 0x39, 0x3, 0x2, 0x36, 0x37, 
    0x3, 0x2, 0x44, 0x46, 0x2, 0x10e, 0x2, 0x40, 0x3, 0x2, 0x2, 0x2, 0x4, 
    0x52, 0x3, 0x2, 0x2, 0x2, 0x6, 0x55, 0x3, 0x2, 0x2, 0x2, 0x8, 0x63, 
    0x3, 0x2, 0x2, 0x2, 0xa, 0x67, 0x3, 0x2, 0x2, 0x2, 0xc, 0x69, 0x3, 0x2, 
    0x2, 0x2, 0xe, 0x6c, 0x3, 0x2, 0x2, 0x2, 0x10, 0x76, 0x3, 0x2, 0x2, 
    0x2, 0x12, 0x7b, 0x3, 0x2, 0x2, 0x2, 0x14, 0x7d, 0x3, 0x2, 0x2, 0x2, 
    0x16, 0x83, 0x3, 0x2, 0x2, 0x2, 0x18, 0x8d, 0x3, 0x2, 0x2, 0x2, 0x1a, 
    0x93, 0x3, 0x2, 0x2, 0x2, 0x1c, 0x9c, 0x3, 0x2, 0x2, 0x2, 0x1e, 0xa4, 
    0x3, 0x2, 0x2, 0x2, 0x20, 0xac, 0x3, 0x2, 0x2, 0x2, 0x22, 0xb5, 0x3, 
    0x2, 0x2, 0x2, 0x24, 0xba, 0x3, 0x2, 0x2, 0x2, 0x26, 0xc7, 0x3, 0x2, 
    0x2, 0x2, 0x28, 0xcc, 0x3, 0x2, 0x2, 0x2, 0x2a, 0xd1, 0x3, 0x2, 0x2, 
    0x2, 0x2c, 0xda, 0x3, 0x2, 0x2, 0x2, 0x2e, 0xdc, 0x3, 0x2, 0x2, 0x2, 
    0x30, 0xe0, 0x3, 0x2, 0x2, 0x2, 0x32, 0xe4, 0x3, 0x2, 0x2, 0x2, 0x34, 
    0xe8, 0x3, 0x2, 0x2, 0x2, 0x36, 0xea, 0x3, 0x2, 0x2, 0x2, 0x38, 0xee, 
    0x3, 0x2, 0x2, 0x2, 0x3a, 0xf1, 0x3, 0x2, 0x2, 0x2, 0x3c, 0xf3, 0x3, 
    0x2, 0x2, 0x2, 0x3e, 0x106, 0x3, 0x2, 0x2, 0x2, 0x40, 0x41, 0x5, 0x4, 
    0x3, 0x2, 0x41, 0x47, 0x5, 0xe, 0x8, 0x2, 0x42, 0x43, 0x5, 0x6, 0x4, 
    0x2, 0x43, 0x44, 0x5, 0xe, 0x8, 0x2, 0x44, 0x46, 0x3, 0x2, 0x2, 0x2, 
    0x45, 0x42, 0x3, 0x2, 0x2, 0x2, 0x46, 0x49, 0x3, 0x2, 0x2, 0x2, 0x47, 
    0x45, 0x3, 0x2, 0x2, 0x2, 0x47, 0x48, 0x3, 0x2, 0x2, 0x2, 0x48, 0x4f, 
    0x3, 0x2, 0x2, 0x2, 0x49, 0x47, 0x3, 0x2, 0x2, 0x2, 0x4a, 0x4b, 0x5, 
    0xa, 0x6, 0x2, 0x4b, 0x4c, 0x5, 0xe, 0x8, 0x2, 0x4c, 0x4e, 0x3, 0x2, 
    0x2, 0x2, 0x4d, 0x4a, 0x3, 0x2, 0x2, 0x2, 0x4e, 0x51, 0x3, 0x2, 0x2, 
    0x2, 0x4f, 0x4d, 0x3, 0x2, 0x2, 0x2, 0x4f, 0x50, 0x3, 0x2, 0x2, 0x2, 
    0x50, 0x3, 0x3, 0x2, 0x2, 0x2, 0x51, 0x4f, 0x3, 0x2, 0x2, 0x2, 0x52, 
    0x53, 0x7, 0x23, 0x2, 0x2, 0x53, 0x54, 0x7, 0x69, 0x2, 0x2, 0x54, 0x5, 
    0x3, 0x2, 0x2, 0x2, 0x55, 0x61, 0x7, 0x21, 0x2, 0x2, 0x56, 0x62, 0x5, 
    0x8, 0x5, 0x2, 0x57, 0x5d, 0x7, 0x49, 0x2, 0x2, 0x58, 0x59, 0x5, 0x8, 
    0x5, 0x2, 0x59, 0x5a, 0x5, 0xe, 0x8, 0x2, 0x5a, 0x5c, 0x3, 0x2, 0x2, 
    0x2, 0x5b, 0x58, 0x3, 0x2, 0x2, 0x2, 0x5c, 0x5f, 0x3, 0x2, 0x2, 0x2, 
    0x5d, 0x5b, 0x3, 0x2, 0x2, 0x2, 0x5d, 0x5e, 0x3, 0x2, 0x2, 0x2, 0x5e, 
    0x60, 0x3, 0x2, 0x2, 0x2, 0x5f, 0x5d, 0x3, 0x2, 0x2, 0x2, 0x60, 0x62, 
    0x7, 0x4a, 0x2, 0x2, 0x61, 0x56, 0x3, 0x2, 0x2, 0x2, 0x61, 0x57, 0x3, 
    0x2, 0x2, 0x2, 0x62, 0x7, 0x3, 0x2, 0x2, 0x2, 0x63, 0x64, 0x7, 0x6e, 
    0x2, 0x2, 0x64, 0x9, 0x3, 0x2, 0x2, 0x2, 0x65, 0x68, 0x5, 0x10, 0x9, 
    0x2, 0x66, 0x68, 0x5, 0x16, 0xc, 0x2, 0x67, 0x65, 0x3, 0x2, 0x2, 0x2, 
    0x67, 0x66, 0x3, 0x2, 0x2, 0x2, 0x68, 0xb, 0x3, 0x2, 0x2, 0x2, 0x69, 
    0x6a, 0x5, 0x10, 0x9, 0x2, 0x6a, 0x6b, 0x9, 0x2, 0x2, 0x2, 0x6b, 0xd, 
    0x3, 0x2, 0x2, 0x2, 0x6c, 0x6d, 0x9, 0x2, 0x2, 0x2, 0x6d, 0xf, 0x3, 
    0x2, 0x2, 0x2, 0x6e, 0x77, 0x3, 0x2, 0x2, 0x2, 0x6f, 0x77, 0x5, 0x12, 
    0xa, 0x2, 0x70, 0x77, 0x5, 0x24, 0x13, 0x2, 0x71, 0x77, 0x5, 0x26, 0x14, 
    0x2, 0x72, 0x77, 0x5, 0x2a, 0x16, 0x2, 0x73, 0x77, 0x5, 0x2c, 0x17, 
    0x2, 0x74, 0x77, 0x5, 0x36, 0x1c, 0x2, 0x75, 0x77, 0x5, 0x18, 0xd, 0x2, 
    0x76, 0x6e, 0x3, 0x2, 0x2, 0x2, 0x76, 0x6f, 0x3, 0x2, 0x2, 0x2, 0x76, 
    0x70, 0x3, 0x2, 0x2, 0x2, 0x76, 0x71, 0x3, 0x2, 0x2, 0x2, 0x76, 0x72, 
    0x3, 0x2, 0x2, 0x2, 0x76, 0x73, 0x3, 0x2, 0x2, 0x2, 0x76, 0x74, 0x3, 
    0x2, 0x2, 0x2, 0x76, 0x75, 0x3, 0x2, 0x2, 0x2, 0x77, 0x11, 0x3, 0x2, 
    0x2, 0x2, 0x78, 0x7c, 0x3, 0x2, 0x2, 0x2, 0x79, 0x7c, 0x5, 0x14, 0xb, 
    0x2, 0x7a, 0x7c, 0x5, 0x16, 0xc, 0x2, 0x7b, 0x78, 0x3, 0x2, 0x2, 0x2, 
    0x7b, 0x79, 0x3, 0x2, 0x2, 0x2, 0x7b, 0x7a, 0x3, 0x2, 0x2, 0x2, 0x7c, 
    0x13, 0x3, 0x2, 0x2, 0x2, 0x7d, 0x7e, 0x7, 0x8, 0x2, 0x2, 0x7e, 0x7f, 
    0x7, 0x69, 0x2, 0x2, 0x7f, 0x80, 0x7, 0x5c, 0x2, 0x2, 0x80, 0x81, 0x7, 
    0x31, 0x2, 0x2, 0x81, 0x82, 0x9, 0x3, 0x2, 0x2, 0x82, 0x15, 0x3, 0x2, 
    0x2, 0x2, 0x83, 0x84, 0x7, 0x19, 0x2, 0x2, 0x84, 0x85, 0x7, 0x5c, 0x2, 
    0x2, 0x85, 0x86, 0x7, 0x69, 0x2, 0x2, 0x86, 0x87, 0x7, 0x5c, 0x2, 0x2, 
    0x87, 0x88, 0x7, 0x49, 0x2, 0x2, 0x88, 0x89, 0x5, 0x1a, 0xe, 0x2, 0x89, 
    0x8a, 0x7, 0x4a, 0x2, 0x2, 0x8a, 0x8b, 0x7, 0x5c, 0x2, 0x2, 0x8b, 0x8c, 
    0x7, 0x50, 0x2, 0x2, 0x8c, 0x17, 0x3, 0x2, 0x2, 0x2, 0x8d, 0x8e, 0x7, 
    0xc, 0x2, 0x2, 0x8e, 0x8f, 0x7, 0x5c, 0x2, 0x2, 0x8f, 0x90, 0x7, 0x49, 
    0x2, 0x2, 0x90, 0x91, 0x9, 0x3, 0x2, 0x2, 0x91, 0x92, 0x7, 0x4a, 0x2, 
    0x2, 0x92, 0x19, 0x3, 0x2, 0x2, 0x2, 0x93, 0x98, 0x7, 0x49, 0x2, 0x2, 
    0x94, 0x96, 0x5, 0x20, 0x11, 0x2, 0x95, 0x97, 0x7, 0x48, 0x2, 0x2, 0x96, 
    0x95, 0x3, 0x2, 0x2, 0x2, 0x96, 0x97, 0x3, 0x2, 0x2, 0x2, 0x97, 0x99, 
    0x3, 0x2, 0x2, 0x2, 0x98, 0x94, 0x3, 0x2, 0x2, 0x2, 0x98, 0x99, 0x3, 
    0x2, 0x2, 0x2, 0x99, 0x9a, 0x3, 0x2, 0x2, 0x2, 0x9a, 0x9b, 0x7, 0x4a, 
    0x2, 0x2, 0x9b, 0x1b, 0x3, 0x2, 0x2, 0x2, 0x9c, 0xa1, 0x7, 0x69, 0x2, 
    0x2, 0x9d, 0x9e, 0x7, 0x48, 0x2, 0x2, 0x9e, 0xa0, 0x7, 0x69, 0x2, 0x2, 
    0x9f, 0x9d, 0x3, 0x2, 0x2, 0x2, 0xa0, 0xa3, 0x3, 0x2, 0x2, 0x2, 0xa1, 
    0x9f, 0x3, 0x2, 0x2, 0x2, 0xa1, 0xa2, 0x3, 0x2, 0x2, 0x2, 0xa2, 0x1d, 
    0x3, 0x2, 0x2, 0x2, 0xa3, 0xa1, 0x3, 0x2, 0x2, 0x2, 0xa4, 0xa9, 0x5, 
    0x3c, 0x1f, 0x2, 0xa5, 0xa6, 0x7, 0x48, 0x2, 0x2, 0xa6, 0xa8, 0x7, 0x69, 
    0x2, 0x2, 0xa7, 0xa5, 0x3, 0x2, 0x2, 0x2, 0xa8, 0xab, 0x3, 0x2, 0x2, 
    0x2, 0xa9, 0xa7, 0x3, 0x2, 0x2, 0x2, 0xa9, 0xaa, 0x3, 0x2, 0x2, 0x2, 
    0xaa, 0x1f, 0x3, 0x2, 0x2, 0x2, 0xab, 0xa9, 0x3, 0x2, 0x2, 0x2, 0xac, 
    0xb1, 0x5, 0x22, 0x12, 0x2, 0xad, 0xae, 0x7, 0x48, 0x2, 0x2, 0xae, 0xb0, 
    0x5, 0x22, 0x12, 0x2, 0xaf, 0xad, 0x3, 0x2, 0x2, 0x2, 0xb0, 0xb3, 0x3, 
    0x2, 0x2, 0x2, 0xb1, 0xaf, 0x3, 0x2, 0x2, 0x2, 0xb1, 0xb2, 0x3, 0x2, 
    0x2, 0x2, 0xb2, 0x21, 0x3, 0x2, 0x2, 0x2, 0xb3, 0xb1, 0x3, 0x2, 0x2, 
    0x2, 0xb4, 0xb6, 0x5, 0x1c, 0xf, 0x2, 0xb5, 0xb4, 0x3, 0x2, 0x2, 0x2, 
    0xb5, 0xb6, 0x3, 0x2, 0x2, 0x2, 0xb6, 0xb8, 0x3, 0x2, 0x2, 0x2, 0xb7, 
    0xb9, 0x7, 0x52, 0x2, 0x2, 0xb8, 0xb7, 0x3, 0x2, 0x2, 0x2, 0xb8, 0xb9, 
    0x3, 0x2, 0x2, 0x2, 0xb9, 0x23, 0x3, 0x2, 0x2, 0x2, 0xba, 0xbc, 0x7, 
    0xe, 0x2, 0x2, 0xbb, 0xbd, 0x5, 0x2c, 0x17, 0x2, 0xbc, 0xbb, 0x3, 0x2, 
    0x2, 0x2, 0xbc, 0xbd, 0x3, 0x2, 0x2, 0x2, 0xbd, 0xbe, 0x3, 0x2, 0x2, 
    0x2, 0xbe, 0xbf, 0x5, 0x3c, 0x1f, 0x2, 0xbf, 0xc5, 0x5, 0x36, 0x1c, 
    0x2, 0xc0, 0xc3, 0x7, 0x13, 0x2, 0x2, 0xc1, 0xc4, 0x5, 0x24, 0x13, 0x2, 
    0xc2, 0xc4, 0x5, 0x36, 0x1c, 0x2, 0xc3, 0xc1, 0x3, 0x2, 0x2, 0x2, 0xc3, 
    0xc2, 0x3, 0x2, 0x2, 0x2, 0xc4, 0xc6, 0x3, 0x2, 0x2, 0x2, 0xc5, 0xc0, 
    0x3, 0x2, 0x2, 0x2, 0xc5, 0xc6, 0x3, 0x2, 0x2, 0x2, 0xc6, 0x25, 0x3, 
    0x2, 0x2, 0x2, 0xc7, 0xca, 0x7, 0x16, 0x2, 0x2, 0xc8, 0xcb, 0x5, 0x3c, 
    0x1f, 0x2, 0xc9, 0xcb, 0x5, 0x3a, 0x1e, 0x2, 0xca, 0xc8, 0x3, 0x2, 0x2, 
    0x2, 0xca, 0xc9, 0x3, 0x2, 0x2, 0x2, 0xca, 0xcb, 0x3, 0x2, 0x2, 0x2, 
    0xcb, 0x27, 0x3, 0x2, 0x2, 0x2, 0xcc, 0xcf, 0x7, 0x15, 0x2, 0x2, 0xcd, 
    0xd0, 0x5, 0x3c, 0x1f, 0x2, 0xce, 0xd0, 0x5, 0x3a, 0x1e, 0x2, 0xcf, 
    0xcd, 0x3, 0x2, 0x2, 0x2, 0xcf, 0xce, 0x3, 0x2, 0x2, 0x2, 0xcf, 0xd0, 
    0x3, 0x2, 0x2, 0x2, 0xd0, 0x29, 0x3, 0x2, 0x2, 0x2, 0xd1, 0xd3, 0x7, 
    0xd, 0x2, 0x2, 0xd2, 0xd4, 0x5, 0x1e, 0x10, 0x2, 0xd3, 0xd2, 0x3, 0x2, 
    0x2, 0x2, 0xd3, 0xd4, 0x3, 0x2, 0x2, 0x2, 0xd4, 0x2b, 0x3, 0x2, 0x2, 
    0x2, 0xd5, 0xdb, 0x5, 0x3c, 0x1f, 0x2, 0xd6, 0xdb, 0x5, 0x2e, 0x18, 
    0x2, 0xd7, 0xdb, 0x5, 0x30, 0x19, 0x2, 0xd8, 0xdb, 0x5, 0x32, 0x1a, 
    0x2, 0xd9, 0xdb, 0x5, 0x34, 0x1b, 0x2, 0xda, 0xd5, 0x3, 0x2, 0x2, 0x2, 
    0xda, 0xd6, 0x3, 0x2, 0x2, 0x2, 0xda, 0xd7, 0x3, 0x2, 0x2, 0x2, 0xda, 
    0xd8, 0x3, 0x2, 0x2, 0x2, 0xda, 0xd9, 0x3, 0x2, 0x2, 0x2, 0xdb, 0x2d, 
    0x3, 0x2, 0x2, 0x2, 0xdc, 0xdd, 0x5, 0x3c, 0x1f, 0x2, 0xdd, 0xde, 0x9, 
    0x4, 0x2, 0x2, 0xde, 0x2f, 0x3, 0x2, 0x2, 0x2, 0xdf, 0xe1, 0x9, 0x5, 
    0x2, 0x2, 0xe0, 0xdf, 0x3, 0x2, 0x2, 0x2, 0xe0, 0xe1, 0x3, 0x2, 0x2, 
    0x2, 0xe1, 0xe2, 0x3, 0x2, 0x2, 0x2, 0xe2, 0xe3, 0x7, 0x31, 0x2, 0x2, 
    0xe3, 0x31, 0x3, 0x2, 0x2, 0x2, 0xe4, 0xe5, 0x5, 0x1c, 0xf, 0x2, 0xe5, 
    0xe6, 0x7, 0x30, 0x2, 0x2, 0xe6, 0xe7, 0x5, 0x1e, 0x10, 0x2, 0xe7, 0x33, 
    0x3, 0x2, 0x2, 0x2, 0xe8, 0xe9, 0x5, 0xe, 0x8, 0x2, 0xe9, 0x35, 0x3, 
    0x2, 0x2, 0x2, 0xea, 0xeb, 0x7, 0x3, 0x2, 0x2, 0xeb, 0xec, 0x5, 0x38, 
    0x1d, 0x2, 0xec, 0xed, 0x7, 0x4, 0x2, 0x2, 0xed, 0x37, 0x3, 0x2, 0x2, 
    0x2, 0xee, 0xef, 0x5, 0x10, 0x9, 0x2, 0xef, 0xf0, 0x5, 0xe, 0x8, 0x2, 
    0xf0, 0x39, 0x3, 0x2, 0x2, 0x2, 0xf1, 0xf2, 0x3, 0x2, 0x2, 0x2, 0xf2, 
    0x3b, 0x3, 0x2, 0x2, 0x2, 0xf3, 0xf4, 0x8, 0x1f, 0x1, 0x2, 0xf4, 0xf5, 
    0x7, 0x49, 0x2, 0x2, 0xf5, 0xf6, 0x5, 0x3c, 0x1f, 0x2, 0xf6, 0xf7, 0x7, 
    0x4a, 0x2, 0x2, 0xf7, 0x103, 0x3, 0x2, 0x2, 0x2, 0xf8, 0xf9, 0xc, 0x6, 
    0x2, 0x2, 0xf9, 0xfa, 0x9, 0x6, 0x2, 0x2, 0xfa, 0x102, 0x5, 0x3c, 0x1f, 
    0x7, 0xfb, 0xfc, 0xc, 0x5, 0x2, 0x2, 0xfc, 0xfd, 0x9, 0x7, 0x2, 0x2, 
    0xfd, 0x102, 0x5, 0x3c, 0x1f, 0x6, 0xfe, 0xff, 0xc, 0x4, 0x2, 0x2, 0xff, 
    0x100, 0x7, 0x24, 0x2, 0x2, 0x100, 0x102, 0x5, 0x3e, 0x20, 0x2, 0x101, 
    0xf8, 0x3, 0x2, 0x2, 0x2, 0x101, 0xfb, 0x3, 0x2, 0x2, 0x2, 0x101, 0xfe, 
    0x3, 0x2, 0x2, 0x2, 0x102, 0x105, 0x3, 0x2, 0x2, 0x2, 0x103, 0x101, 
    0x3, 0x2, 0x2, 0x2, 0x103, 0x104, 0x3, 0x2, 0x2, 0x2, 0x104, 0x3d, 0x3, 
    0x2, 0x2, 0x2, 0x105, 0x103, 0x3, 0x2, 0x2, 0x2, 0x106, 0x107, 0x9, 
    0x8, 0x2, 0x2, 0x107, 0x3f, 0x3, 0x2, 0x2, 0x2, 0x1a, 0x47, 0x4f, 0x5d, 
    0x61, 0x67, 0x76, 0x7b, 0x96, 0x98, 0xa1, 0xa9, 0xb1, 0xb5, 0xb8, 0xbc, 
    0xc3, 0xc5, 0xca, 0xcf, 0xd3, 0xda, 0xe0, 0x101, 0x103, 
  };

  atn::ATNDeserializer deserializer;
  _atn = deserializer.deserialize(_serializedATN);

  size_t count = _atn.getNumberOfDecisions();
  _decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    _decisionToDFA.emplace_back(_atn.getDecisionState(i), i);
  }
}

JingleParser::Initializer JingleParser::_init;
