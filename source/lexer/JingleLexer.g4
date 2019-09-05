lexer grammar JingleLexer;


fragment DIGIT : [0-9] ;

// Comment
COMMENT : '#' | . | '//';

// Keywords
VAR : 'var' ;
CONST : 'const' | . | 'constant';
DISPLAY : 'display' ;
IF : 'if' ;
ELSE : 'else' ;
FOR : 'for' ;
TRUE : 'true' ;
FALSE : 'false' ;
FUNC : 'func' ;
LET : 'let' ;

// Operators
ASSIGN : ':' ;
EQUALS : '=' ;
PLUS : '+' ;
MINUS : '-' ;
MULTIPLY : '*' ;
DIVIDE : '/' ;
LESSTHAN : '<' ;
GREATERTHAN : '>' ;
NOTEQUAL : '!=' ;
BANG : '!' ;

// Delimiters
COMMA : ',' ;
SEMICOLON : ';' ;
LBRACKET : '(' ;
RBRACKET : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LSQRBRACKET : '[' ;
RSQRBRACKET : ']' ;
ARROW : '->' ;

// Literals
FLOAT : 'float' ;
STRING : 'string' ;
BOOLEAN : 'bool' ;
NULL : 'null' ;
CHAR : 'char' ;

INT
   : DIGIT+
   | 'int'
   ;