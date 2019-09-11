# Generated from JingleParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\5\4\36\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\66\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b")
        buf.write("A\n\b\f\b\16\bD\13\b\3\t\3\t\5\tH\n\t\3\t\2\3\16\n\2\4")
        buf.write("\6\b\n\f\16\20\2\5\3\3\3\3\3\2\"#\3\2 !\2L\2\23\3\2\2")
        buf.write("\2\4\27\3\2\2\2\6\35\3\2\2\2\b\37\3\2\2\2\n$\3\2\2\2\f")
        buf.write("\'\3\2\2\2\16\65\3\2\2\2\20G\3\2\2\2\22\24\5\4\3\2\23")
        buf.write("\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2")
        buf.write("\26\3\3\2\2\2\27\30\5\6\4\2\30\31\t\2\2\2\31\5\3\2\2\2")
        buf.write("\32\36\5\n\6\2\33\36\5\f\7\2\34\36\5\b\5\2\35\32\3\2\2")
        buf.write("\2\35\33\3\2\2\2\35\34\3\2\2\2\36\7\3\2\2\2\37 \7\t\2")
        buf.write("\2 !\7-\2\2!\"\5\16\b\2\"#\7.\2\2#\t\3\2\2\2$%\7\6\2\2")
        buf.write("%&\5\f\7\2&\13\3\2\2\2\'(\7:\2\2()\7\36\2\2)*\5\16\b\2")
        buf.write("*\r\3\2\2\2+,\b\b\1\2,-\7-\2\2-.\5\16\b\2./\7.\2\2/\66")
        buf.write("\3\2\2\2\60\66\7:\2\2\61\62\7!\2\2\62\66\5\16\b\5\63\66")
        buf.write("\79\2\2\64\66\7\64\2\2\65+\3\2\2\2\65\60\3\2\2\2\65\61")
        buf.write("\3\2\2\2\65\63\3\2\2\2\65\64\3\2\2\2\66B\3\2\2\2\678\f")
        buf.write("\n\2\289\t\3\2\29A\5\16\b\13:;\f\t\2\2;<\t\4\2\2<A\5\16")
        buf.write("\b\n=>\f\b\2\2>?\7\35\2\2?A\5\20\t\2@\67\3\2\2\2@:\3\2")
        buf.write("\2\2@=\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\17\3\2\2")
        buf.write("\2DB\3\2\2\2EH\79\2\2FH\7\64\2\2GE\3\2\2\2GF\3\2\2\2H")
        buf.write("\21\3\2\2\2\b\25\35\65@BG")
        return buf.getvalue()


class JingleParser ( Parser ):

    grammarFileName = "JingleParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'##'", "'\"'", "'var'", 
                     "'array'", "<INVALID>", "'display'", "'return'", "'if'", 
                     "'in'", "'else'", "'elif'", "'while'", "'for'", "'true'", 
                     "'false'", "<INVALID>", "'class'", "'let'", "'trait'", 
                     "'def'", "'protocol'", "'enum'", "'import'", "'from'", 
                     "'package'", "'as'", "':='", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'<'", "'>'", "'!='", "'!'", "'|'", "'=='", 
                     "'#'", "'&'", "','", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "'->'", "'float'", "'string'", "'bool'", "'null'", 
                     "'char'" ]

    symbolicNames = [ "<INVALID>", "ENDSTATEMENT", "COMMENT", "SPEECHMARKS", 
                      "VAR", "ARRAY", "CONST", "DISPLAY", "RETURN", "IF", 
                      "IN", "ELSE", "ELIF", "WHILE", "FOR", "TRUE", "FALSE", 
                      "FUNC", "CLASS", "LET", "TRAIT", "DEFINE", "PROTOCOL", 
                      "ENUM", "IMPORT", "FROM", "PACKAGE", "AS", "ASSIGN", 
                      "EQUALS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", 
                      "GREATERTHAN", "NOTEQUAL", "BANG", "OR", "EQEQ", "HASH", 
                      "AMBERSAND", "COMMA", "LBRACKET", "RBRACKET", "LBRACE", 
                      "RBRACE", "LSQRBRACKET", "RSQRBRACKET", "ARROW", "FLOAT", 
                      "STRING", "BOOLEAN", "NULL", "CHAR", "INT", "ID" ]

    RULE_jingleFile = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_display = 3
    RULE_varDeclaration = 4
    RULE_assignment = 5
    RULE_expression = 6
    RULE_dataType = 7

    ruleNames =  [ "jingleFile", "line", "statement", "display", "varDeclaration", 
                   "assignment", "expression", "dataType" ]

    EOF = Token.EOF
    ENDSTATEMENT=1
    COMMENT=2
    SPEECHMARKS=3
    VAR=4
    ARRAY=5
    CONST=6
    DISPLAY=7
    RETURN=8
    IF=9
    IN=10
    ELSE=11
    ELIF=12
    WHILE=13
    FOR=14
    TRUE=15
    FALSE=16
    FUNC=17
    CLASS=18
    LET=19
    TRAIT=20
    DEFINE=21
    PROTOCOL=22
    ENUM=23
    IMPORT=24
    FROM=25
    PACKAGE=26
    AS=27
    ASSIGN=28
    EQUALS=29
    PLUS=30
    MINUS=31
    MULTIPLY=32
    DIVIDE=33
    LESSTHAN=34
    GREATERTHAN=35
    NOTEQUAL=36
    BANG=37
    OR=38
    EQEQ=39
    HASH=40
    AMBERSAND=41
    COMMA=42
    LBRACKET=43
    RBRACKET=44
    LBRACE=45
    RBRACE=46
    LSQRBRACKET=47
    RSQRBRACKET=48
    ARROW=49
    FLOAT=50
    STRING=51
    BOOLEAN=52
    NULL=53
    CHAR=54
    INT=55
    ID=56

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




    def jingleFile(self):

        localctx = JingleParser.JingleFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_jingleFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                localctx.lines = self.line()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JingleParser.VAR) | (1 << JingleParser.DISPLAY) | (1 << JingleParser.ID))) != 0)):
                    break

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




    def line(self):

        localctx = JingleParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.statement()
            self.state = 22
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


        def getRuleIndex(self):
            return JingleParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(JingleParser.AssignmentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)


    class DisplayStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def display(self):
            return self.getTypedRuleContext(JingleParser.DisplayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayStatement" ):
                listener.enterDisplayStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayStatement" ):
                listener.exitDisplayStatement(self)


    class VarDeclarationStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varDeclaration(self):
            return self.getTypedRuleContext(JingleParser.VarDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclarationStatement" ):
                listener.enterVarDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclarationStatement" ):
                listener.exitVarDeclarationStatement(self)



    def statement(self):

        localctx = JingleParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JingleParser.VAR]:
                localctx = JingleParser.VarDeclarationStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.varDeclaration()
                pass
            elif token in [JingleParser.ID]:
                localctx = JingleParser.AssignmentStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.assignment()
                pass
            elif token in [JingleParser.DISPLAY]:
                localctx = JingleParser.DisplayStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.display()
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


    class DisplayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISPLAY(self):
            return self.getToken(JingleParser.DISPLAY, 0)

        def LBRACKET(self):
            return self.getToken(JingleParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(JingleParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(JingleParser.RBRACKET, 0)

        def getRuleIndex(self):
            return JingleParser.RULE_display

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplay" ):
                listener.enterDisplay(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplay" ):
                listener.exitDisplay(self)




    def display(self):

        localctx = JingleParser.DisplayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_display)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(JingleParser.DISPLAY)
            self.state = 30
            self.match(JingleParser.LBRACKET)
            self.state = 31
            self.expression(0)
            self.state = 32
            self.match(JingleParser.RBRACKET)
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

        def assignment(self):
            return self.getTypedRuleContext(JingleParser.AssignmentContext,0)


        def getRuleIndex(self):
            return JingleParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)




    def varDeclaration(self):

        localctx = JingleParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(JingleParser.VAR)
            self.state = 35
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JingleParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(JingleParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(JingleParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JingleParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = JingleParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(JingleParser.ID)
            self.state = 38
            self.match(JingleParser.ASSIGN)
            self.state = 39
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JingleParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DecimalLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(JingleParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimalLiteral" ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimalLiteral" ):
                listener.exitDecimalLiteral(self)


    class MinusExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(JingleParser.MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(JingleParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinusExpression" ):
                listener.enterMinusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinusExpression" ):
                listener.exitMinusExpression(self)


    class IntLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(JingleParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)


    class ParenExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACKET(self):
            return self.getToken(JingleParser.LBRACKET, 0)
        def expression(self):
            return self.getTypedRuleContext(JingleParser.ExpressionContext,0)

        def RBRACKET(self):
            return self.getToken(JingleParser.RBRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpression" ):
                listener.enterParenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpression" ):
                listener.exitParenExpression(self)


    class BinaryOperationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.operator = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JingleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JingleParser.ExpressionContext,i)

        def DIVIDE(self):
            return self.getToken(JingleParser.DIVIDE, 0)
        def MULTIPLY(self):
            return self.getToken(JingleParser.MULTIPLY, 0)
        def PLUS(self):
            return self.getToken(JingleParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(JingleParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOperation" ):
                listener.enterBinaryOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOperation" ):
                listener.exitBinaryOperation(self)


    class TypeConversionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.ExpressionContext
            super().__init__(parser)
            self.value = None # ExpressionContext
            self.targetType = None # DataTypeContext
            self.copyFrom(ctx)

        def AS(self):
            return self.getToken(JingleParser.AS, 0)
        def expression(self):
            return self.getTypedRuleContext(JingleParser.ExpressionContext,0)

        def dataType(self):
            return self.getTypedRuleContext(JingleParser.DataTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeConversion" ):
                listener.enterTypeConversion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeConversion" ):
                listener.exitTypeConversion(self)


    class VarReferenceContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JingleParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarReference" ):
                listener.enterVarReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarReference" ):
                listener.exitVarReference(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = JingleParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JingleParser.LBRACKET]:
                localctx = JingleParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 42
                self.match(JingleParser.LBRACKET)
                self.state = 43
                self.expression(0)
                self.state = 44
                self.match(JingleParser.RBRACKET)
                pass
            elif token in [JingleParser.ID]:
                localctx = JingleParser.VarReferenceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(JingleParser.ID)
                pass
            elif token in [JingleParser.MINUS]:
                localctx = JingleParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(JingleParser.MINUS)
                self.state = 48
                self.expression(3)
                pass
            elif token in [JingleParser.INT]:
                localctx = JingleParser.IntLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(JingleParser.INT)
                pass
            elif token in [JingleParser.FLOAT]:
                localctx = JingleParser.DecimalLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(JingleParser.FLOAT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 62
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = JingleParser.BinaryOperationContext(self, JingleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 53
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 54
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==JingleParser.MULTIPLY or _la==JingleParser.DIVIDE):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = JingleParser.BinaryOperationContext(self, JingleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 56
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 57
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==JingleParser.PLUS or _la==JingleParser.MINUS):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 58
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = JingleParser.TypeConversionContext(self, JingleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.value = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 59
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 60
                        self.match(JingleParser.AS)
                        self.state = 61
                        localctx.targetType = self.dataType()
                        pass

             
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DataTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JingleParser.RULE_dataType

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerContext(DataTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.DataTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(JingleParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)


    class DecimalContext(DataTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.DataTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(JingleParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimal" ):
                listener.enterDecimal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimal" ):
                listener.exitDecimal(self)



    def dataType(self):

        localctx = JingleParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dataType)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JingleParser.INT]:
                localctx = JingleParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(JingleParser.INT)
                pass
            elif token in [JingleParser.FLOAT]:
                localctx = JingleParser.DecimalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(JingleParser.FLOAT)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




