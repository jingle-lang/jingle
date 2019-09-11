// Code generated from JingleParser.g4 by ANTLR 4.7.2. DO NOT EDIT.

package parser // JingleParser

import "github.com/antlr/antlr4/runtime/Go/antlr"

// A complete Visitor for a parse tree produced by JingleParser.
type JingleParserVisitor interface {
	antlr.ParseTreeVisitor

	// Visit a parse tree produced by JingleParser#jingleFile.
	VisitJingleFile(ctx *JingleFileContext) interface{}

	// Visit a parse tree produced by JingleParser#line.
	VisitLine(ctx *LineContext) interface{}

	// Visit a parse tree produced by JingleParser#varDeclarationStatement.
	VisitVarDeclarationStatement(ctx *VarDeclarationStatementContext) interface{}

	// Visit a parse tree produced by JingleParser#assignmentStatement.
	VisitAssignmentStatement(ctx *AssignmentStatementContext) interface{}

	// Visit a parse tree produced by JingleParser#displayStatement.
	VisitDisplayStatement(ctx *DisplayStatementContext) interface{}

	// Visit a parse tree produced by JingleParser#display.
	VisitDisplay(ctx *DisplayContext) interface{}

	// Visit a parse tree produced by JingleParser#varDeclaration.
	VisitVarDeclaration(ctx *VarDeclarationContext) interface{}

	// Visit a parse tree produced by JingleParser#assignment.
	VisitAssignment(ctx *AssignmentContext) interface{}

	// Visit a parse tree produced by JingleParser#decimalLiteral.
	VisitDecimalLiteral(ctx *DecimalLiteralContext) interface{}

	// Visit a parse tree produced by JingleParser#minusExpression.
	VisitMinusExpression(ctx *MinusExpressionContext) interface{}

	// Visit a parse tree produced by JingleParser#intLiteral.
	VisitIntLiteral(ctx *IntLiteralContext) interface{}

	// Visit a parse tree produced by JingleParser#parenExpression.
	VisitParenExpression(ctx *ParenExpressionContext) interface{}

	// Visit a parse tree produced by JingleParser#binaryOperation.
	VisitBinaryOperation(ctx *BinaryOperationContext) interface{}

	// Visit a parse tree produced by JingleParser#typeConversion.
	VisitTypeConversion(ctx *TypeConversionContext) interface{}

	// Visit a parse tree produced by JingleParser#varReference.
	VisitVarReference(ctx *VarReferenceContext) interface{}

	// Visit a parse tree produced by JingleParser#integer.
	VisitInteger(ctx *IntegerContext) interface{}

	// Visit a parse tree produced by JingleParser#decimal.
	VisitDecimal(ctx *DecimalContext) interface{}
}
