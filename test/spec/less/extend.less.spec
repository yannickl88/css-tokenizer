nav ul {
  &:extend(.inline);
  background: blue;
}
============TEST
T_WORD,1:1,1:3,"nav"
T_WHITESPACE,1,4," "
T_WORD,1:1,5:6,"ul"
T_WHITESPACE,1,7," "
T_OPENCURLY,1,8,"{"
T_WHITESPACE,1:2,9:2,"\n  "
T_WORD,2:2,3:3,"&"
T_COLON,2,4,":"
T_WORD,2:2,5:10,"extend"
T_OPENBRACKET,2,11,"("
T_WORD,2:2,12:18,".inline"
T_CLOSEBRACKET,2,19,")"
T_SEMICOLON,2,20,";"
T_WHITESPACE,2:3,21:2,"\n  "
T_WORD,3:3,3:12,"background"
T_COLON,3,13,":"
T_WHITESPACE,3,14," "
T_WORD,3:3,15:18,"blue"
T_SEMICOLON,3,19,";"
T_WHITESPACE,3:4,20:0,"\n"
T_CLOSECURLY,4,1,"}"
