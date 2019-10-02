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

	// Visit a parse tree produced by JingleParser#statement.
	VisitStatement(ctx *StatementContext) interface{}

	// Visit a parse tree produced by JingleParser#varDeclaration.
	VisitVarDeclaration(ctx *VarDeclarationContext) interface{}

	// Visit a parse tree produced by JingleParser#stmtDisplay.
	VisitStmtDisplay(ctx *StmtDisplayContext) interface{}
}
