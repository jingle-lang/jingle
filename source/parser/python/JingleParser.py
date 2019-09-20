# Generated from JingleParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

if __name__ is not None and "." in __name__:
    from .JingleBaseParser import JingleBaseParser
else:
    from JingleBaseParser import JingleBaseParser


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3X")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\5\4\36\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b8\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\7\bC\n\b\f\b\16\bF\13\b\3\t\3\t\5\tJ\n\t\3\t\2\3\16")
        buf.write("\n\2\4\6\b\n\f\16\20\2\5\3\3\3\3\3\2,-\3\2*+\2N\2\23\3")
        buf.write("\2\2\2\4\27\3\2\2\2\6\35\3\2\2\2\b\37\3\2\2\2\n&\3\2\2")
        buf.write("\2\f)\3\2\2\2\16\67\3\2\2\2\20I\3\2\2\2\22\24\5\4\3\2")
        buf.write("\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2")
        buf.write("\2\26\3\3\2\2\2\27\30\5\6\4\2\30\31\t\2\2\2\31\5\3\2\2")
        buf.write("\2\32\36\5\n\6\2\33\36\5\f\7\2\34\36\5\b\5\2\35\32\3\2")
        buf.write("\2\2\35\33\3\2\2\2\35\34\3\2\2\2\36\7\3\2\2\2\37 \7\t")
        buf.write("\2\2 !\7@\2\2!\"\7U\2\2\"#\79\2\2#$\5\16\b\2$%\7:\2\2")
        buf.write("%\t\3\2\2\2&\'\7\6\2\2\'(\5\f\7\2(\13\3\2\2\2)*\7V\2\2")
        buf.write("*+\7$\2\2+,\5\16\b\2,\r\3\2\2\2-.\b\b\1\2./\79\2\2/\60")
        buf.write("\5\16\b\2\60\61\7:\2\2\618\3\2\2\2\628\7V\2\2\63\64\7")
        buf.write("+\2\2\648\5\16\b\5\658\7W\2\2\668\7X\2\2\67-\3\2\2\2\67")
        buf.write("\62\3\2\2\2\67\63\3\2\2\2\67\65\3\2\2\2\67\66\3\2\2\2")
        buf.write("8D\3\2\2\29:\f\n\2\2:;\t\3\2\2;C\5\16\b\13<=\f\t\2\2=")
        buf.write(">\t\4\2\2>C\5\16\b\n?@\f\b\2\2@A\7 \2\2AC\5\20\t\2B9\3")
        buf.write("\2\2\2B<\3\2\2\2B?\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2")
        buf.write("\2E\17\3\2\2\2FD\3\2\2\2GJ\7W\2\2HJ\7X\2\2IG\3\2\2\2I")
        buf.write("H\3\2\2\2J\21\3\2\2\2\b\25\35\67BDI")
        return buf.getvalue()


class JingleParser ( JingleBaseParser ):

    grammarFileName = "JingleParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'\"'", "'var'", 
                     "'array'", "<INVALID>", "'display'", "'return'", "'if'", 
                     "'then'", "'and'", "'or'", "'in'", "'else'", "'elif'", 
                     "'while'", "'for'", "'true'", "'false'", "<INVALID>", 
                     "'class'", "'let'", "'trait'", "'def'", "'protocol'", 
                     "'enum'", "'import'", "'from'", "'package'", "'as'", 
                     "'break'", "'abstract'", "'select'", "':='", "'='", 
                     "'=='", "'!='", "'<='", "'>='", "'+'", "'-'", "'*'", 
                     "'/'", "'<'", "'>'", "'!'", "'^'", "'%'", "'|'", "'||'", 
                     "'#'", "'&'", "'&&'", "','", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "'->'", "':'", "'.'", "'...'", "'++'", 
                     "'--'", "'float'", "'string'", "'bool'", "'null'", 
                     "'char'" ]

    symbolicNames = [ "<INVALID>", "ENDSTATEMENT", "SEMICOLONTERMINATE", 
                      "SPEECHMARKS", "VAR", "ARRAY", "CONST", "DISPLAY", 
                      "RETURN", "IF", "THEN", "AND", "OR", "IN", "ELSE", 
                      "ELIF", "WHILE", "FOR", "TRUE", "FALSE", "FUNC", "CLASS", 
                      "LET", "TRAIT", "DEFINE", "PROTOCOL", "ENUM", "IMPORT", 
                      "FROM", "PACKAGE", "AS", "BREAK", "ABSTRACT", "SELECT", 
                      "ASSIGN", "EQUALS", "EQEQ", "NOTEQUAL", "LTEQUALS", 
                      "GTEQUALS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                      "LESSTHAN", "GREATERTHAN", "BANG", "POWER", "MODULUS", 
                      "VERTICAL", "ORSYMBOL", "HASH", "AMBERSAND", "ANDSYMBOL", 
                      "COMMA", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", 
                      "LSQRBRACKET", "RSQRBRACKET", "ARROW", "COLON", "DOT", 
                      "ELLIPSIS", "PLUSPLUS", "MINUSMINUS", "FLOAT", "STRING", 
                      "BOOLEAN", "NULL", "CHAR", "INT", "COMMENT", "TERMINATOR", 
                      "IDENTIFIER", "BINARY_OP", "INT_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "RUNE_LIT", "LITTLE_U_VALUE", "BIG_U_VALUE", 
                      "WHITESPACE", "NOUNICODEID", "INT_TYPE", "FLOAT_TYPE" ]

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
    SEMICOLONTERMINATE=2
    SPEECHMARKS=3
    VAR=4
    ARRAY=5
    CONST=6
    DISPLAY=7
    RETURN=8
    IF=9
    THEN=10
    AND=11
    OR=12
    IN=13
    ELSE=14
    ELIF=15
    WHILE=16
    FOR=17
    TRUE=18
    FALSE=19
    FUNC=20
    CLASS=21
    LET=22
    TRAIT=23
    DEFINE=24
    PROTOCOL=25
    ENUM=26
    IMPORT=27
    FROM=28
    PACKAGE=29
    AS=30
    BREAK=31
    ABSTRACT=32
    SELECT=33
    ASSIGN=34
    EQUALS=35
    EQEQ=36
    NOTEQUAL=37
    LTEQUALS=38
    GTEQUALS=39
    PLUS=40
    MINUS=41
    MULTIPLY=42
    DIVIDE=43
    LESSTHAN=44
    GREATERTHAN=45
    BANG=46
    POWER=47
    MODULUS=48
    VERTICAL=49
    ORSYMBOL=50
    HASH=51
    AMBERSAND=52
    ANDSYMBOL=53
    COMMA=54
    LBRACKET=55
    RBRACKET=56
    LBRACE=57
    RBRACE=58
    LSQRBRACKET=59
    RSQRBRACKET=60
    ARROW=61
    COLON=62
    DOT=63
    ELLIPSIS=64
    PLUSPLUS=65
    MINUSMINUS=66
    FLOAT=67
    STRING=68
    BOOLEAN=69
    NULL=70
    CHAR=71
    INT=72
    COMMENT=73
    TERMINATOR=74
    IDENTIFIER=75
    BINARY_OP=76
    INT_LIT=77
    FLOAT_LIT=78
    STRING_LIT=79
    RUNE_LIT=80
    LITTLE_U_VALUE=81
    BIG_U_VALUE=82
    WHITESPACE=83
    NOUNICODEID=84
    INT_TYPE=85
    FLOAT_TYPE=86

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
                if not (_la==JingleParser.VAR or _la==JingleParser.DISPLAY or _la==JingleParser.NOUNICODEID):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplayStatement" ):
                return visitor.visitDisplayStatement(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclarationStatement" ):
                return visitor.visitVarDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)



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
            elif token in [JingleParser.NOUNICODEID]:
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

        def COLON(self):
            return self.getToken(JingleParser.COLON, 0)

        def WHITESPACE(self):
            return self.getToken(JingleParser.WHITESPACE, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplay" ):
                return visitor.visitDisplay(self)
            else:
                return visitor.visitChildren(self)




    def display(self):

        localctx = JingleParser.DisplayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_display)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(JingleParser.DISPLAY)
            self.state = 30
            self.match(JingleParser.COLON)
            self.state = 31
            self.match(JingleParser.WHITESPACE)
            self.state = 32
            self.match(JingleParser.LBRACKET)
            self.state = 33
            self.expression(0)
            self.state = 34
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = JingleParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(JingleParser.VAR)
            self.state = 37
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

        def NOUNICODEID(self):
            return self.getToken(JingleParser.NOUNICODEID, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = JingleParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(JingleParser.NOUNICODEID)
            self.state = 40
            self.match(JingleParser.ASSIGN)
            self.state = 41
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

        def FLOAT_TYPE(self):
            return self.getToken(JingleParser.FLOAT_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimalLiteral" ):
                listener.enterDecimalLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimalLiteral" ):
                listener.exitDecimalLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecimalLiteral" ):
                return visitor.visitDecimalLiteral(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinusExpression" ):
                return visitor.visitMinusExpression(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_TYPE(self):
            return self.getToken(JingleParser.INT_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpression" ):
                return visitor.visitParenExpression(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOperation" ):
                return visitor.visitBinaryOperation(self)
            else:
                return visitor.visitChildren(self)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeConversion" ):
                return visitor.visitTypeConversion(self)
            else:
                return visitor.visitChildren(self)


    class VarReferenceContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOUNICODEID(self):
            return self.getToken(JingleParser.NOUNICODEID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarReference" ):
                listener.enterVarReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarReference" ):
                listener.exitVarReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarReference" ):
                return visitor.visitVarReference(self)
            else:
                return visitor.visitChildren(self)



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
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JingleParser.LBRACKET]:
                localctx = JingleParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 44
                self.match(JingleParser.LBRACKET)
                self.state = 45
                self.expression(0)
                self.state = 46
                self.match(JingleParser.RBRACKET)
                pass
            elif token in [JingleParser.NOUNICODEID]:
                localctx = JingleParser.VarReferenceContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(JingleParser.NOUNICODEID)
                pass
            elif token in [JingleParser.MINUS]:
                localctx = JingleParser.MinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(JingleParser.MINUS)
                self.state = 50
                self.expression(3)
                pass
            elif token in [JingleParser.INT_TYPE]:
                localctx = JingleParser.IntLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(JingleParser.INT_TYPE)
                pass
            elif token in [JingleParser.FLOAT_TYPE]:
                localctx = JingleParser.DecimalLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(JingleParser.FLOAT_TYPE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = JingleParser.BinaryOperationContext(self, JingleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 55
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 56
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==JingleParser.MULTIPLY or _la==JingleParser.DIVIDE):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        localctx.right = self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = JingleParser.BinaryOperationContext(self, JingleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 58
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 59
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==JingleParser.PLUS or _la==JingleParser.MINUS):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        localctx.right = self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = JingleParser.TypeConversionContext(self, JingleParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.value = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 61
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 62
                        self.match(JingleParser.AS)
                        self.state = 63
                        localctx.targetType = self.dataType()
                        pass

             
                self.state = 68
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

        def INT_TYPE(self):
            return self.getToken(JingleParser.INT_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class DecimalContext(DataTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JingleParser.DataTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_TYPE(self):
            return self.getToken(JingleParser.FLOAT_TYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimal" ):
                listener.enterDecimal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimal" ):
                listener.exitDecimal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecimal" ):
                return visitor.visitDecimal(self)
            else:
                return visitor.visitChildren(self)



    def dataType(self):

        localctx = JingleParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dataType)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JingleParser.INT_TYPE]:
                localctx = JingleParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(JingleParser.INT_TYPE)
                pass
            elif token in [JingleParser.FLOAT_TYPE]:
                localctx = JingleParser.DecimalContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(JingleParser.FLOAT_TYPE)
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
         




