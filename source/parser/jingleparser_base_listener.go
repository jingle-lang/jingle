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

// EnterVarDeclarationStatement is called when production varDeclarationStatement is entered.
func (s *BaseJingleParserListener) EnterVarDeclarationStatement(ctx *VarDeclarationStatementContext) {}

// ExitVarDeclarationStatement is called when production varDeclarationStatement is exited.
func (s *BaseJingleParserListener) ExitVarDeclarationStatement(ctx *VarDeclarationStatementContext) {}

// EnterAssignmentStatement is called when production assignmentStatement is entered.
func (s *BaseJingleParserListener) EnterAssignmentStatement(ctx *AssignmentStatementContext) {}

// ExitAssignmentStatement is called when production assignmentStatement is exited.
func (s *BaseJingleParserListener) ExitAssignmentStatement(ctx *AssignmentStatementContext) {}

// EnterDisplayStatement is called when production displayStatement is entered.
func (s *BaseJingleParserListener) EnterDisplayStatement(ctx *DisplayStatementContext) {}

// ExitDisplayStatement is called when production displayStatement is exited.
func (s *BaseJingleParserListener) ExitDisplayStatement(ctx *DisplayStatementContext) {}

// EnterDisplay is called when production display is entered.
func (s *BaseJingleParserListener) EnterDisplay(ctx *DisplayContext) {}

// ExitDisplay is called when production display is exited.
func (s *BaseJingleParserListener) ExitDisplay(ctx *DisplayContext) {}

// EnterVarDeclaration is called when production varDeclaration is entered.
func (s *BaseJingleParserListener) EnterVarDeclaration(ctx *VarDeclarationContext) {}

// ExitVarDeclaration is called when production varDeclaration is exited.
func (s *BaseJingleParserListener) ExitVarDeclaration(ctx *VarDeclarationContext) {}

// EnterAssignment is called when production assignment is entered.
func (s *BaseJingleParserListener) EnterAssignment(ctx *AssignmentContext) {}

// ExitAssignment is called when production assignment is exited.
func (s *BaseJingleParserListener) ExitAssignment(ctx *AssignmentContext) {}

// EnterDecimalLiteral is called when production decimalLiteral is entered.
func (s *BaseJingleParserListener) EnterDecimalLiteral(ctx *DecimalLiteralContext) {}

// ExitDecimalLiteral is called when production decimalLiteral is exited.
func (s *BaseJingleParserListener) ExitDecimalLiteral(ctx *DecimalLiteralContext) {}

// EnterMinusExpression is called when production minusExpression is entered.
func (s *BaseJingleParserListener) EnterMinusExpression(ctx *MinusExpressionContext) {}

// ExitMinusExpression is called when production minusExpression is exited.
func (s *BaseJingleParserListener) ExitMinusExpression(ctx *MinusExpressionContext) {}

// EnterIntLiteral is called when production intLiteral is entered.
func (s *BaseJingleParserListener) EnterIntLiteral(ctx *IntLiteralContext) {}

// ExitIntLiteral is called when production intLiteral is exited.
func (s *BaseJingleParserListener) ExitIntLiteral(ctx *IntLiteralContext) {}

// EnterParenExpression is called when production parenExpression is entered.
func (s *BaseJingleParserListener) EnterParenExpression(ctx *ParenExpressionContext) {}

// ExitParenExpression is called when production parenExpression is exited.
func (s *BaseJingleParserListener) ExitParenExpression(ctx *ParenExpressionContext) {}

// EnterBinaryOperation is called when production binaryOperation is entered.
func (s *BaseJingleParserListener) EnterBinaryOperation(ctx *BinaryOperationContext) {}

// ExitBinaryOperation is called when production binaryOperation is exited.
func (s *BaseJingleParserListener) ExitBinaryOperation(ctx *BinaryOperationContext) {}

// EnterTypeConversion is called when production typeConversion is entered.
func (s *BaseJingleParserListener) EnterTypeConversion(ctx *TypeConversionContext) {}

// ExitTypeConversion is called when production typeConversion is exited.
func (s *BaseJingleParserListener) ExitTypeConversion(ctx *TypeConversionContext) {}

// EnterVarReference is called when production varReference is entered.
func (s *BaseJingleParserListener) EnterVarReference(ctx *VarReferenceContext) {}

// ExitVarReference is called when production varReference is exited.
func (s *BaseJingleParserListener) ExitVarReference(ctx *VarReferenceContext) {}

// EnterInteger is called when production integer is entered.
func (s *BaseJingleParserListener) EnterInteger(ctx *IntegerContext) {}

// ExitInteger is called when production integer is exited.
func (s *BaseJingleParserListener) ExitInteger(ctx *IntegerContext) {}

// EnterDecimal is called when production decimal is entered.
func (s *BaseJingleParserListener) EnterDecimal(ctx *DecimalContext) {}

// ExitDecimal is called when production decimal is exited.
func (s *BaseJingleParserListener) ExitDecimal(ctx *DecimalContext) {}
