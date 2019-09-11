// Code generated from JingleParser.g4 by ANTLR 4.7.2. DO NOT EDIT.

package parser // JingleParser

import "github.com/antlr/antlr4/runtime/Go/antlr"

// JingleParserListener is a complete listener for a parse tree produced by JingleParser.
type JingleParserListener interface {
	antlr.ParseTreeListener

	// EnterJingleFile is called when entering the jingleFile production.
	EnterJingleFile(c *JingleFileContext)

	// EnterLine is called when entering the line production.
	EnterLine(c *LineContext)

	// EnterVarDeclarationStatement is called when entering the varDeclarationStatement production.
	EnterVarDeclarationStatement(c *VarDeclarationStatementContext)

	// EnterAssignmentStatement is called when entering the assignmentStatement production.
	EnterAssignmentStatement(c *AssignmentStatementContext)

	// EnterDisplayStatement is called when entering the displayStatement production.
	EnterDisplayStatement(c *DisplayStatementContext)

	// EnterDisplay is called when entering the display production.
	EnterDisplay(c *DisplayContext)

	// EnterVarDeclaration is called when entering the varDeclaration production.
	EnterVarDeclaration(c *VarDeclarationContext)

	// EnterAssignment is called when entering the assignment production.
	EnterAssignment(c *AssignmentContext)

	// EnterDecimalLiteral is called when entering the decimalLiteral production.
	EnterDecimalLiteral(c *DecimalLiteralContext)

	// EnterMinusExpression is called when entering the minusExpression production.
	EnterMinusExpression(c *MinusExpressionContext)

	// EnterIntLiteral is called when entering the intLiteral production.
	EnterIntLiteral(c *IntLiteralContext)

	// EnterParenExpression is called when entering the parenExpression production.
	EnterParenExpression(c *ParenExpressionContext)

	// EnterBinaryOperation is called when entering the binaryOperation production.
	EnterBinaryOperation(c *BinaryOperationContext)

	// EnterTypeConversion is called when entering the typeConversion production.
	EnterTypeConversion(c *TypeConversionContext)

	// EnterVarReference is called when entering the varReference production.
	EnterVarReference(c *VarReferenceContext)

	// EnterInteger is called when entering the integer production.
	EnterInteger(c *IntegerContext)

	// EnterDecimal is called when entering the decimal production.
	EnterDecimal(c *DecimalContext)

	// ExitJingleFile is called when exiting the jingleFile production.
	ExitJingleFile(c *JingleFileContext)

	// ExitLine is called when exiting the line production.
	ExitLine(c *LineContext)

	// ExitVarDeclarationStatement is called when exiting the varDeclarationStatement production.
	ExitVarDeclarationStatement(c *VarDeclarationStatementContext)

	// ExitAssignmentStatement is called when exiting the assignmentStatement production.
	ExitAssignmentStatement(c *AssignmentStatementContext)

	// ExitDisplayStatement is called when exiting the displayStatement production.
	ExitDisplayStatement(c *DisplayStatementContext)

	// ExitDisplay is called when exiting the display production.
	ExitDisplay(c *DisplayContext)

	// ExitVarDeclaration is called when exiting the varDeclaration production.
	ExitVarDeclaration(c *VarDeclarationContext)

	// ExitAssignment is called when exiting the assignment production.
	ExitAssignment(c *AssignmentContext)

	// ExitDecimalLiteral is called when exiting the decimalLiteral production.
	ExitDecimalLiteral(c *DecimalLiteralContext)

	// ExitMinusExpression is called when exiting the minusExpression production.
	ExitMinusExpression(c *MinusExpressionContext)

	// ExitIntLiteral is called when exiting the intLiteral production.
	ExitIntLiteral(c *IntLiteralContext)

	// ExitParenExpression is called when exiting the parenExpression production.
	ExitParenExpression(c *ParenExpressionContext)

	// ExitBinaryOperation is called when exiting the binaryOperation production.
	ExitBinaryOperation(c *BinaryOperationContext)

	// ExitTypeConversion is called when exiting the typeConversion production.
	ExitTypeConversion(c *TypeConversionContext)

	// ExitVarReference is called when exiting the varReference production.
	ExitVarReference(c *VarReferenceContext)

	// ExitInteger is called when exiting the integer production.
	ExitInteger(c *IntegerContext)

	// ExitDecimal is called when exiting the decimal production.
	ExitDecimal(c *DecimalContext)
}
