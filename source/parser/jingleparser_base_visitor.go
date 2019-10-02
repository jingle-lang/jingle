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

func (v *BaseJingleParserVisitor) VisitStatement(ctx *StatementContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitVarDeclaration(ctx *VarDeclarationContext) interface{} {
	return v.VisitChildren(ctx)
}

func (v *BaseJingleParserVisitor) VisitStmtDisplay(ctx *StmtDisplayContext) interface{} {
	return v.VisitChildren(ctx)
}
