.border-radius(@radius) {
  -webkit-border-radius: @radius;
     -moz-border-radius: @radius;
          border-radius: @radius;
}
#header {
  .border-radius(4px);
}
============TEST
T_WORD,1:1,1:14,".border-radius"
T_OPENBRACKET,1,15,"("
T_ATWORD,1:1,16:22,"@radius"
T_CLOSEBRACKET,1,23,")"
T_WHITESPACE,1,24," "
T_OPENCURLY,1,25,"{"
T_WHITESPACE,2,0,"\n  "
T_WORD,2:2,3:23,"-webkit-border-radius"
T_COLON,2,24,":"
T_WHITESPACE,2,25," "
T_ATWORD,2:2,26:32,"@radius"
T_SEMICOLON,2,33,";"
T_WHITESPACE,3,0,"\n     "
T_WORD,3:3,6:23,"-moz-border-radius"
T_COLON,3,24,":"
T_WHITESPACE,3,25," "
T_ATWORD,3:3,26:32,"@radius"
T_SEMICOLON,3,33,";"
T_WHITESPACE,4,0,"\n          "
T_WORD,4:4,11:23,"border-radius"
T_COLON,4,24,":"
T_WHITESPACE,4,25," "
T_ATWORD,4:4,26:32,"@radius"
T_SEMICOLON,4,33,";"
T_WHITESPACE,5,0,"\n"
T_CLOSECURLY,5,1,"}"
T_WHITESPACE,6,0,"\n"
T_WORD,6:6,1:7,"#header"
T_WHITESPACE,6,8," "
T_OPENCURLY,6,9,"{"
T_WHITESPACE,7,0,"\n  "
T_WORD,7:7,3:16,".border-radius"
T_OPENBRACKET,7,17,"("
T_WORD,7:7,18:20,"4px"
T_CLOSEBRACKET,7,21,")"
T_SEMICOLON,7,22,";"
T_WHITESPACE,8,0,"\n"
T_CLOSECURLY,8,1,"}"
