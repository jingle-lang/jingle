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

	// EnterStatement is called when entering the statement production.
	EnterStatement(c *StatementContext)

	// EnterVarDeclaration is called when entering the varDeclaration production.
	EnterVarDeclaration(c *VarDeclarationContext)

	// EnterStmtDisplay is called when entering the stmtDisplay production.
	EnterStmtDisplay(c *StmtDisplayContext)

	// ExitJingleFile is called when exiting the jingleFile production.
	ExitJingleFile(c *JingleFileContext)

	// ExitLine is called when exiting the line production.
	ExitLine(c *LineContext)

	// ExitStatement is called when exiting the statement production.
	ExitStatement(c *StatementContext)

	// ExitVarDeclaration is called when exiting the varDeclaration production.
	ExitVarDeclaration(c *VarDeclarationContext)

	// ExitStmtDisplay is called when exiting the stmtDisplay production.
	ExitStmtDisplay(c *StmtDisplayContext)
}
