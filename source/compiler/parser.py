# gone/parser.py
'''
Project 2:  Write a parser
==========================
In this project, you write the basic shell of a parser for Gone.  A
formal BNF of the language follows.  Your task is to write parsing
rules and build the AST for this grammar using SLY.  The following
grammar is partial.  More features get added in later projects.

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

func_declaration : FN ID LPAREN func_params RPAREN datatype COLON block END

func_params : func_param COMA func_params
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

arguments : arguments COMA argument
          | argument
          | empty

argument : expression
         | ID

literal : INTEGER
        | FLOAT
        | CHAR
        | BOOL

location : ID
         ;

datatype : ID
         ;

empty    :

To do the project, follow the instructions contained below.
'''

# ----------------------------------------------------------------------
# parsers are defined using SLY.  You inherit from the Parser class
#
# See http://sly.readthedocs.io/en/latest/
# ----------------------------------------------------------------------
from sly import Parser

# ----------------------------------------------------------------------
# The following import loads a function error(lineno,msg) that should be
# used to report all error messages issued by your parser.  Unit tests and
# other features of the compiler will rely on this function.  See the
# file errors.py for more documentation about the error handling mechanism.
from .errors import error

# ----------------------------------------------------------------------
# Import the lexer class.  It's token list is needed to validate and
# build the parser object.
from .tokenizer import GoneLexer

# ----------------------------------------------------------------------
# Get the AST nodes.
# Read instructions in ast.py
from .ast import *

class GoneParser(Parser):
    # Same token set as defined in the lexer
    tokens = GoneLexer.tokens

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

    # ----------------------------------------------------------------------
    # YOUR TASK.   Translate the BNF in the string below into a collection
    # of parser functions.  For example, a rule such as :
    #
    #   program : statements
    #
    # Gets turned into a Python method like this:
    #
    # @_('statements')
    # def program(self, p):
    #      return Program(p.statements)
    #
    # For symbols such as '(' or '+', you'll need to replace with the name
    # of the corresponding token such as LPAREN or PLUS.
    #
    # In the body of each rule, create an appropriate AST node and return it
    # as shown above.
    #
    # For the purposes of lineno number tracking, you should assign a line number
    # to each AST node as appropriate.  To do this, I suggest pulling the
    # line number off of any nearby terminal symbol.  For example:
    #
    # @_('PRINT expr')
    # def print_statement(self, p):
    #     return PrintStatement(p.expr, lineno=p.lineno)
    #
    # STARTING OUT
    # ============
    # The following grammar rules should give you an idea of how to start.
    # Try running this file on the input Tests/parsetest0.g
    #
    # Afterwards, add features by looking at the code in Tests/parsetest1-6.g

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

    @_('FN ID LPAREN func_params RPAREN datatype COLON block END')
    def func_declaration(self, p):
        return FuncDeclaration(p.ID, p.func_params, p.datatype, p.block, lineno=p.lineno)

    @_('func_params COMA func_param')
    def func_params(self, p):
        p.func_params.append(p.func_param)
        return p.func_params

    @_('func_param')
    def func_params(self, p):
        return [p.func_param]

    @_('')
    def func_params(self, p):
        return []

    @_('ID datatype')
    def func_param(self, p):
        return FuncParameter(p.ID, p.datatype, lineno=p.lineno)

    @_("RETURN expression")
    def ret_statement(self, p):
        return ReturnStatement(p.expression, lineno=p.lineno)

    ##########################################

    @_('ID LPAREN arguments RPAREN')
    def func_call(self, p):
        return FuncCall(p.ID, p.arguments, lineno=p.lineno)

    @_('arguments COMA argument')
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
    lexer = GoneLexer()
    parser = GoneParser()
    ast = parser.parse(lexer.tokenize(source))
    return ast

def main():
    '''
    Main program. Used for testing.
    '''
    import sys

    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python3 -m gone.parser filename\n')
        raise SystemExit(1)

    # Parse and create the AST
    ast = parse(open(sys.argv[1]).read())

    # Output the resulting parse tree structure
    for depth, node in flatten(ast):
        print('%s: %s%s' % (getattr(node, 'lineno', None), ' '*(4*depth), node))

if __name__ == '__main__':
    main()
