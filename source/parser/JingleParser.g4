parser grammar Jingle;

start  :
     expression  EOF
  ;

expression
   :
   |   INT
   |   expression (PLUS | MINUS) expression
   ;

PLUS   :  '+';
MINUS  :  '-';
MULTIPLY : '*';
DIVIDE : '/';
INT    :  '0'..'9'+;
