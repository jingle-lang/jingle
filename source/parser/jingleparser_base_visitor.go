// Code generated from JingleParser.g4 by ANTLR 4.7.2. DO NOT EDIT.

package parser // JingleParser

import "github.com/antlr/antlr4/runtime/Go/antlr"

type BaseJingleParserVisitor struct {
	*antlr.BaseParseTreeVisitor
}

func (v *BaseJingleParserVisitor) VisitJingleFile(ctx *JingleFileContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitLine(ctx *LineContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitVarDeclarationStatement(ctx *VarDeclarationStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitAssignmentStatement(ctx *AssignmentStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitDisplayStatement(ctx *DisplayStatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitDisplay(ctx *DisplayContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitVarDeclaration(ctx *VarDeclarationContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitAssignment(ctx *AssignmentContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitDecimalLiteral(ctx *DecimalLiteralContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitMinusExpression(ctx *MinusExpressionContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitIntLiteral(ctx *IntLiteralContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitParenExpression(ctx *ParenExpressionContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitBinaryOperation(ctx *BinaryOperationContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitTypeConversion(ctx *TypeConversionContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitVarReference(ctx *VarReferenceContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitInteger(ctx *IntegerContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitDecimal(ctx *DecimalContext) interface{} {
	return v.VisitChildren(ctx)
}
