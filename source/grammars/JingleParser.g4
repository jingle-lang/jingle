parser grammar JingleParser;

options { 
     tokenVocab=JingleLexer; 
     }

top_level_decl : statements? ;

end_of_statement : ENDSTATEMENT | SEMICOLONTERMINATE | EOF ;

// Primitives

attributes : attribute+ ;
attribute : ATTSYMBOL IDENTIFIER LBRACKET attribute_list RBRACKET ;
attribute_list
     : IDENTIFIER
     | expression
     | literal
     | operator
     ;

operator : (PLUS | MINUS | MULTIPLY | DIVIDE | POWER | EQUALS | BANG | MODULUS | AMBERSAND | VERTICAL | LESSTHAN | GREATERTHAN ) ;
statements : statement+ ;

block : NEWLINE INDENT statement+ DEDENT ;

param_list : param (COMMA param)* COMMA? ;

param : ;

// Expressions

expression
     : main_expression
     | unary_expression
     | expression (MULTIPLY | DIVIDE | MODULUS) expression
     | expression (PLUS | MINUS | POWER) expression
     | expression (EQEQ | NOTEQUAL | LESSTHAN | GREATERTHAN | LESSTHANEQUAL | MORETHANEQUAL) expression
     | expression (ANDSYMBOL | AND) expression
     | expression (ORSYMBOL | OR) expression
     ;

main_expression
     : operand
     | main_expression ( DOT IDENTIFIER )
     ;

unary_expression
     : main_expression
     | (PLUS | MINUS | BANG | POWER | MULTIPLY | AMBERSAND | BACKARROW) expression
     ;

operand
     : literal
     ;

literal
     : STRING
     | NUMBER
     ;

// Parser Rules

statement
     : declaration
     | expression
     | loop_statement
     | control_statement
     ;

declaration
     : var_declaration
     | function_declaration
     | class_declaration
     | trait_declaration
     | import_declaration
     | static_var_declaration
     ;

var_declaration // var string = "hello" 
     : var_declaration_prefix IDENTIFIER EQUALS expression
     ;

var_declaration_prefix
     : attributes? var_declaration_keyword
     ;

var_declaration_keyword // con pi = 3.14
     : VAR
     | LET
     ;

function_declaration // fn func()
     : function_declaration_prefix IDENTIFIER LBRACKET param_list? RBRACKET block
     ;

function_declaration_prefix
     : attributes? FUNCTION
     ;

class_declaration // class Class()
     : class_declaration_prefix IDENTIFIER ( LBRACKET (param_list)? RBRACKET )? block 
     ;

class_declaration_prefix
     : attributes? CLASS
     ;

trait_declaration
     : trait_declaration_prefix IDENTIFIER trait_block
     ;

trait_declaration_prefix
     : attributes? TRAIT
     ;

trait_block
     : NEWLINE INDENT trait_block_body+ DEDENT
     ;

trait_block_body
     : function_declaration
     | var_declaration
     | property_declaration
     ;

property_declaration
     : property_declaration_prefix IDENTIFIER EQUALS expression
     ;

property_declaration_prefix
     : attributes? DEFINE
     ; 

import_declaration
     : import_name_direct
     | import_from
     ;

import_name_direct
     : IMPORT STRING
     ;

import_from
     : FROM STRING IMPORT STRING
     ;

static_var_declaration // bind string = "hello" 
     : static_var_declaration_prefix IDENTIFIER EQUALS expression
     ;

static_var_declaration_prefix
     : attributes? BIND
     ;

loop_statement
     : for_statement
     | while_statement
     ;

for_statement
     : FOR expression? expression? expression? block
     ;

while_statement
     : WHILE expression block
     ;

control_statement
     : if_statement
     ;

if_statement
     : IF expression else_statement? block
     ;

else_statement
     : ELSE block
     | ELSE if_statement
     ;