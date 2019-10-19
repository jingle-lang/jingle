package main

import (
	parser "./native"
	"github.com/antlr/antlr4/runtime/Go/antlr"
)

// JingleParserListener : good
type JingleParserListener struct {
	*parser.BaseJingleParserListener
}

func main() {
	// Setup the input
	is := antlr.NewInputStream("display:(5)")

	// Create the Lexer
	lexer := parser.NewJingleLexer(is)
	stream := antlr.NewCommonTokenStream(lexer, antlr.TokenDefaultChannel)

	// Create the Parser
	p := parser.NewJingleParser(stream)

	// Finally parse the expression
	antlr.ParseTreeWalkerDefault.Walk(&JingleParserListener{}, p.Start())
}
