import lexer

def main():

	content = ""
	with open('test.jn', 'r') as file:
		content = file.read()

	lex = lexer.Lexer(content)
	tokens = lex.tokenize()

main()
