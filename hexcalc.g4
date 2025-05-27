grammar hexcalc;

// Parser rules
expression
  : '-' expression                         # UnaryMinus
  | expression '^' expression              # Power
  | expression op=('*'|'/') expression     # MulDiv
  | expression '%' expression              # Mod
  | expression op=('+'|'-') expression     # AddSub
  | '(' expression ')'                     # Parens
  | HEX                                    # HexNumber
  ;

// Lexer rules
HEX : [0-9A-F]+ ;                // nombres hexadécimaux (ex : 1A, 3F)
WS  : [ \t\r\n]+ -> skip ;       // ignore les espaces
