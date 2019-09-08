lexer grammar JingleLexer;

// Helpers
fragment DIGIT : [0-9] ;
fragment DIGIT_CONT : [0-9_] ;
fragment HEXDIGIT : [0-9a-fA-F_] ;
fragment BINARY : [0-1_] ;
fragment WHITESPACE : [ \t\r\n]+ -> skip ;

// Comment
COMMENT : '#' | . | '//';

// Keywords
VAR : 'var' ;
ARRAY : 'array' ;
CONST : 'const' | . | 'constant';
DISPLAY : 'display' ;
RETURN : 'return' ;
IF : 'if' ;
ELSE : 'else' ;
ELIF : 'elif' ;
FOR : 'for' ;
TRUE : 'true' ;
FALSE : 'false' ;
FUNC : 'function' | . | 'func' | . | 'fn' ;
CLASS : 'class' ;
LET : 'let' ;
TRAIT : 'trait' ;
DEFINE : 'def' ;
PROTOCOL : 'protocol' ;

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
OR : '|' ;
EQEQ : '==' ;
HASH : '#' ;
AMBERSAND : '&' ;

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
