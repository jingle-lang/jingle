// Code generated from JingleParser.g4 by ANTLR 4.7.2. DO NOT EDIT.

package parser // JingleParser

import "github.com/antlr/antlr4/runtime/Go/antlr"

// BaseJingleParserListener is a complete listener for a parse tree produced by JingleParser.
type BaseJingleParserListener struct{}

var _ JingleParserListener = &BaseJingleParserListener{}

// VisitTerminal is called when a terminal node is visited.
func (s *BaseJingleParserListener) VisitTerminal(node antlr.TerminalNode) {}

// VisitErrorNode is called when an error node is visited.
func (s *BaseJingleParserListener) VisitErrorNode(node antlr.ErrorNode) {}

// EnterEveryRule is called when any rule is entered.
func (s *BaseJingleParserListener) EnterEveryRule(ctx antlr.ParserRuleContext) {}

// ExitEveryRule is called when any rule is exited.
func (s *BaseJingleParserListener) ExitEveryRule(ctx antlr.ParserRuleContext) {}

// EnterJingleFile is called when production jingleFile is entered.
func (s *BaseJingleParserListener) EnterJingleFile(ctx *JingleFileContext) {}

// ExitJingleFile is called when production jingleFile is exited.
func (s *BaseJingleParserListener) ExitJingleFile(ctx *JingleFileContext) {}

// EnterLine is called when production line is entered.
func (s *BaseJingleParserListener) EnterLine(ctx *LineContext) {}

// ExitLine is called when production line is exited.
func (s *BaseJingleParserListener) ExitLine(ctx *LineContext) {}

// EnterStatement is called when production statement is entered.
func (s *BaseJingleParserListener) EnterStatement(ctx *StatementContext) {}

// ExitStatement is called when production statement is exited.
func (s *BaseJingleParserListener) ExitStatement(ctx *StatementContext) {}

// EnterVarDeclaration is called when production varDeclaration is entered.
func (s *BaseJingleParserListener) EnterVarDeclaration(ctx *VarDeclarationContext) {}

// ExitVarDeclaration is called when production varDeclaration is exited.
func (s *BaseJingleParserListener) ExitVarDeclaration(ctx *VarDeclarationContext) {}

// EnterStmtDisplay is called when production stmtDisplay is entered.
func (s *BaseJingleParserListener) EnterStmtDisplay(ctx *StmtDisplayContext) {}

// ExitStmtDisplay is called when production stmtDisplay is exited.
func (s *BaseJingleParserListener) ExitStmtDisplay(ctx *StmtDisplayContext) {}
