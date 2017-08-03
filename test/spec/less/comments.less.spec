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
T_COMMENT,5:5,2:16,"\/\/ Get in line"
T_WHITESPACE,6,0,"\n"
T_ATWORD,6:6,1:4,"@var"
T_COLON,6,5,":"
T_WHITESPACE,6,6," "
T_WORD,6:6,7:11,"white"
T_SEMICOLON,6,12,";"
