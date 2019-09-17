lexer grammar JingleLexer;

// Channels
channels { COMMENTS }

// Helpers
fragment SEMICOLON : ';' ;
fragment NEWLINE : '\r' '\n' | '\n' | '\r' ;
fragment ID : [a-zA-Z]+ ;
fragment DIGIT : [0-9] ;
fragment DIGIT_CONT : [0-9_] ;
fragment HEXDIGIT : [0-9a-fA-F_] ;
fragment BINARY : [0-1_] ;
fragment WHITESPACE : [ \t\r\n]+ -> skip ;
fragment UNICODE_WS : [\p{White_Space}] -> skip;

ENDSTATEMENT : NEWLINE* | NEWLINE+;
SEMICOLONTERMINATE : SEMICOLON NEWLINE* | NEWLINE+;

// Comment
COMMENT : '//' -> channel(COMMENTS);

// Quotes
SPEECHMARKS : '"' ;

// Keywords
VAR : 'var' ;
ARRAY : 'array' ;
CONST : 'const' | . | 'constant';
DISPLAY : 'display' ;
RETURN : 'return' ;
IF : 'if' ;
IN : 'in' ;
ELSE : 'else' ;
ELIF : 'elif' ;
WHILE : 'while' ;
FOR : 'for' ;
TRUE : 'true' ;
FALSE : 'false' ;
FUNC : 'function' | . | 'func' | . | 'fn' ;
CLASS : 'class' ;
LET : 'let' ;
TRAIT : 'trait' ;
DEFINE : 'def' ;
PROTOCOL : 'protocol' ;
ENUM : 'enum' ;
IMPORT : 'import' ;
FROM : 'from' ;
PACKAGE : 'package' ;
AS : 'as' ;

// Operators
ASSIGN : ':=' ;
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
