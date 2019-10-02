parser grammar JingleParser;

options { 
     tokenVocab=JingleLexer; 
     }

jingleFile : lines=line+ ;

// INTs only

line      : statement (ENDSTATEMENT | EOF) ;

statement :
    | varDeclaration
    | stmtDisplay  ;


varDeclaration : VAR NOUNICODEID EQUALS INT_LITERAL ;

stmtDisplay : DISPLAY COLON LBRACKET (INT_LITERAL | NOUNICODEID) RBRACKET;

/*

display : DISPLAY COLON WHITESPACE LBRACKET expression RBRACKET ;

assignment : NOUNICODEID EQUALS expression ;

expression : left=expression operator=(DIVIDE|MULTIPLY) right=expression # binaryOperation
           | left=expression operator=(PLUS|MINUS) right=expression        # binaryOperation
           | value=expression AS targetType=dataType                           # typeConversion
           | LBRACKET expression RBRACKET                                      # parenExpression
           | NOUNICODEID                                                            # varReference
           | TYPE_INT                                                        # intLiteral
           | TYPE_DECIMAL                                                    # decimalLiteral 
           | TYPE_STRING ;

dataType : TYPE_INT      # integer
     | TYPE_DECIMAL # decimal ;

*/

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
