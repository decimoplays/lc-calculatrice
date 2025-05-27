grammar hexcalc;

// Parser rules
expression
  : expression op=('*'|'/') expression     # MulDiv
  | expression op=('+'|'-') expression     # AddSub
  | '(' expression ')'                     # Parens
  | HEX                                    # HexNumber
  ;

// Lexer rules
HEX : [0-9A-F]+ ;                // nombres hexadécimaux (ex : 1A, 3F)
WS  : [ \t\r\n]+ -> skip ;       // ignore les espaces
