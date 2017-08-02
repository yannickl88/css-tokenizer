@images: "../img";

body {
  color: #444;
  background: url("@{images}/white-sand.png");
}
============TEST
T_ATWORD,1:1,1:7,"@images"
T_COLON,1,8,":"
T_WHITESPACE,1,9," "
T_STRING,1:1,10:17,"\"..\/img\""
T_SEMICOLON,1,18,";"
T_WHITESPACE,3,0,"\n\n"
T_WORD,3:3,2:5,"body"
T_WHITESPACE,3,6," "
T_OPENCURLY,3,7,"{"
T_WHITESPACE,4,0,"\n  "
T_WORD,4:4,3:7,"color"
T_COLON,4,8,":"
T_WHITESPACE,4,9," "
T_WORD,4:4,10:13,"#444"
T_SEMICOLON,4,14,";"
T_WHITESPACE,5,0,"\n  "
T_WORD,5:5,3:12,"background"
T_COLON,5,13,":"
T_WHITESPACE,5,14," "
T_WORD,5:5,15:17,"url"
T_OPENBRACKET,5,18,"("
T_STRING,5:5,19:44,"\"@{images}\/white-sand.png\""
T_CLOSEBRACKET,5,45,")"
T_SEMICOLON,5,46,";"
T_WHITESPACE,6,0,"\n"
T_CLOSECURLY,6,1,"}"
