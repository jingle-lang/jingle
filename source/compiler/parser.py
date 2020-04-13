# parser.py
'''
Jingle Grammar

program : block
        | empty

block : statements
      | empty

statements :  statements statement
           |  statement

statement :  const_declaration
          |  var_declaration
          |  assign_statement
          |  echo_statement
          |  if_statement
          |  while_statement
          |  func_declaration
          |  ret_statement

func_declaration : FN ID LPAREN func_params RPAREN ARROW datatype COLON block END

func_params : func_param COMMA func_params
            | func_param
            | empty

func_param : ID datatype

ret_statement : RETURN expression 

const_declaration : CONST ID = expression ;

var_declaration : VAR ID datatype ;
                | VAR ID datatype = expression ;

assign_statement : location = expression ;

echo_statement : ECHO expression ;

if_statement: IF expression COLON block END
            | IF expression COLON block END ELSE COLON block END

expression :  + expression
           |  - expression
           |  ! expression
           | expression + expression
           | expression - expression
           | expression * expression
           | expression / expression
           | expression < expression
           | expression <= expression
           | expression > expression
           | expression >= expression
           | expression == expression
           | expression != expression
           | expression && expression
           | expression || expression
           | ( expression )
           | location
           | literal
           | func_call

func_call : ID LPAREN arguments RPAREN 

arguments : arguments COMMA argument
          | argument
          | empty

argument : expression
         | ID

literal : INTEGER
        | FLOAT
        | CHAR
        | BOOL
        | STRING

location : ID
         ;

datatype : ID
         ;

empty    :

'''

from sly import Parser
from .errors import error
from .scanner import JingleLexer
from .ast import *

class JingleParser(Parser):
    tokens = JingleLexer.tokens

    # ----------------------------------------------------------------------
    # Operator precedence table.   Operators must follow the same
    # precedence rules as in Python.  Instructions to be given in the project.

    precedence = (
        ('left', 'AND', 'NOT'),
        ('nonassoc', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'UNARY')
    )

    @_("statements")
    def block(self, p):
        return p.statements

    @_("")
    def block(self, p):
        return []

    ##########################################

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('statements statement')
    def statements(self, p):
        p.statements.append(p.statement)
        return p.statements

    ##########################################

    @_('echo_statement')
    def statement(self, p):
        return p.echo_statement

    @_('const_declaration')
    def statement(self, p):
        return p.const_declaration

    @_('var_declaration')
    def statement(self, p):
        return p.var_declaration

    @_('assign_statement')
    def statement(self, p):
        return p.assign_statement

    @_('if_statement')
    def statement(self, p):
        return p.if_statement

    @_('while_statement')
    def statement(self, p):
        return p.while_statement

    @_('func_declaration')
    def statement(self, p):
        return p.func_declaration

    @_('ret_statement')
    def statement(self, p):
        return p.ret_statement

    ##########################################

    @_('FN ID LPAREN func_params RPAREN ARROW datatype COLON block END')
    def func_declaration(self, p):
        return FuncDeclaration(p.ID, p.func_params, p.datatype, p.block, lineno=p.lineno)

    @_('func_params COMMA func_param')
    def func_params(self, p):
        p.func_params.append(p.func_param)
        return p.func_params

    @_('func_param')
    def func_params(self, p):
        return [p.func_param]

    @_('')
    def func_params(self, p):
        return []

    @_('ID COLON datatype')
    def func_param(self, p):
        return FuncParameter(p.ID, p.datatype, lineno=p.lineno)

    @_("RETURN expression")
    def ret_statement(self, p):
        return ReturnStatement(p.expression, lineno=p.lineno)

    ##########################################

    @_('ID LPAREN arguments RPAREN')
    def func_call(self, p):
        return FuncCall(p.ID, p.arguments, lineno=p.lineno)

    @_('arguments COMMA argument')
    def arguments(self, p):
        p.arguments.append(p.argument)
        return p.arguments

    @_('argument')
    def arguments(self, p):
        return [p.argument]

    @_('')
    def arguments(self, p):
        return []

    @_('expression')
    def argument(self, p):
        return p.expression

    ##########################################

    @_('IF expression COLON block END ELSE COLON block END')
    def if_statement(self, p):
        return IfStatement(p.expression, p[3], p[7], lineno=p.lineno)

    @_('IF expression COLON block END')
    def if_statement(self, p):
        return IfStatement(p.expression, p[3], [], lineno=p.lineno)

    ###########################################

    @_('WHILE expression COLON block END')
    def while_statement(self, p):
        return WhileStatement(p.expression, p.block, lineno=p.lineno)

    ###########################################

    @_('ECHO expression')
    def echo_statement(self, p):
        return EchoStatement(p.expression, lineno=p.lineno)

    ##########################################

    @_('CONST ID ASSIGN expression')
    def const_declaration(self, p):
        return ConstDeclaration(p[1], p.expression, lineno=p.lineno)

    ##########################################

    @_('VAR ID COLON datatype')
    def var_declaration(self, p):
        return VarDeclaration(p[1], p.datatype, None, lineno=p.lineno)

    @_('VAR ID COLON datatype ASSIGN expression')
    def var_declaration(self, p):
        return VarDeclaration(p[1], p.datatype, p.expression, lineno=p.lineno)

    ##########################################

    @_('location ASSIGN expression')
    def assign_statement(self, p):
        return WriteLocation(p.location, p.expression, lineno=p.lineno)

    ##########################################

    @_('expression PLUS expression',
       'expression MINUS expression',
       'expression TIMES expression',
       'expression DIVIDE expression',
       'expression LT expression',
       'expression LE expression',
       'expression GT expression',
       'expression GE expression',
       'expression EQ expression',
       'expression NE expression',
       'expression MOD expression',
       'expression AND expression',
       'expression OR expression')
    def expression(self, p):
        return BinOp(p[1], p.expression0, p.expression1, lineno=p.lineno)

    @_('PLUS expression',
       'MINUS expression',
       'NOT expression %prec UNARY')
    def expression(self, p):
        return UnaryOp(p[0], p.expression, lineno=p.lineno)

    @_('LPAREN expression RPAREN')
    def expression(self, p):
        return p.expression

    @_('location')
    def expression(self, p):
        return ReadLocation(p.location, lineno=p.location.lineno)

    @_('literal')
    def expression(self, p):
        return p.literal

    @_('func_call')
    def expression(self, p):
        return p.func_call

    ##########################################

    @_('INTEGER')
    def literal(self, p):
        return IntegerLiteral(int(p.INTEGER), lineno=p.lineno)

    @_('FLOAT')
    def literal(self, p):
        return FloatLiteral(float(p.FLOAT), lineno=p.lineno)

    @_('CHAR')
    def literal(self, p):
        return CharLiteral(eval(p.CHAR), lineno=p.lineno)

    #@_('STRING')
    #def literal(self, p):
    #    return StringLiteral(eval(p.STRING), lineno=p.lineno)

    @_('BOOL')
    def literal(self, p):
        return BoolLiteral(p.BOOL, lineno=p.lineno)

    #########################################

    @_('ID')
    def datatype(self, p):
        return SimpleType(p.ID, lineno=p.lineno)

    #########################################

    @_('ID')
    def location(self, p):
        return SimpleLocation(p.ID, lineno=p.lineno)

    # ----------------------------------------------------------------------
    # DO NOT MODIFY
    #
    # catch-all error handling.   The following function gets called on any
    # bad input.  p is the offending token or None if end-of-file (EOF).
    def error(self, p):
        if p:
            error(p.lineno, "Syntax error in input at token '%s'" % p.value)
        else:
            error('EOF','Syntax error. No more input.')

# ----------------------------------------------------------------------
#                     DO NOT MODIFY ANYTHING BELOW HERE
# ----------------------------------------------------------------------

def parse(source):
    '''
    Parse source code into an AST. Return the top of the AST tree.
    '''
    lexer = JingleLexer()
    parser = JingleParser()
    ast = parser.parse(lexer.tokenize(source))
    return ast

def main():
    '''
    Main program. Used for testing.
    '''
    import sys

    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python3 -m jingle.parser filename\n')
        raise SystemExit(1)

    # Parse and create the AST
    ast = parse(open(sys.argv[1]).read())

    # Output the resulting parse tree structure
    for depth, node in flatten(ast):
        print('%s: %s%s' % (getattr(node, 'lineno', None), ' '*(4*depth), node))

if __name__ == '__main__':
    main()
