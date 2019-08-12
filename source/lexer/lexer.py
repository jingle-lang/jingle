import re

class Lexer(object):

	def __init__(self, source_code):
		self.source_code = source_code

	def tokenize(self):

		tokens = []

		source_code = self.source_code.split()

		source_index = 0

		while source_index < len(source_code):

			word = (source_code[source_index])

			if word == "var": tokens.append(["VAR_DECLERATION", word])

			elif re.match('[a-z]', word) or re.match('[A-Z]', word):
				tokens.append(['IDENTIFIER', word])

			elif re.match('[0-9]', word):
				tokens.append(['INTEGER', word])

			elif word in "=/*=-+":
				tokens.append(['OPERATOR', word])

			elif word in ";":
				tokens.append(['SEMICOLON', word])

			source_index += 1

		print(tokens)

		return tokens
