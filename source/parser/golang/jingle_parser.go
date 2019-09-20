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
	3, 24715, 42794, 33075, 47597, 16764, 15335, 30598, 22884, 3, 88, 76, 4,
	2, 9, 2, 4, 3, 9, 3, 4, 4, 9, 4, 4, 5, 9, 5, 4, 6, 9, 6, 4, 7, 9, 7, 4,
	8, 9, 8, 4, 9, 9, 9, 3, 2, 6, 2, 20, 10, 2, 13, 2, 14, 2, 21, 3, 3, 3,
	3, 3, 3, 3, 4, 3, 4, 3, 4, 5, 4, 30, 10, 4, 3, 5, 3, 5, 3, 5, 3, 5, 3,
	5, 3, 5, 3, 5, 3, 6, 3, 6, 3, 6, 3, 7, 3, 7, 3, 7, 3, 7, 3, 8, 3, 8, 3,
	8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 5, 8, 56, 10, 8, 3, 8, 3,
	8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 3, 8, 7, 8, 67, 10, 8, 12, 8, 14,
	8, 70, 11, 8, 3, 9, 3, 9, 5, 9, 74, 10, 9, 3, 9, 2, 3, 14, 10, 2, 4, 6,
	8, 10, 12, 14, 16, 2, 5, 3, 3, 3, 3, 3, 2, 44, 45, 3, 2, 42, 43, 2, 78,
	2, 19, 3, 2, 2, 2, 4, 23, 3, 2, 2, 2, 6, 29, 3, 2, 2, 2, 8, 31, 3, 2, 2,
	2, 10, 38, 3, 2, 2, 2, 12, 41, 3, 2, 2, 2, 14, 55, 3, 2, 2, 2, 16, 73,
	3, 2, 2, 2, 18, 20, 5, 4, 3, 2, 19, 18, 3, 2, 2, 2, 20, 21, 3, 2, 2, 2,
	21, 19, 3, 2, 2, 2, 21, 22, 3, 2, 2, 2, 22, 3, 3, 2, 2, 2, 23, 24, 5, 6,
	4, 2, 24, 25, 9, 2, 2, 2, 25, 5, 3, 2, 2, 2, 26, 30, 5, 10, 6, 2, 27, 30,
	5, 12, 7, 2, 28, 30, 5, 8, 5, 2, 29, 26, 3, 2, 2, 2, 29, 27, 3, 2, 2, 2,
	29, 28, 3, 2, 2, 2, 30, 7, 3, 2, 2, 2, 31, 32, 7, 9, 2, 2, 32, 33, 7, 64,
	2, 2, 33, 34, 7, 85, 2, 2, 34, 35, 7, 57, 2, 2, 35, 36, 5, 14, 8, 2, 36,
	37, 7, 58, 2, 2, 37, 9, 3, 2, 2, 2, 38, 39, 7, 6, 2, 2, 39, 40, 5, 12,
	7, 2, 40, 11, 3, 2, 2, 2, 41, 42, 7, 86, 2, 2, 42, 43, 7, 36, 2, 2, 43,
	44, 5, 14, 8, 2, 44, 13, 3, 2, 2, 2, 45, 46, 8, 8, 1, 2, 46, 47, 7, 57,
	2, 2, 47, 48, 5, 14, 8, 2, 48, 49, 7, 58, 2, 2, 49, 56, 3, 2, 2, 2, 50,
	56, 7, 86, 2, 2, 51, 52, 7, 43, 2, 2, 52, 56, 5, 14, 8, 5, 53, 56, 7, 87,
	2, 2, 54, 56, 7, 88, 2, 2, 55, 45, 3, 2, 2, 2, 55, 50, 3, 2, 2, 2, 55,
	51, 3, 2, 2, 2, 55, 53, 3, 2, 2, 2, 55, 54, 3, 2, 2, 2, 56, 68, 3, 2, 2,
	2, 57, 58, 12, 10, 2, 2, 58, 59, 9, 3, 2, 2, 59, 67, 5, 14, 8, 11, 60,
	61, 12, 9, 2, 2, 61, 62, 9, 4, 2, 2, 62, 67, 5, 14, 8, 10, 63, 64, 12,
	8, 2, 2, 64, 65, 7, 32, 2, 2, 65, 67, 5, 16, 9, 2, 66, 57, 3, 2, 2, 2,
	66, 60, 3, 2, 2, 2, 66, 63, 3, 2, 2, 2, 67, 70, 3, 2, 2, 2, 68, 66, 3,
	2, 2, 2, 68, 69, 3, 2, 2, 2, 69, 15, 3, 2, 2, 2, 70, 68, 3, 2, 2, 2, 71,
	74, 7, 87, 2, 2, 72, 74, 7, 88, 2, 2, 73, 71, 3, 2, 2, 2, 73, 72, 3, 2,
	2, 2, 74, 17, 3, 2, 2, 2, 8, 21, 29, 55, 66, 68, 73,
}
var deserializer = antlr.NewATNDeserializer(nil)
var deserializedATN = deserializer.DeserializeFromUInt16(parserATN)

var literalNames = []string{
	"", "", "", "'\"'", "'var'", "'array'", "", "'display'", "'return'", "'if'",
	"'then'", "'and'", "'or'", "'in'", "'else'", "'elif'", "'while'", "'for'",
	"'true'", "'false'", "", "'class'", "'let'", "'trait'", "'def'", "'protocol'",
	"'enum'", "'import'", "'from'", "'package'", "'as'", "'break'", "'abstract'",
	"'select'", "':='", "'='", "'=='", "'!='", "'<='", "'>='", "'+'", "'-'",
	"'*'", "'/'", "'<'", "'>'", "'!'", "'^'", "'%'", "'|'", "'||'", "'#'",
	"'&'", "'&&'", "','", "'('", "')'", "'{'", "'}'", "'['", "']'", "'->'",
	"':'", "'.'", "'...'", "'++'", "'--'", "'float'", "'string'", "'bool'",
	"'null'", "'char'",
}
var symbolicNames = []string{
	"", "ENDSTATEMENT", "SEMICOLONTERMINATE", "SPEECHMARKS", "VAR", "ARRAY",
	"CONST", "DISPLAY", "RETURN", "IF", "THEN", "AND", "OR", "IN", "ELSE",
	"ELIF", "WHILE", "FOR", "TRUE", "FALSE", "FUNC", "CLASS", "LET", "TRAIT",
	"DEFINE", "PROTOCOL", "ENUM", "IMPORT", "FROM", "PACKAGE", "AS", "BREAK",
	"ABSTRACT", "SELECT", "ASSIGN", "EQUALS", "EQEQ", "NOTEQUAL", "LTEQUALS",
	"GTEQUALS", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "LESSTHAN", "GREATERTHAN",
	"BANG", "POWER", "MODULUS", "VERTICAL", "ORSYMBOL", "HASH", "AMBERSAND",
	"ANDSYMBOL", "COMMA", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", "LSQRBRACKET",
	"RSQRBRACKET", "ARROW", "COLON", "DOT", "ELLIPSIS", "PLUSPLUS", "MINUSMINUS",
	"FLOAT", "STRING", "BOOLEAN", "NULL", "CHAR", "INT", "COMMENT", "TERMINATOR",
	"IDENTIFIER", "BINARY_OP", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "RUNE_LIT",
	"LITTLE_U_VALUE", "BIG_U_VALUE", "WHITESPACE", "NOUNICODEID", "INT_TYPE",
	"FLOAT_TYPE",
}

var ruleNames = []string{
	"jingleFile", "line", "statement", "display", "varDeclaration", "assignment",
	"expression", "dataType",
}
var decisionToDFA = make([]*antlr.DFA, len(deserializedATN.DecisionToState))

func init() {
	for index, ds := range deserializedATN.DecisionToState {
		decisionToDFA[index] = antlr.NewDFA(ds, index)
	}
}

type JingleParser struct {
	JingleBaseParser
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
	JingleParserEOF                = antlr.TokenEOF
	JingleParserENDSTATEMENT       = 1
	JingleParserSEMICOLONTERMINATE = 2
	JingleParserSPEECHMARKS        = 3
	JingleParserVAR                = 4
	JingleParserARRAY              = 5
	JingleParserCONST              = 6
	JingleParserDISPLAY            = 7
	JingleParserRETURN             = 8
	JingleParserIF                 = 9
	JingleParserTHEN               = 10
	JingleParserAND                = 11
	JingleParserOR                 = 12
	JingleParserIN                 = 13
	JingleParserELSE               = 14
	JingleParserELIF               = 15
	JingleParserWHILE              = 16
	JingleParserFOR                = 17
	JingleParserTRUE               = 18
	JingleParserFALSE              = 19
	JingleParserFUNC               = 20
	JingleParserCLASS              = 21
	JingleParserLET                = 22
	JingleParserTRAIT              = 23
	JingleParserDEFINE             = 24
	JingleParserPROTOCOL           = 25
	JingleParserENUM               = 26
	JingleParserIMPORT             = 27
	JingleParserFROM               = 28
	JingleParserPACKAGE            = 29
	JingleParserAS                 = 30
	JingleParserBREAK              = 31
	JingleParserABSTRACT           = 32
	JingleParserSELECT             = 33
	JingleParserASSIGN             = 34
	JingleParserEQUALS             = 35
	JingleParserEQEQ               = 36
	JingleParserNOTEQUAL           = 37
	JingleParserLTEQUALS           = 38
	JingleParserGTEQUALS           = 39
	JingleParserPLUS               = 40
	JingleParserMINUS              = 41
	JingleParserMULTIPLY           = 42
	JingleParserDIVIDE             = 43
	JingleParserLESSTHAN           = 44
	JingleParserGREATERTHAN        = 45
	JingleParserBANG               = 46
	JingleParserPOWER              = 47
	JingleParserMODULUS            = 48
	JingleParserVERTICAL           = 49
	JingleParserORSYMBOL           = 50
	JingleParserHASH               = 51
	JingleParserAMBERSAND          = 52
	JingleParserANDSYMBOL          = 53
	JingleParserCOMMA              = 54
	JingleParserLBRACKET           = 55
	JingleParserRBRACKET           = 56
	JingleParserLBRACE             = 57
	JingleParserRBRACE             = 58
	JingleParserLSQRBRACKET        = 59
	JingleParserRSQRBRACKET        = 60
	JingleParserARROW              = 61
	JingleParserCOLON              = 62
	JingleParserDOT                = 63
	JingleParserELLIPSIS           = 64
	JingleParserPLUSPLUS           = 65
	JingleParserMINUSMINUS         = 66
	JingleParserFLOAT              = 67
	JingleParserSTRING             = 68
	JingleParserBOOLEAN            = 69
	JingleParserNULL               = 70
	JingleParserCHAR               = 71
	JingleParserINT                = 72
	JingleParserCOMMENT            = 73
	JingleParserTERMINATOR         = 74
	JingleParserIDENTIFIER         = 75
	JingleParserBINARY_OP          = 76
	JingleParserINT_LIT            = 77
	JingleParserFLOAT_LIT          = 78
	JingleParserSTRING_LIT         = 79
	JingleParserRUNE_LIT           = 80
	JingleParserLITTLE_U_VALUE     = 81
	JingleParserBIG_U_VALUE        = 82
	JingleParserWHITESPACE         = 83
	JingleParserNOUNICODEID        = 84
	JingleParserINT_TYPE           = 85
	JingleParserFLOAT_TYPE         = 86
)

// JingleParser rules.
const (
	JingleParserRULE_jingleFile     = 0
	JingleParserRULE_line           = 1
	JingleParserRULE_statement      = 2
	JingleParserRULE_display        = 3
	JingleParserRULE_varDeclaration = 4
	JingleParserRULE_assignment     = 5
	JingleParserRULE_expression     = 6
	JingleParserRULE_dataType       = 7
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
	p.SetState(17)
	p.GetErrorHandler().Sync(p)
	_la = p.GetTokenStream().LA(1)

	for ok := true; ok; ok = _la == JingleParserVAR || _la == JingleParserDISPLAY || _la == JingleParserNOUNICODEID {
		{
			p.SetState(16)

			var _x = p.Line()

			localctx.(*JingleFileContext).lines = _x
		}

		p.SetState(19)
		p.GetErrorHandler().Sync(p)
		_la = p.GetTokenStream().LA(1)
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
		p.SetState(21)
		p.Statement()
	}
	{
		p.SetState(22)
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

func (s *StatementContext) CopyFrom(ctx *StatementContext) {
	s.BaseParserRuleContext.CopyFrom(ctx.BaseParserRuleContext)
}

func (s *StatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *StatementContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

type AssignmentStatementContext struct {
	*StatementContext
}

func NewAssignmentStatementContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *AssignmentStatementContext {
	var p = new(AssignmentStatementContext)

	p.StatementContext = NewEmptyStatementContext()
	p.parser = parser
	p.CopyFrom(ctx.(*StatementContext))

	return p
}

func (s *AssignmentStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *AssignmentStatementContext) Assignment() IAssignmentContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IAssignmentContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IAssignmentContext)
}

func (s *AssignmentStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterAssignmentStatement(s)
	}
}

func (s *AssignmentStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitAssignmentStatement(s)
	}
}

func (s *AssignmentStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitAssignmentStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

type DisplayStatementContext struct {
	*StatementContext
}

func NewDisplayStatementContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *DisplayStatementContext {
	var p = new(DisplayStatementContext)

	p.StatementContext = NewEmptyStatementContext()
	p.parser = parser
	p.CopyFrom(ctx.(*StatementContext))

	return p
}

func (s *DisplayStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *DisplayStatementContext) Display() IDisplayContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IDisplayContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IDisplayContext)
}

func (s *DisplayStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterDisplayStatement(s)
	}
}

func (s *DisplayStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitDisplayStatement(s)
	}
}

func (s *DisplayStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitDisplayStatement(s)

	default:
		return t.VisitChildren(s)
	}
}

type VarDeclarationStatementContext struct {
	*StatementContext
}

func NewVarDeclarationStatementContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *VarDeclarationStatementContext {
	var p = new(VarDeclarationStatementContext)

	p.StatementContext = NewEmptyStatementContext()
	p.parser = parser
	p.CopyFrom(ctx.(*StatementContext))

	return p
}

func (s *VarDeclarationStatementContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *VarDeclarationStatementContext) VarDeclaration() IVarDeclarationContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IVarDeclarationContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IVarDeclarationContext)
}

func (s *VarDeclarationStatementContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterVarDeclarationStatement(s)
	}
}

func (s *VarDeclarationStatementContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitVarDeclarationStatement(s)
	}
}

func (s *VarDeclarationStatementContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitVarDeclarationStatement(s)

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

	p.SetState(27)
	p.GetErrorHandler().Sync(p)

	switch p.GetTokenStream().LA(1) {
	case JingleParserVAR:
		localctx = NewVarDeclarationStatementContext(p, localctx)
		p.EnterOuterAlt(localctx, 1)
		{
			p.SetState(24)
			p.VarDeclaration()
		}

	case JingleParserNOUNICODEID:
		localctx = NewAssignmentStatementContext(p, localctx)
		p.EnterOuterAlt(localctx, 2)
		{
			p.SetState(25)
			p.Assignment()
		}

	case JingleParserDISPLAY:
		localctx = NewDisplayStatementContext(p, localctx)
		p.EnterOuterAlt(localctx, 3)
		{
			p.SetState(26)
			p.Display()
		}

	default:
		panic(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
	}

	return localctx
}

// IDisplayContext is an interface to support dynamic dispatch.
type IDisplayContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsDisplayContext differentiates from other interfaces.
	IsDisplayContext()
}

type DisplayContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyDisplayContext() *DisplayContext {
	var p = new(DisplayContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = JingleParserRULE_display
	return p
}

func (*DisplayContext) IsDisplayContext() {}

func NewDisplayContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *DisplayContext {
	var p = new(DisplayContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = JingleParserRULE_display

	return p
}

func (s *DisplayContext) GetParser() antlr.Parser { return s.parser }

func (s *DisplayContext) DISPLAY() antlr.TerminalNode {
	return s.GetToken(JingleParserDISPLAY, 0)
}

func (s *DisplayContext) COLON() antlr.TerminalNode {
	return s.GetToken(JingleParserCOLON, 0)
}

func (s *DisplayContext) WHITESPACE() antlr.TerminalNode {
	return s.GetToken(JingleParserWHITESPACE, 0)
}

func (s *DisplayContext) LBRACKET() antlr.TerminalNode {
	return s.GetToken(JingleParserLBRACKET, 0)
}

func (s *DisplayContext) Expression() IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *DisplayContext) RBRACKET() antlr.TerminalNode {
	return s.GetToken(JingleParserRBRACKET, 0)
}

func (s *DisplayContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *DisplayContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *DisplayContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterDisplay(s)
	}
}

func (s *DisplayContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitDisplay(s)
	}
}

func (s *DisplayContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitDisplay(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *JingleParser) Display() (localctx IDisplayContext) {
	localctx = NewDisplayContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 6, JingleParserRULE_display)

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
		p.SetState(29)
		p.Match(JingleParserDISPLAY)
	}
	{
		p.SetState(30)
		p.Match(JingleParserCOLON)
	}
	{
		p.SetState(31)
		p.Match(JingleParserWHITESPACE)
	}
	{
		p.SetState(32)
		p.Match(JingleParserLBRACKET)
	}
	{
		p.SetState(33)
		p.expression(0)
	}
	{
		p.SetState(34)
		p.Match(JingleParserRBRACKET)
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

func (s *VarDeclarationContext) Assignment() IAssignmentContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IAssignmentContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IAssignmentContext)
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
	p.EnterRule(localctx, 8, JingleParserRULE_varDeclaration)

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
		p.SetState(36)
		p.Match(JingleParserVAR)
	}
	{
		p.SetState(37)
		p.Assignment()
	}

	return localctx
}

// IAssignmentContext is an interface to support dynamic dispatch.
type IAssignmentContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsAssignmentContext differentiates from other interfaces.
	IsAssignmentContext()
}

type AssignmentContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyAssignmentContext() *AssignmentContext {
	var p = new(AssignmentContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = JingleParserRULE_assignment
	return p
}

func (*AssignmentContext) IsAssignmentContext() {}

func NewAssignmentContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *AssignmentContext {
	var p = new(AssignmentContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = JingleParserRULE_assignment

	return p
}

func (s *AssignmentContext) GetParser() antlr.Parser { return s.parser }

func (s *AssignmentContext) NOUNICODEID() antlr.TerminalNode {
	return s.GetToken(JingleParserNOUNICODEID, 0)
}

func (s *AssignmentContext) ASSIGN() antlr.TerminalNode {
	return s.GetToken(JingleParserASSIGN, 0)
}

func (s *AssignmentContext) Expression() IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *AssignmentContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *AssignmentContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

func (s *AssignmentContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterAssignment(s)
	}
}

func (s *AssignmentContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitAssignment(s)
	}
}

func (s *AssignmentContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitAssignment(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *JingleParser) Assignment() (localctx IAssignmentContext) {
	localctx = NewAssignmentContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 10, JingleParserRULE_assignment)

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
		p.SetState(39)
		p.Match(JingleParserNOUNICODEID)
	}
	{
		p.SetState(40)
		p.Match(JingleParserASSIGN)
	}
	{
		p.SetState(41)
		p.expression(0)
	}

	return localctx
}

// IExpressionContext is an interface to support dynamic dispatch.
type IExpressionContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsExpressionContext differentiates from other interfaces.
	IsExpressionContext()
}

type ExpressionContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyExpressionContext() *ExpressionContext {
	var p = new(ExpressionContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = JingleParserRULE_expression
	return p
}

func (*ExpressionContext) IsExpressionContext() {}

func NewExpressionContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *ExpressionContext {
	var p = new(ExpressionContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = JingleParserRULE_expression

	return p
}

func (s *ExpressionContext) GetParser() antlr.Parser { return s.parser }

func (s *ExpressionContext) CopyFrom(ctx *ExpressionContext) {
	s.BaseParserRuleContext.CopyFrom(ctx.BaseParserRuleContext)
}

func (s *ExpressionContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ExpressionContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

type DecimalLiteralContext struct {
	*ExpressionContext
}

func NewDecimalLiteralContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *DecimalLiteralContext {
	var p = new(DecimalLiteralContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *DecimalLiteralContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *DecimalLiteralContext) FLOAT_TYPE() antlr.TerminalNode {
	return s.GetToken(JingleParserFLOAT_TYPE, 0)
}

func (s *DecimalLiteralContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterDecimalLiteral(s)
	}
}

func (s *DecimalLiteralContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitDecimalLiteral(s)
	}
}

func (s *DecimalLiteralContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitDecimalLiteral(s)

	default:
		return t.VisitChildren(s)
	}
}

type MinusExpressionContext struct {
	*ExpressionContext
}

func NewMinusExpressionContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *MinusExpressionContext {
	var p = new(MinusExpressionContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *MinusExpressionContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *MinusExpressionContext) MINUS() antlr.TerminalNode {
	return s.GetToken(JingleParserMINUS, 0)
}

func (s *MinusExpressionContext) Expression() IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *MinusExpressionContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterMinusExpression(s)
	}
}

func (s *MinusExpressionContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitMinusExpression(s)
	}
}

func (s *MinusExpressionContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitMinusExpression(s)

	default:
		return t.VisitChildren(s)
	}
}

type IntLiteralContext struct {
	*ExpressionContext
}

func NewIntLiteralContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *IntLiteralContext {
	var p = new(IntLiteralContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *IntLiteralContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *IntLiteralContext) INT_TYPE() antlr.TerminalNode {
	return s.GetToken(JingleParserINT_TYPE, 0)
}

func (s *IntLiteralContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterIntLiteral(s)
	}
}

func (s *IntLiteralContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitIntLiteral(s)
	}
}

func (s *IntLiteralContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitIntLiteral(s)

	default:
		return t.VisitChildren(s)
	}
}

type ParenExpressionContext struct {
	*ExpressionContext
}

func NewParenExpressionContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *ParenExpressionContext {
	var p = new(ParenExpressionContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *ParenExpressionContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *ParenExpressionContext) LBRACKET() antlr.TerminalNode {
	return s.GetToken(JingleParserLBRACKET, 0)
}

func (s *ParenExpressionContext) Expression() IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *ParenExpressionContext) RBRACKET() antlr.TerminalNode {
	return s.GetToken(JingleParserRBRACKET, 0)
}

func (s *ParenExpressionContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterParenExpression(s)
	}
}

func (s *ParenExpressionContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitParenExpression(s)
	}
}

func (s *ParenExpressionContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitParenExpression(s)

	default:
		return t.VisitChildren(s)
	}
}

type BinaryOperationContext struct {
	*ExpressionContext
	left     IExpressionContext
	operator antlr.Token
	right    IExpressionContext
}

func NewBinaryOperationContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *BinaryOperationContext {
	var p = new(BinaryOperationContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *BinaryOperationContext) GetOperator() antlr.Token { return s.operator }

func (s *BinaryOperationContext) SetOperator(v antlr.Token) { s.operator = v }

func (s *BinaryOperationContext) GetLeft() IExpressionContext { return s.left }

func (s *BinaryOperationContext) GetRight() IExpressionContext { return s.right }

func (s *BinaryOperationContext) SetLeft(v IExpressionContext) { s.left = v }

func (s *BinaryOperationContext) SetRight(v IExpressionContext) { s.right = v }

func (s *BinaryOperationContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *BinaryOperationContext) AllExpression() []IExpressionContext {
	var ts = s.GetTypedRuleContexts(reflect.TypeOf((*IExpressionContext)(nil)).Elem())
	var tst = make([]IExpressionContext, len(ts))

	for i, t := range ts {
		if t != nil {
			tst[i] = t.(IExpressionContext)
		}
	}

	return tst
}

func (s *BinaryOperationContext) Expression(i int) IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), i)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *BinaryOperationContext) DIVIDE() antlr.TerminalNode {
	return s.GetToken(JingleParserDIVIDE, 0)
}

func (s *BinaryOperationContext) MULTIPLY() antlr.TerminalNode {
	return s.GetToken(JingleParserMULTIPLY, 0)
}

func (s *BinaryOperationContext) PLUS() antlr.TerminalNode {
	return s.GetToken(JingleParserPLUS, 0)
}

func (s *BinaryOperationContext) MINUS() antlr.TerminalNode {
	return s.GetToken(JingleParserMINUS, 0)
}

func (s *BinaryOperationContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterBinaryOperation(s)
	}
}

func (s *BinaryOperationContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitBinaryOperation(s)
	}
}

func (s *BinaryOperationContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitBinaryOperation(s)

	default:
		return t.VisitChildren(s)
	}
}

type TypeConversionContext struct {
	*ExpressionContext
	value      IExpressionContext
	targetType IDataTypeContext
}

func NewTypeConversionContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *TypeConversionContext {
	var p = new(TypeConversionContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *TypeConversionContext) GetValue() IExpressionContext { return s.value }

func (s *TypeConversionContext) GetTargetType() IDataTypeContext { return s.targetType }

func (s *TypeConversionContext) SetValue(v IExpressionContext) { s.value = v }

func (s *TypeConversionContext) SetTargetType(v IDataTypeContext) { s.targetType = v }

func (s *TypeConversionContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *TypeConversionContext) AS() antlr.TerminalNode {
	return s.GetToken(JingleParserAS, 0)
}

func (s *TypeConversionContext) Expression() IExpressionContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IExpressionContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IExpressionContext)
}

func (s *TypeConversionContext) DataType() IDataTypeContext {
	var t = s.GetTypedRuleContext(reflect.TypeOf((*IDataTypeContext)(nil)).Elem(), 0)

	if t == nil {
		return nil
	}

	return t.(IDataTypeContext)
}

func (s *TypeConversionContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterTypeConversion(s)
	}
}

func (s *TypeConversionContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitTypeConversion(s)
	}
}

func (s *TypeConversionContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitTypeConversion(s)

	default:
		return t.VisitChildren(s)
	}
}

type VarReferenceContext struct {
	*ExpressionContext
}

func NewVarReferenceContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *VarReferenceContext {
	var p = new(VarReferenceContext)

	p.ExpressionContext = NewEmptyExpressionContext()
	p.parser = parser
	p.CopyFrom(ctx.(*ExpressionContext))

	return p
}

func (s *VarReferenceContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *VarReferenceContext) NOUNICODEID() antlr.TerminalNode {
	return s.GetToken(JingleParserNOUNICODEID, 0)
}

func (s *VarReferenceContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterVarReference(s)
	}
}

func (s *VarReferenceContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitVarReference(s)
	}
}

func (s *VarReferenceContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitVarReference(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *JingleParser) Expression() (localctx IExpressionContext) {
	return p.expression(0)
}

func (p *JingleParser) expression(_p int) (localctx IExpressionContext) {
	var _parentctx antlr.ParserRuleContext = p.GetParserRuleContext()
	_parentState := p.GetState()
	localctx = NewExpressionContext(p, p.GetParserRuleContext(), _parentState)
	var _prevctx IExpressionContext = localctx
	var _ antlr.ParserRuleContext = _prevctx // TODO: To prevent unused variable warning.
	_startState := 12
	p.EnterRecursionRule(localctx, 12, JingleParserRULE_expression, _p)
	var _la int

	defer func() {
		p.UnrollRecursionContexts(_parentctx)
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
	p.SetState(53)
	p.GetErrorHandler().Sync(p)

	switch p.GetTokenStream().LA(1) {
	case JingleParserLBRACKET:
		localctx = NewParenExpressionContext(p, localctx)
		p.SetParserRuleContext(localctx)
		_prevctx = localctx

		{
			p.SetState(44)
			p.Match(JingleParserLBRACKET)
		}
		{
			p.SetState(45)
			p.expression(0)
		}
		{
			p.SetState(46)
			p.Match(JingleParserRBRACKET)
		}

	case JingleParserNOUNICODEID:
		localctx = NewVarReferenceContext(p, localctx)
		p.SetParserRuleContext(localctx)
		_prevctx = localctx
		{
			p.SetState(48)
			p.Match(JingleParserNOUNICODEID)
		}

	case JingleParserMINUS:
		localctx = NewMinusExpressionContext(p, localctx)
		p.SetParserRuleContext(localctx)
		_prevctx = localctx
		{
			p.SetState(49)
			p.Match(JingleParserMINUS)
		}
		{
			p.SetState(50)
			p.expression(3)
		}

	case JingleParserINT_TYPE:
		localctx = NewIntLiteralContext(p, localctx)
		p.SetParserRuleContext(localctx)
		_prevctx = localctx
		{
			p.SetState(51)
			p.Match(JingleParserINT_TYPE)
		}

	case JingleParserFLOAT_TYPE:
		localctx = NewDecimalLiteralContext(p, localctx)
		p.SetParserRuleContext(localctx)
		_prevctx = localctx
		{
			p.SetState(52)
			p.Match(JingleParserFLOAT_TYPE)
		}

	default:
		panic(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
	}
	p.GetParserRuleContext().SetStop(p.GetTokenStream().LT(-1))
	p.SetState(66)
	p.GetErrorHandler().Sync(p)
	_alt = p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 4, p.GetParserRuleContext())

	for _alt != 2 && _alt != antlr.ATNInvalidAltNumber {
		if _alt == 1 {
			if p.GetParseListeners() != nil {
				p.TriggerExitRuleEvent()
			}
			_prevctx = localctx
			p.SetState(64)
			p.GetErrorHandler().Sync(p)
			switch p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 3, p.GetParserRuleContext()) {
			case 1:
				localctx = NewBinaryOperationContext(p, NewExpressionContext(p, _parentctx, _parentState))
				localctx.(*BinaryOperationContext).left = _prevctx

				p.PushNewRecursionContext(localctx, _startState, JingleParserRULE_expression)
				p.SetState(55)

				if !(p.Precpred(p.GetParserRuleContext(), 8)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 8)", ""))
				}
				{
					p.SetState(56)

					var _lt = p.GetTokenStream().LT(1)

					localctx.(*BinaryOperationContext).operator = _lt

					_la = p.GetTokenStream().LA(1)

					if !(_la == JingleParserMULTIPLY || _la == JingleParserDIVIDE) {
						var _ri = p.GetErrorHandler().RecoverInline(p)

						localctx.(*BinaryOperationContext).operator = _ri
					} else {
						p.GetErrorHandler().ReportMatch(p)
						p.Consume()
					}
				}
				{
					p.SetState(57)

					var _x = p.expression(9)

					localctx.(*BinaryOperationContext).right = _x
				}

			case 2:
				localctx = NewBinaryOperationContext(p, NewExpressionContext(p, _parentctx, _parentState))
				localctx.(*BinaryOperationContext).left = _prevctx

				p.PushNewRecursionContext(localctx, _startState, JingleParserRULE_expression)
				p.SetState(58)

				if !(p.Precpred(p.GetParserRuleContext(), 7)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 7)", ""))
				}
				{
					p.SetState(59)

					var _lt = p.GetTokenStream().LT(1)

					localctx.(*BinaryOperationContext).operator = _lt

					_la = p.GetTokenStream().LA(1)

					if !(_la == JingleParserPLUS || _la == JingleParserMINUS) {
						var _ri = p.GetErrorHandler().RecoverInline(p)

						localctx.(*BinaryOperationContext).operator = _ri
					} else {
						p.GetErrorHandler().ReportMatch(p)
						p.Consume()
					}
				}
				{
					p.SetState(60)

					var _x = p.expression(8)

					localctx.(*BinaryOperationContext).right = _x
				}

			case 3:
				localctx = NewTypeConversionContext(p, NewExpressionContext(p, _parentctx, _parentState))
				localctx.(*TypeConversionContext).value = _prevctx

				p.PushNewRecursionContext(localctx, _startState, JingleParserRULE_expression)
				p.SetState(61)

				if !(p.Precpred(p.GetParserRuleContext(), 6)) {
					panic(antlr.NewFailedPredicateException(p, "p.Precpred(p.GetParserRuleContext(), 6)", ""))
				}
				{
					p.SetState(62)
					p.Match(JingleParserAS)
				}
				{
					p.SetState(63)

					var _x = p.DataType()

					localctx.(*TypeConversionContext).targetType = _x
				}

			}

		}
		p.SetState(68)
		p.GetErrorHandler().Sync(p)
		_alt = p.GetInterpreter().AdaptivePredict(p.GetTokenStream(), 4, p.GetParserRuleContext())
	}

	return localctx
}

// IDataTypeContext is an interface to support dynamic dispatch.
type IDataTypeContext interface {
	antlr.ParserRuleContext

	// GetParser returns the parser.
	GetParser() antlr.Parser

	// IsDataTypeContext differentiates from other interfaces.
	IsDataTypeContext()
}

type DataTypeContext struct {
	*antlr.BaseParserRuleContext
	parser antlr.Parser
}

func NewEmptyDataTypeContext() *DataTypeContext {
	var p = new(DataTypeContext)
	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(nil, -1)
	p.RuleIndex = JingleParserRULE_dataType
	return p
}

func (*DataTypeContext) IsDataTypeContext() {}

func NewDataTypeContext(parser antlr.Parser, parent antlr.ParserRuleContext, invokingState int) *DataTypeContext {
	var p = new(DataTypeContext)

	p.BaseParserRuleContext = antlr.NewBaseParserRuleContext(parent, invokingState)

	p.parser = parser
	p.RuleIndex = JingleParserRULE_dataType

	return p
}

func (s *DataTypeContext) GetParser() antlr.Parser { return s.parser }

func (s *DataTypeContext) CopyFrom(ctx *DataTypeContext) {
	s.BaseParserRuleContext.CopyFrom(ctx.BaseParserRuleContext)
}

func (s *DataTypeContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *DataTypeContext) ToStringTree(ruleNames []string, recog antlr.Recognizer) string {
	return antlr.TreesStringTree(s, ruleNames, recog)
}

type IntegerContext struct {
	*DataTypeContext
}

func NewIntegerContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *IntegerContext {
	var p = new(IntegerContext)

	p.DataTypeContext = NewEmptyDataTypeContext()
	p.parser = parser
	p.CopyFrom(ctx.(*DataTypeContext))

	return p
}

func (s *IntegerContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *IntegerContext) INT_TYPE() antlr.TerminalNode {
	return s.GetToken(JingleParserINT_TYPE, 0)
}

func (s *IntegerContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterInteger(s)
	}
}

func (s *IntegerContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitInteger(s)
	}
}

func (s *IntegerContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitInteger(s)

	default:
		return t.VisitChildren(s)
	}
}

type DecimalContext struct {
	*DataTypeContext
}

func NewDecimalContext(parser antlr.Parser, ctx antlr.ParserRuleContext) *DecimalContext {
	var p = new(DecimalContext)

	p.DataTypeContext = NewEmptyDataTypeContext()
	p.parser = parser
	p.CopyFrom(ctx.(*DataTypeContext))

	return p
}

func (s *DecimalContext) GetRuleContext() antlr.RuleContext {
	return s
}

func (s *DecimalContext) FLOAT_TYPE() antlr.TerminalNode {
	return s.GetToken(JingleParserFLOAT_TYPE, 0)
}

func (s *DecimalContext) EnterRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.EnterDecimal(s)
	}
}

func (s *DecimalContext) ExitRule(listener antlr.ParseTreeListener) {
	if listenerT, ok := listener.(JingleParserListener); ok {
		listenerT.ExitDecimal(s)
	}
}

func (s *DecimalContext) Accept(visitor antlr.ParseTreeVisitor) interface{} {
	switch t := visitor.(type) {
	case JingleParserVisitor:
		return t.VisitDecimal(s)

	default:
		return t.VisitChildren(s)
	}
}

func (p *JingleParser) DataType() (localctx IDataTypeContext) {
	localctx = NewDataTypeContext(p, p.GetParserRuleContext(), p.GetState())
	p.EnterRule(localctx, 14, JingleParserRULE_dataType)

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

	p.SetState(71)
	p.GetErrorHandler().Sync(p)

	switch p.GetTokenStream().LA(1) {
	case JingleParserINT_TYPE:
		localctx = NewIntegerContext(p, localctx)
		p.EnterOuterAlt(localctx, 1)
		{
			p.SetState(69)
			p.Match(JingleParserINT_TYPE)
		}

	case JingleParserFLOAT_TYPE:
		localctx = NewDecimalContext(p, localctx)
		p.EnterOuterAlt(localctx, 2)
		{
			p.SetState(70)
			p.Match(JingleParserFLOAT_TYPE)
		}

	default:
		panic(antlr.NewNoViableAltException(p, nil, nil, nil, nil, nil))
	}

	return localctx
}

func (p *JingleParser) Sempred(localctx antlr.RuleContext, ruleIndex, predIndex int) bool {
	switch ruleIndex {
	case 6:
		var t *ExpressionContext = nil
		if localctx != nil {
			t = localctx.(*ExpressionContext)
		}
		return p.Expression_Sempred(t, predIndex)

	default:
		panic("No predicate with index: " + fmt.Sprint(ruleIndex))
	}
}

func (p *JingleParser) Expression_Sempred(localctx antlr.RuleContext, predIndex int) bool {
	switch predIndex {
	case 0:
		return p.Precpred(p.GetParserRuleContext(), 8)

	case 1:
		return p.Precpred(p.GetParserRuleContext(), 7)

	case 2:
		return p.Precpred(p.GetParserRuleContext(), 6)

	default:
		panic("No predicate with index: " + fmt.Sprint(predIndex))
	}
}
