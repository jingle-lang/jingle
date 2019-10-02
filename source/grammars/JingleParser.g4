parser grammar JingleParser;

options { 
     tokenVocab=JingleLexer; 
     }

jingleFile : lines=line+ ;

// INTs only

line      : statement (ENDSTATEMENT | EOF) ;

statement : varDeclaration # varDeclarationStatement
          | assignment     # assignmentStatement
          | display          # displayStatement ;

display : DISPLAY COLON WHITESPACE LBRACKET expression RBRACKET ;

varDeclaration : VAR assignment ;

assignment : NOUNICODEID EQUALS expression ;

expression : left=expression operator=(DIVIDE|MULTIPLY) right=expression # binaryOperation
           | left=expression operator=(PLUS|MINUS) right=expression        # binaryOperation
           | value=expression AS targetType=dataType                           # typeConversion
           | LBRACKET expression RBRACKET                                      # parenExpression
           | NOUNICODEID                                                            # varReference
           | MINUS expression                                              # minusExpression
           | TYPE_INT                                                        # intLiteral
           | TYPE_DECIMAL                                                    # decimalLiteral ;

dataType : TYPE_INT      # integer
     | TYPE_DECIMAL # decimal ;

/*
// Development Parser
topLevelDecl
     : declaration
     | functionDecl
     | methodDecl
     ;

declaration
     : varDecl
     ;

functionDecl
    : FUNCTION IDENTIFIER ( function | signature )
    ;

function
    : signature block
    ;

methodDecl
    : FUNC receiver IDENTIFIER ( function | signature )
    ;

receiver
    : parameters
    ;     

varDecl
    : VAR ( varSpec | '(' ( varSpec )* ')' )
    ;

varSpec
    : identifierList ( type_ ( '=' expressionList )? | '=' expressionList )
    ;

block
    : '{' statementList '}'
    ;

statementList
    : ( statement )*
    ;

statement
    : declaration
	;
*/
