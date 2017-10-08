@nice-blue: #5B83AD;
@light-blue: @nice-blue + #111;

#header {
  color: @light-blue;
}
============TEST
T_ATWORD,1:1,1:10,"@nice-blue"
T_COLON,1,11,":"
T_WHITESPACE,1,12," "
T_WORD,1:1,13:19,"#5B83AD"
T_SEMICOLON,1,20,";"
T_WHITESPACE,1:2,21:0,"\n"
T_ATWORD,2:2,1:11,"@light-blue"
T_COLON,2,12,":"
T_WHITESPACE,2,13," "
T_ATWORD,2:2,14:23,"@nice-blue"
T_WHITESPACE,2,24," "
T_WORD,2:2,25:25,"+"
T_WHITESPACE,2,26," "
T_WORD,2:2,27:30,"#111"
T_SEMICOLON,2,31,";"
T_WHITESPACE,2:4,32:0,"\n\n"
T_WORD,4:4,1:7,"#header"
T_WHITESPACE,4,8," "
T_OPENCURLY,4,9,"{"
T_WHITESPACE,4:5,10:2,"\n  "
T_WORD,5:5,3:7,"color"
T_COLON,5,8,":"
T_WHITESPACE,5,9," "
T_ATWORD,5:5,10:20,"@light-blue"
T_SEMICOLON,5,21,";"
T_WHITESPACE,5:6,22:0,"\n"
T_CLOSECURLY,6,1,"}"
