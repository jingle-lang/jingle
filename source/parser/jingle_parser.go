// Code generated from JingleParser.g4 by ANTLR 4.7.2. DO NOT EDIT.

package parser // JingleParser

import (
	"fmt"
	"reflect"
	"strconv"

	"github.com/antlr/antlr4/runtime/Go/antlr"
)

// Suppress unused import errors
var _ = fmt.Printf
var _ = reflect.Copy
var _ = strconv.Itoa

var parserATN = []uint16{
	3, 24715, 42794, 33075, 47597, 16764, 15335, 30598, 22884, 3, 108, 37,
	4, 2, 9, 2, 4, 3, 9, 3, 4, 4, 9, 4, 4, 5, 9, 5, 4, 6, 9, 6, 3, 2, 6, 2,
	14, 10, 2, 13, 2, 14, 2, 15, 3, 3, 3, 3, 3, 3, 3, 4, 3, 4, 3, 4, 5, 4,
	24, 10, 4, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6,
	3, 6, 3, 6, 2, 2, 7, 2, 4, 6, 8, 10, 2, 4, 3, 3, 3, 3, 4, 2, 86, 86, 100,
	100, 2, 34, 2, 13, 3, 2, 2, 2, 4, 17, 3, 2, 2, 2, 6, 23, 3, 2, 2, 2, 8,
	25, 3, 2, 2, 2, 10, 30, 3, 2, 2, 2, 12, 14, 5, 4, 3, 2, 13, 12, 3, 2, 2,
	2, 14, 15, 3, 2, 2, 2, 15, 13, 3, 2, 2, 2, 15, 16, 3, 2, 2, 2, 16, 3, 3,
	2, 2, 2, 17, 18, 5, 6, 4, 2, 18, 19, 9, 2, 2, 2, 19, 5, 3, 2, 2, 2, 20,
	24, 3, 2, 2, 2, 21, 24, 5, 8, 5, 2, 22, 24, 5, 10, 6, 2, 23, 20, 3, 2,
	2, 2, 23, 21, 3, 2, 2, 2, 23, 22, 3, 2, 2, 2, 24, 7, 3, 2, 2, 2, 25, 26,
	7, 6, 2, 2, 26, 27, 7, 100, 2, 2, 27, 28, 7, 45, 2, 2, 28, 29, 7, 86, 2,
	2, 29, 9, 3, 2, 2, 2, 30, 31, 7, 10, 2, 2, 31, 32, 7, 76, 2, 2, 32, 33,
	7, 69, 2, 2, 33, 34, 9, 3, 2, 2, 34, 35, 7, 70, 2, 2, 35, 11, 3, 2, 2,
	2, 4, 15, 23,
}
var deserializer = antlr.NewATNDeserializer(nil)
var deserializedATN = deserializer.DeserializeFromUInt16(parserATN)

var literalNames = []string{
	"", "", "", "", "'var'", "", "", "", "'display'", "'return'", "'if'", "'then'",
	"'and'", "'or'", "'in'", "'else'", "", "'while'", "'for'", "'true'", "'false'",
	"", "'class'", "'let'", "'bind'", "'trait'", "'def'", "'protocol'", "'enum'",
	"'import'", "'from'", "'package'", "'as'", "'break'", "'abstract'", "'select'",
	"'input'", "'each'", "'new'", "'continue'", "'export'", "'include'", "':='",
	"'='", "'=='", "'!='", "'<='", "'>='", "'+'", "'-'", "'*'", "'/'", "'<'",
	"'>'", "'!'", "'^'", "'%'", "'|'", "'||'", "'#'", "'&'", "'&&'", "", "",
	"", "", "','", "'('", "')'", "'{'", "", "'['", "']'", "'->'", "':'", "'.'",
	"'...'", "'++'", "'--'", "'float'", "'string'", "'bool'", "'null'", "'char'",
	"", "", "", "", "", "", "'\\\"'", "'\\\\'", "'\\n'", "'\\#'", "", "'#{'",
}
var symbolicNames = []string{
	"", "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", "VAR", "ARRAY",
	"CONST", "LOCAL", "DISPLAY", "RETURN", "IF", "THEN", "AND", "OR", "IN",
	"ELSE", "ELSEIF", "WHILE", "FOR", "TRUE", "FALSE", "FUNCTION", "CLASS",
	"LET", "BIND", "TRAIT", "DEFINE", "PROTOCOL", "ENUM", "IMPORT", "FROM",
	"PACKAGE", "AS", "BREAK", "ABSTRACT", "SELECT", "INPUT", "EACH", "NEW",
	"CONTINUE", "EXPORT", "INCLUDE", "ASSIGN", "EQUALS", "EQEQ", "NOTEQUAL",
	"LTEQUALS", "GTEQUALS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN",
	"GREATERTHAN", "BANG", "POWER", "MODULUS", "VERTICAL", "ORSYMBOL", "HASH",
	"AMBERSAND", "ANDSYMBOL", "TYPE_INT", "TYPE_DECIMAL", "TYPE_STRING", "TYPE_BOOLEAN",
	"COMMA", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET", "RSQRBRACKET",
	"ARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", "MINUSMINUS", "FLOAT",
	"STRING", "BOOLEAN", "NULL", "CHAR", "INT_LITERAL", "FLOAT_LITERAL", "COMMENT",
	"TERMINATOR", "STRING_OPEN", "UNMATCHED", "SCAPE_STRING_DELIMITER", "ESCAPE_SLASH",
	"ESCAPE_NEWLINE", "ESCAPE_SHARP", "STRING_CLOSE", "INTERPOLATION_OPEN",
	"STRING_CONTENT", "INTERPOLATION_CLOSE", "NOUNICODEID", "IDENTIFIER", "BINARY_OP",
	"INT_LIT", "FLOAT_LIT", "STRING_LIT", "RUNE_LIT", "LITTLE_U_VALUE", "BIG_U_VALUE",
}

var ruleNames = []string{
	"jingleFile", "line", "statement", "varDeclaration", "stmtDisplay",
}
var decisionToDFA = make([]*antlr.DFA, len(deserializedATN.DecisionToState))

func init() {
	for index, ds := range deserializedATN.DecisionToState {
		decisionToDFA[index] = antlr.NewDFA(ds, index)
	}
}

type JingleParser struct {
	*antlr.BaseParser
}

func NewJingleParser(input antlr.TokenStream) *JingleParser {
	this := new(JingleParser)

	this.BaseParser = antlr.NewBaseParser(input)

	this.Interpreter = antlr.NewParserATNSimulator(this, deserializedATN, decisionToDFA, antlr.NewPredictionContextCache())
	this.RuleNames = ruleNames
	this.LiteralNames = literalNames
	this.SymbolicNames = symbolicNames
	this.GrammarFileName = "JingleParser.g4"

	return this
}

// JingleParser tokens.
const (
	JingleParserEOF                    = antlr.TokenEOF
	JingleParserENDSTATEMENT           = 1
	JingleParserSEMICOLONTERMINATE     = 2
	JingleParserSPEECHMARKS            = 3
	JingleParserVAR                    = 4
	JingleParserARRAY                  = 5
	JingleParserCONST                  = 6
	JingleParserLOCAL                  = 7
	JingleParserDISPLAY                = 8
	JingleParserRETURN                 = 9
	JingleParserIF                     = 10
	JingleParserTHEN                   = 11
	JingleParserAND                    = 12
	JingleParserOR                     = 13
	JingleParserIN                     = 14
	JingleParserELSE                   = 15
	JingleParserELSEIF                 = 16
	JingleParserWHILE                  = 17
	JingleParserFOR                    = 18
	JingleParserTRUE                   = 19
	JingleParserFALSE                  = 20
	JingleParserFUNCTION               = 21
	JingleParserCLASS                  = 22
	JingleParserLET                    = 23
	JingleParserBIND                   = 24
	JingleParserTRAIT                  = 25
	JingleParserDEFINE                 = 26
	JingleParserPROTOCOL               = 27
	JingleParserENUM                   = 28
	JingleParserIMPORT                 = 29
	JingleParserFROM                   = 30
	JingleParserPACKAGE                = 31
	JingleParserAS                     = 32
	JingleParserBREAK                  = 33
	JingleParserABSTRACT               = 34
	JingleParserSELECT                 = 35
	JingleParserINPUT                  = 36
	JingleParserEACH                   = 37
	JingleParserNEW                    = 38
	JingleParserCONTINUE               = 39
	JingleParserEXPORT                 = 40
	JingleParserINCLUDE                = 41
	JingleParserASSIGN                 = 42
	JingleParserEQUALS                 = 43
	JingleParserEQEQ                   = 44
	JingleParserNOTEQUAL               = 45
	JingleParserLTEQUALS               = 46
	JingleParserGTEQUALS               = 47
	JingleParserPLUS                   = 48
	JingleParserMINUS                  = 49
	JingleParserMULTIPLY               = 50
	JingleParserDIVIDE                 = 51
	JingleParserLESSTHAN               = 52
	JingleParserGREATERTHAN            = 53
	JingleParserBANG                   = 54
	JingleParserPOWER                  = 55
	JingleParserMODULUS                = 56
	JingleParserVERTICAL               = 57
	JingleParserORSYMBOL               = 58
	JingleParserHASH                   = 59
	JingleParserAMBERSAND              = 60
	JingleParserANDSYMBOL              = 61
	JingleParserTYPE_INT               = 62
	JingleParserTYPE_DECIMAL           = 63
	JingleParserTYPE_STRING            = 64
	JingleParserTYPE_BOOLEAN           = 65
	JingleParserCOMMA                  = 66
	JingleParserLBRACKET               = 67
	JingleParserRBRACKET               = 68
	JingleParserLBRACE                 = 69
	JingleParserRBRACE                 = 70
	JingleParserLSQRBRACKET            = 71
	JingleParserRSQRBRACKET            = 72
	JingleParserARROW                  = 73
	JingleParserCOLON                  = 74
	JingleParserDOT                    = 75
	JingleParserELLIPSIS               = 76
	JingleParserPLUSPLUS               = 77
	JingleParserMINUSMINUS             = 78
	JingleParserFLOAT                  = 79
	JingleParserSTRING                 = 80
	JingleParserBOOLEAN                = 81
	JingleParserNULL                   = 82
	JingleParserCHAR                   = 83
	JingleParserINT_LITERAL            = 84
	JingleParserFLOAT_LITERAL          = 85
	JingleParserCOMMENT                = 86
	JingleParserTERMINATOR             = 87
	JingleParserSTRING_OPEN            = 88
	JingleParserUNMATCHED              = 89
	JingleParserSCAPE_STRING_DELIMITER = 90
	JingleParserESCAPE_SLASH           = 91
	JingleParserESCAPE_NEWLINE         = 92
	JingleParserESCAPE_SHARP           = 93
	JingleParserSTRING_CLOSE           = 94
	JingleParserINTERPOLATION_OPEN     = 95
	JingleParserSTRING_CONTENT         = 96
	JingleParserINTERPOLATION_CLOSE    = 97
	JingleParserNOUNICODEID            = 98
	JingleParserIDENTIFIER             = 99
	JingleParserBINARY_OP              = 100
	JingleParserINT_LIT                = 101
	JingleParserFLOAT_LIT              = 102
	JingleParserSTRING_LIT             = 103
	JingleParserRUNE_LIT               = 104
	JingleParserLITTLE_U_VALUE         = 105
	JingleParserBIG_U_VALUE            = 106
)

// JingleParser rules.
const (
	JingleParserRULE_jingleFile     = 0
	JingleParserRULE_line           = 1
	JingleParserRULE_statement      = 2
	JingleParserRULE_varDeclaration = 3
	JingleParserRULE_stmtDisplay    = 4
)

// IJingleFileContext is an interface to support dynamic dispatch.
type IJingleFileContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// GetLines returns the lines rule contexts.
	GetLines() ILineContext

	// SetLines sets the lines rule contexts.
	SetLines(ILineContext)

	// IsJingleFileContext differentiates from other interfaces.
	IsJingleFileContext()
}

type JingleFileContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
	lines  ILineContext
}

func NewEmptyJingleFileContext() *JingleFileContext {
	var p = new(JingleFileContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = JingleParserRULE_jingleFile
	return p
}

func (*JingleFileContext) IsJingleFileContext() {}

func NewJingleFileContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *JingleFileContext {
	var p = new(JingleFileContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = JingleParserRULE_jingleFile

	return p
}

func (s *JingleFileContext) GetParser() antlr.Parser { return s.parser }

func (s *JingleFileContext) GetLines() ILineContext { return s.lines }

func (s *JingleFileContext) SetLines(v ILineContext) { s.lines = v }

func (s *JingleFileContext) AllLine() []ILineContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*ILineContext)(nil)).Elem())
	var tst = make([]ILineContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(ILineContext)
		}
	}

	return tst
}

func (s *JingleFileContext) Line(i int) ILineContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*ILineContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(ILineContext)
}

func (s *JingleFileContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *JingleFileContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *JingleFileContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterJingleFile(s)
	}
}

func (s *JingleFileContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitJingleFile(s)
	}
}

func (s *JingleFileContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitJingleFile(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *JingleParser) JingleFile() (localctx IJingleFileContext) {
	localctx = NewJingleFileContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 0, JingleParserRULE_jingleFile)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	var _alt int

	p.EnterOuterAlt(localctx, 1)
	p.SetState(11)
	p.GetErrorHandler().Sync(p)
	_alt = 1
	for ok := true; ok; ok = _alt != 2 && _alt != antlr.ATNInvalidAltNumber {
		switch _alt {
		case 1:
			{
				p.SetState(10)

				var _x = p.Line()

				localctx.(*JingleFileContext).lines = _x
			}

		default:
			panic(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
		}

		p.SetState(13)
		p.GetErrorHandler().Sync(p)
		_alt = p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 0, p.GetParserRuleContext())
	}

	return localctx
}

// ILineContext is an interface to support dynamic dispatch.
type ILineContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsLineContext differentiates from other interfaces.
	IsLineContext()
}

type LineContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyLineContext() *LineContext {
	var p = new(LineContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = JingleParserRULE_line
	return p
}

func (*LineContext) IsLineContext() {}

func NewLineContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *LineContext {
	var p = new(LineContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = JingleParserRULE_line

	return p
}

func (s *LineContext) GetParser() antlr.Parser { return s.parser }

func (s *LineContext) Statement() IStatementContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IStatementContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IStatementContext)
}

func (s *LineContext) ENDSTATEMENT() antlr.TerminalNode {
	return s.GetToken(JingleParserENDSTATEMENT, 0)
}

func (s *LineContext) EOF() antlr.TerminalNode {
	return s.GetToken(JingleParserEOF, 0)
}

func (s *LineContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *LineContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *LineContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterLine(s)
	}
}

func (s *LineContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitLine(s)
	}
}

func (s *LineContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitLine(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *JingleParser) Line() (localctx ILineContext) {
	localctx = NewLineContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 2, JingleParserRULE_line)
	var _la int

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(15)
		p.Statement()
	}
	{
		p.SetState(16)
		_la = p.GetTokenStream().LA(1)

		if !(_la == JingleParserEOF || _la == JingleParserENDSTATEMENT) {
			p.GetErrorHandler().RecoverInline(p)
		} else {
			p.GetErrorHandler().ReportMatch(p)
			p.Consume()
		}
	}

	return localctx
}

// IStatementContext is an interface to support dynamic dispatch.
type IStatementContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsStatementContext differentiates from other interfaces.
	IsStatementContext()
}

type StatementContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyStatementContext() *StatementContext {
	var p = new(StatementContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = JingleParserRULE_statement
	return p
}

func (*StatementContext) IsStatementContext() {}

func NewStatementContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *StatementContext {
	var p = new(StatementContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = JingleParserRULE_statement

	return p
}

func (s *StatementContext) GetParser() antlr.Parser { return s.parser }

func (s *StatementContext) VarDeclaration() IVarDeclarationContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IVarDeclarationContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IVarDeclarationContext)
}

func (s *StatementContext) StmtDisplay() IStmtDisplayContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IStmtDisplayContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IStmtDisplayContext)
}

func (s *StatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *StatementContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *StatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterStatement(s)
	}
}

func (s *StatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitStatement(s)
	}
}

func (s *StatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *JingleParser) Statement() (localctx IStatementContext) {
	localctx = NewStatementContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 4, JingleParserRULE_statement)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.SetState(21)
	p.GetErrorHandler().Sync(p)

	switch p.GetTokenStream().LA(1) {
	case JingleParserEOF, JingleParserENDSTATEMENT:
		p.EnterOuterAlt(localctx, 1)

	case JingleParserVAR:
		p.EnterOuterAlt(localctx, 2)
		{
			p.SetState(19)
			p.VarDeclaration()
		}

	case JingleParserDISPLAY:
		p.EnterOuterAlt(localctx, 3)
		{
			p.SetState(20)
			p.StmtDisplay()
		}

	default:
		panic(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
	}

	return localctx
}

// IVarDeclarationContext is an interface to support dynamic dispatch.
type IVarDeclarationContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsVarDeclarationContext differentiates from other interfaces.
	IsVarDeclarationContext()
}

type VarDeclarationContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyVarDeclarationContext() *VarDeclarationContext {
	var p = new(VarDeclarationContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = JingleParserRULE_varDeclaration
	return p
}

func (*VarDeclarationContext) IsVarDeclarationContext() {}

func NewVarDeclarationContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *VarDeclarationContext {
	var p = new(VarDeclarationContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = JingleParserRULE_varDeclaration

	return p
}

func (s *VarDeclarationContext) GetParser() antlr.Parser { return s.parser }

func (s *VarDeclarationContext) VAR() antlr.TerminalNode {
	return s.GetToken(JingleParserVAR, 0)
}

func (s *VarDeclarationContext) NOUNICODEID() antlr.TerminalNode {
	return s.GetToken(JingleParserNOUNICODEID, 0)
}

func (s *VarDeclarationContext) EQUALS() antlr.TerminalNode {
	return s.GetToken(JingleParserEQUALS, 0)
}

func (s *VarDeclarationContext) INT_LITERAL() antlr.TerminalNode {
	return s.GetToken(JingleParserINT_LITERAL, 0)
}

func (s *VarDeclarationContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *VarDeclarationContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *VarDeclarationContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterVarDeclaration(s)
	}
}

func (s *VarDeclarationContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitVarDeclaration(s)
	}
}

func (s *VarDeclarationContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitVarDeclaration(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *JingleParser) VarDeclaration() (localctx IVarDeclarationContext) {
	localctx = NewVarDeclarationContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 6, JingleParserRULE_varDeclaration)

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(23)
		p.Match(JingleParserVAR)
	}
	{
		p.SetState(24)
		p.Match(JingleParserNOUNICODEID)
	}
	{
		p.SetState(25)
		p.Match(JingleParserEQUALS)
	}
	{
		p.SetState(26)
		p.Match(JingleParserINT_LITERAL)
	}

	return localctx
}

// IStmtDisplayContext is an interface to support dynamic dispatch.
type IStmtDisplayContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsStmtDisplayContext differentiates from other interfaces.
	IsStmtDisplayContext()
}

type StmtDisplayContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyStmtDisplayContext() *StmtDisplayContext {
	var p = new(StmtDisplayContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = JingleParserRULE_stmtDisplay
	return p
}

func (*StmtDisplayContext) IsStmtDisplayContext() {}

func NewStmtDisplayContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *StmtDisplayContext {
	var p = new(StmtDisplayContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = JingleParserRULE_stmtDisplay

	return p
}

func (s *StmtDisplayContext) GetParser() antlr.Parser { return s.parser }

func (s *StmtDisplayContext) DISPLAY() antlr.TerminalNode {
	return s.GetToken(JingleParserDISPLAY, 0)
}

func (s *StmtDisplayContext) COLON() antlr.TerminalNode {
	return s.GetToken(JingleParserCOLON, 0)
}

func (s *StmtDisplayContext) LBRACKET() antlr.TerminalNode {
	return s.GetToken(JingleParserLBRACKET, 0)
}

func (s *StmtDisplayContext) RBRACKET() antlr.TerminalNode {
	return s.GetToken(JingleParserRBRACKET, 0)
}

func (s *StmtDisplayContext) INT_LITERAL() antlr.TerminalNode {
	return s.GetToken(JingleParserINT_LITERAL, 0)
}

func (s *StmtDisplayContext) NOUNICODEID() antlr.TerminalNode {
	return s.GetToken(JingleParserNOUNICODEID, 0)
}

func (s *StmtDisplayContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *StmtDisplayContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *StmtDisplayContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterStmtDisplay(s)
	}
}

func (s *StmtDisplayContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitStmtDisplay(s)
	}
}

func (s *StmtDisplayContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitStmtDisplay(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *JingleParser) StmtDisplay() (localctx IStmtDisplayContext) {
	localctx = NewStmtDisplayContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 8, JingleParserRULE_stmtDisplay)
	var _la int

	defer func() {
		p.ExitRule()
	}()

	defer func() {
		if err := recover(); err != nil {
			if v, ok := err.(antlr.RecognitionException); ok {
				localctx.SetException(v)
				p.GetErrorHandler().ReportError(p, v)
				p.GetErrorHandler().Recover(p, v)
			} else {
				panic(err)
			}
		}
	}()

	p.EnterOuterAlt(localctx, 1)
	{
		p.SetState(28)
		p.Match(JingleParserDISPLAY)
	}
	{
		p.SetState(29)
		p.Match(JingleParserCOLON)
	}
	{
		p.SetState(30)
		p.Match(JingleParserLBRACKET)
	}
	{
		p.SetState(31)
		_la = p.GetTokenStream().LA(1)

		if !(_la == JingleParserINT_LITERAL || _la == JingleParserNOUNICODEID) {
			p.GetErrorHandler().RecoverInline(p)
		} else {
			p.GetErrorHandler().ReportMatch(p)
			p.Consume()
		}
	}
	{
		p.SetState(32)
		p.Match(JingleParserRBRACKET)
	}

	return localctx
}
