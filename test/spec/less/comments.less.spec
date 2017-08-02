/* One hell of a block
style comment! */
@var: red;

// Get in line!
@var: white;
============TEST
T_COMMENT,1:2,1:17,"\/* One hell of a block\nstyle comment! *\/"
T_WHITESPACE,3,0,"\n"
T_ATWORD,3:3,1:4,"@var"
T_COLON,3,5,":"
T_WHITESPACE,3,6," "
T_WORD,3:3,7:9,"red"
T_SEMICOLON,3,10,";"
T_WHITESPACE,5,0,"\n\n"
T_COMMENT,5:5,2:17,"\/\/ Get in line!"
T_ATWORD,5:5,18:21,"@var"
T_COLON,5,22,":"
T_WHITESPACE,5,23," "
T_WORD,5:5,24:28,"white"
T_SEMICOLON,5,29,";"
