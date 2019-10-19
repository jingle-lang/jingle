package main

import (
	"fmt"
	"log"

	parser "./native"
	"github.com/antlr/antlr4/runtime/Go/antlr"
)

func main() {
	fs, err := antlr.NewFileStream("test.jn")
	if err != nil {
		log.Fatal(err)
	}
	lex := parser.NewJingleLexer(fs)
	tokens := antlr.NewCommonTokenStream(lex, antlr.TokenDefaultChannel)
	p := parser.NewJingleParser(tokens)
	visitor := parser.NewJingleParserVisitorImpl()
	tree := p.Input()
	fmt.Println(visitor.Visit(tree))
}
