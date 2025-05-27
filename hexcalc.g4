grammar hexcalc;

// Parser rules
prog
  : statement+ EOF
  ;

statement
  : ID '=' expression                      # Assign
  | expression                             # Expr
  ;

expression
  : '-' expression                         # UnaryMinus
  | expression '^' expression              # Power
  | expression op=('*'|'/') expression     # MulDiv
  | expression '%' expression              # Mod
  | expression op=('+'|'-') expression     # AddSub
  | '(' expression ')'                     # Parens
  | ID                                     # Variable
  | HEX                                    # HexNumber
  ;

// Lexer rules
ID  : [a-z_][a-zA-Z_0-9]* ;   
HEX : [0-9A-F]+ ;                // nombres hexadécimaux (ex : 1A, 3F)
WS  : [ \t\r\n]+ -> skip ;       // ignore les espaces
