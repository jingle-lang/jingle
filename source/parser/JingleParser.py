# Generated from JingleParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3n")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\3\3\3\3\3\3\4\3\4\3\4\5\4\30\n\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\2\2\7\2\4")
        buf.write("\6\b\n\2\4\3\3\3\3\4\2XXff\2\"\2\r\3\2\2\2\4\21\3\2\2")
        buf.write("\2\6\27\3\2\2\2\b\31\3\2\2\2\n\36\3\2\2\2\f\16\5\4\3\2")
        buf.write("\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2")
        buf.write("\20\3\3\2\2\2\21\22\5\6\4\2\22\23\t\2\2\2\23\5\3\2\2\2")
        buf.write("\24\30\3\2\2\2\25\30\5\b\5\2\26\30\5\n\6\2\27\24\3\2\2")
        buf.write("\2\27\25\3\2\2\2\27\26\3\2\2\2\30\7\3\2\2\2\31\32\7\6")
        buf.write("\2\2\32\33\7f\2\2\33\34\7/\2\2\34\35\7X\2\2\35\t\3\2\2")
        buf.write("\2\36\37\7\n\2\2\37 \7N\2\2 !\7G\2\2!\"\t\3\2\2\"#\7H")
        buf.write("\2\2#\13\3\2\2\2\4\17\27")
        return buf.getvalue()


class JingleParser ( Parser ):

    grammarFileName = "JingleParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'var'", "<INVALID>", "<INVALID>", "<INVALID>", "'display'", 
                     "'return'", "'if'", "'then'", "'and'", "'or'", "'in'", 
                     "'else'", "<INVALID>", "'while'", "'for'", "'true'", 
                     "'false'", "<INVALID>", "'class'", "'let'", "'bind'", 
                     "'trait'", "'def'", "'protocol'", "'enum'", "'import'", 
                     "'from'", "'package'", "'as'", "'break'", "'abstract'", 
                     "'select'", "'input'", "'each'", "'new'", "'continue'", 
                     "'export'", "'include'", "'require'", "'summon'", "':='", 
                     "'='", "'=='", "'!='", "'<='", "'>='", "'+'", "'-'", 
                     "'*'", "'/'", "'<'", "'>'", "'!'", "'^'", "'%'", "'|'", 
                     "'||'", "'#'", "'&'", "'&&'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "'('", "')'", "'{'", 
                     "<INVALID>", "'['", "']'", "'->'", "':'", "'.'", "'...'", 
                     "'++'", "'--'", "'float'", "'string'", "'bool'", "'null'", 
                     "'char'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\\"'", "'\\\\'", "'\\n'", 
                     "'\\#'", "<INVALID>", "'#{'" ]

    symbolicNames = [ "<INVALID>", "ENDSTATEMENT", "SEMICOLONTERMINATE", 
                      "SPEECHMARKS", "VAR", "ARRAY", "CONST", "LOCAL", "DISPLAY", 
                      "RETURN", "IF", "THEN", "AND", "OR", "IN", "ELSE", 
                      "ELSEIF", "WHILE", "FOR", "TRUE", "FALSE", "FUNCTION", 
                      "CLASS", "LET", "BIND", "TRAIT", "DEFINE", "PROTOCOL", 
                      "ENUM", "IMPORT", "FROM", "PACKAGE", "AS", "BREAK", 
                      "ABSTRACT", "SELECT", "INPUT", "EACH", "NEW", "CONTINUE", 
                      "EXPORT", "INCLUDE", "REQUIRE", "SUMMON", "ASSIGN", 
                      "EQUALS", "EQEQ", "NOTEQUAL", "LTEQUALS", "GTEQUALS", 
                      "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", 
                      "GREATERTHAN", "BANG", "POWER", "MODULUS", "VERTICAL", 
                      "ORSYMBOL", "HASH", "AMBERSAND", "ANDSYMBOL", "TYPE_INT", 
                      "TYPE_DECIMAL", "TYPE_STRING", "TYPE_BOOLEAN", "COMMA", 
                      "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET", 
                      "RSQRBRACKET", "ARROW", "COLON", "DOT", "ELLIPSIS", 
                      "PLUSPLUS", "MINUSMINUS", "FLOAT", "STRING", "BOOLEAN", 
                      "NULL", "CHAR", "INT_LITERAL", "FLOAT_LITERAL", "COMMENT", 
                      "TERMINATOR", "STRING_OPEN", "UNMATCHED", "SCAPE_STRING_DELIMITER", 
                      "ESCAPE_SLASH", "ESCAPE_NEWLINE", "ESCAPE_SHARP", 
                      "STRING_CLOSE", "INTERPOLATION_OPEN", "STRING_CONTENT", 
                      "INTERPOLATION_CLOSE", "NOUNICODEID", "IDENTIFIER", 
                      "BINARY_OP", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "RUNE_LIT", "LITTLE_U_VALUE", "BIG_U_VALUE" ]

    RULE_jingleFile = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_varDeclaration = 3
    RULE_stmtDisplay = 4

    ruleNames =  [ "jingleFile", "line", "statement", "varDeclaration", 
                   "stmtDisplay" ]

    EOF = Token.EOF
    ENDSTATEMENT=1
    SEMICOLONTERMINATE=2
    SPEECHMARKS=3
    VAR=4
    ARRAY=5
    CONST=6
    LOCAL=7
    DISPLAY=8
    RETURN=9
    IF=10
    THEN=11
    AND=12
    OR=13
    IN=14
    ELSE=15
    ELSEIF=16
    WHILE=17
    FOR=18
    TRUE=19
    FALSE=20
    FUNCTION=21
    CLASS=22
    LET=23
    BIND=24
    TRAIT=25
    DEFINE=26
    PROTOCOL=27
    ENUM=28
    IMPORT=29
    FROM=30
    PACKAGE=31
    AS=32
    BREAK=33
    ABSTRACT=34
    SELECT=35
    INPUT=36
    EACH=37
    NEW=38
    CONTINUE=39
    EXPORT=40
    INCLUDE=41
    REQUIRE=42
    SUMMON=43
    ASSIGN=44
    EQUALS=45
    EQEQ=46
    NOTEQUAL=47
    LTEQUALS=48
    GTEQUALS=49
    PLUS=50
    MINUS=51
    MULTIPLY=52
    DIVIDE=53
    LESSTHAN=54
    GREATERTHAN=55
    BANG=56
    POWER=57
    MODULUS=58
    VERTICAL=59
    ORSYMBOL=60
    HASH=61
    AMBERSAND=62
    ANDSYMBOL=63
    TYPE_INT=64
    TYPE_DECIMAL=65
    TYPE_STRING=66
    TYPE_BOOLEAN=67
    COMMA=68
    LBRACKET=69
    RBRACKET=70
    LBRACE=71
    RBRACE=72
    LSQRBRACKET=73
    RSQRBRACKET=74
    ARROW=75
    COLON=76
    DOT=77
    ELLIPSIS=78
    PLUSPLUS=79
    MINUSMINUS=80
    FLOAT=81
    STRING=82
    BOOLEAN=83
    NULL=84
    CHAR=85
    INT_LITERAL=86
    FLOAT_LITERAL=87
    COMMENT=88
    TERMINATOR=89
    STRING_OPEN=90
    UNMATCHED=91
    SCAPE_STRING_DELIMITER=92
    ESCAPE_SLASH=93
    ESCAPE_NEWLINE=94
    ESCAPE_SHARP=95
    STRING_CLOSE=96
    INTERPOLATION_OPEN=97
    STRING_CONTENT=98
    INTERPOLATION_CLOSE=99
    NOUNICODEID=100
    IDENTIFIER=101
    BINARY_OP=102
    INT_LIT=103
    FLOAT_LIT=104
    STRING_LIT=105
    RUNE_LIT=106
    LITTLE_U_VALUE=107
    BIG_U_VALUE=108

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class JingleFileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lines = None # LineContext

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JingleParser.LineContext)
            else:
                return self.getTypedRuleContext(JingleParser.LineContext,i)


        def getRuleIndex(self):
            return JingleParser.RULE_jingleFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJingleFile" ):
                listener.enterJingleFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJingleFile" ):
                listener.exitJingleFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJingleFile" ):
                return visitor.visitJingleFile(self)
            else:
                return visitor.visitChildren(self)




    def jingleFile(self):

        localctx = JingleParser.JingleFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_jingleFile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 10
                    localctx.lines = self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 13 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(JingleParser.StatementContext,0)


        def ENDSTATEMENT(self):
            return self.getToken(JingleParser.ENDSTATEMENT, 0)

        def EOF(self):
            return self.getToken(JingleParser.EOF, 0)

        def getRuleIndex(self):
            return JingleParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = JingleParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.statement()
            self.state = 16
            _la = self._input.LA(1)
            if not(_la==JingleParser.EOF or _la==JingleParser.ENDSTATEMENT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self):
            return self.getTypedRuleContext(JingleParser.VarDeclarationContext,0)


        def stmtDisplay(self):
            return self.getTypedRuleContext(JingleParser.StmtDisplayContext,0)


        def getRuleIndex(self):
            return JingleParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = JingleParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JingleParser.EOF, JingleParser.ENDSTATEMENT]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [JingleParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.varDeclaration()
                pass
            elif token in [JingleParser.DISPLAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.stmtDisplay()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(JingleParser.VAR, 0)

        def NOUNICODEID(self):
            return self.getToken(JingleParser.NOUNICODEID, 0)

        def EQUALS(self):
            return self.getToken(JingleParser.EQUALS, 0)

        def INT_LITERAL(self):
            return self.getToken(JingleParser.INT_LITERAL, 0)

        def getRuleIndex(self):
            return JingleParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = JingleParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(JingleParser.VAR)
            self.state = 24
            self.match(JingleParser.NOUNICODEID)
            self.state = 25
            self.match(JingleParser.EQUALS)
            self.state = 26
            self.match(JingleParser.INT_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtDisplayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISPLAY(self):
            return self.getToken(JingleParser.DISPLAY, 0)

        def COLON(self):
            return self.getToken(JingleParser.COLON, 0)

        def LBRACKET(self):
            return self.getToken(JingleParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(JingleParser.RBRACKET, 0)

        def INT_LITERAL(self):
            return self.getToken(JingleParser.INT_LITERAL, 0)

        def NOUNICODEID(self):
            return self.getToken(JingleParser.NOUNICODEID, 0)

        def getRuleIndex(self):
            return JingleParser.RULE_stmtDisplay

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtDisplay" ):
                listener.enterStmtDisplay(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtDisplay" ):
                listener.exitStmtDisplay(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtDisplay" ):
                return visitor.visitStmtDisplay(self)
            else:
                return visitor.visitChildren(self)




    def stmtDisplay(self):

        localctx = JingleParser.StmtDisplayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmtDisplay)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(JingleParser.DISPLAY)
            self.state = 29
            self.match(JingleParser.COLON)
            self.state = 30
            self.match(JingleParser.LBRACKET)
            self.state = 31
            _la = self._input.LA(1)
            if not(_la==JingleParser.INT_LITERAL or _la==JingleParser.NOUNICODEID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 32
            self.match(JingleParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





