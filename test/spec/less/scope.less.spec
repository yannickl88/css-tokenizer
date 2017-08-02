@var: red;

#page {
  @var: white;
  #header {
    color: @var;
  }
}
============TEST
T_ATWORD,1:1,1:4,"@var"
T_COLON,1,5,":"
T_WHITESPACE,1,6," "
T_WORD,1:1,7:9,"red"
T_SEMICOLON,1,10,";"
T_WHITESPACE,3,0,"\n\n"
T_WORD,3:3,2:6,"#page"
T_WHITESPACE,3,7," "
T_OPENCURLY,3,8,"{"
T_WHITESPACE,4,0,"\n  "
T_ATWORD,4:4,3:6,"@var"
T_COLON,4,7,":"
T_WHITESPACE,4,8," "
T_WORD,4:4,9:13,"white"
T_SEMICOLON,4,14,";"
T_WHITESPACE,5,0,"\n  "
T_WORD,5:5,3:9,"#header"
T_WHITESPACE,5,10," "
T_OPENCURLY,5,11,"{"
T_WHITESPACE,6,0,"\n    "
T_WORD,6:6,5:9,"color"
T_COLON,6,10,":"
T_WHITESPACE,6,11," "
T_ATWORD,6:6,12:15,"@var"
T_SEMICOLON,6,16,";"
T_WHITESPACE,7,0,"\n  "
T_CLOSECURLY,7,3,"}"
T_WHITESPACE,8,0,"\n"
T_CLOSECURLY,8,1,"}"
