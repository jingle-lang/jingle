/*
 * Parser Rules
 */

operation  : NUMBER '+' NUMBER ;

/*
 * Lexer Rules
 */

NUMBER     : [0-9]+ ;

WHITESPACE : ' ' -> skip ;