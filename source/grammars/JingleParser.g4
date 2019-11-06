parser grammar JingleParser;

options { 
     tokenVocab=JingleLexer; 
     }

jingleFile
    // : lines=line+
    : packagePhrase endOfStatement ( importDecl endOfStatement )* ( topLevelDecl endOfStatement)*
    ;

// INTs only

packagePhrase
    : PACKAGE NOUNICODEID
    ;

importDecl
    : IMPORT ( importSpec | LBRACKET ( importSpec endOfStatement)* RBRACKET )
    ;

importSpec
    : STRING_LIT
    ;

topLevelDecl
    : statement
    | funcDecl
    ;

line      : statement (ENDSTATEMENT | EOF) ;

endOfStatement :
    ENDSTATEMENT
    | EOF
    ;

statement :
    | declaration
    | ifStmt
    | forStmt
    | returnStmt
    | simpleStmt
    | block
    | echoDisplay 
    ;

declaration :
    | varDecl
    | funcDecl ;

varDecl : VAR NOUNICODEID WHITESPACE EQUALS ( INT_LITERAL | NOUNICODEID ) ;

funcDecl : FUNCTION WHITESPACE NOUNICODEID WHITESPACE LBRACKET params RBRACKET WHITESPACE COLON ;

echoDisplay : ECHO WHITESPACE LBRACKET (INT_LITERAL | NOUNICODEID) RBRACKET;

params
    : LBRACKET ( paramList COMMA? )? RBRACKET
    ;

identifierList
    : NOUNICODEID ( COMMA NOUNICODEID )*
    ;

expressionList
    : expression ( COMMA NOUNICODEID )*
    ;

paramList
    : paramDecl (COMMA paramDecl)*
    ;

paramDecl
    : identifierList? ELLIPSIS?
    ;

ifStmt
    : IF (simpleStmt)? expression block ( ELSE (ifStmt | block) )?
    ;

forStmt
    : FOR ( expression | forClause )?
    ;

whileStmt
    : WHILE (expression | forClause)?
    ;

returnStmt
    : RETURN expressionList?
    ;

simpleStmt
    : expression
    | incDecStmt
    | assign_op
    | shortVarDecl
    | emptyStmt
    ;

incDecStmt
    : expression ( PLUSPLUS | MINUSMINUS)
    ;

assign_op
    : (PLUS | MINUS | MULTIPLY | DIVIDE | MODULUS | ANDSYMBOL)? EQUALS
    ;

shortVarDecl
    : identifierList WALRUS expressionList
    ;

emptyStmt
    : endOfStatement 
    ;   

block
    : INDENT statementList DEDENT
    ;

statementList
    : statement endOfStatement
    ;

forClause
    : 
    ;

expression : left=expression operator=(DIVIDE|MULTIPLY) right=expression # binaryOperation
           | left=expression operator=(PLUS|MINUS) right=expression        # binaryOperation
           | value=expression AS targetType=dataType                           # typeConversion
           | LBRACKET expression RBRACKET      # parenExpression
           ;                                

dataType
    : TYPE_INT
    | TYPE_DECIMAL
    | TYPE_STRING
    ;
/*

display : DISPLAY COLON WHITESPACE LBRACKET expression RBRACKET ;

assignment : NOUNICODEID EQUALS expression ;


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