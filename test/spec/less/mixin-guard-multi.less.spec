.mixin (@a) when (@a > 10), (@a < -10) {
}
============TEST
T_WORD,1:1,1:6,".mixin"
T_WHITESPACE,1,7," "
T_OPENBRACKET,1,8,"("
T_ATWORD,1:1,9:10,"@a"
T_CLOSEBRACKET,1,11,")"
T_WHITESPACE,1,12," "
T_WORD,1:1,13:16,"when"
T_WHITESPACE,1,17," "
T_OPENBRACKET,1,18,"("
T_ATWORD,1:1,19:20,"@a"
T_WHITESPACE,1,21," "
T_WORD,1:1,22:22,">"
T_WHITESPACE,1,23," "
T_WORD,1:1,24:25,"10"
T_CLOSEBRACKET,1,26,")"
T_COMMA,1,27,","
T_WHITESPACE,1,28," "
T_OPENBRACKET,1,29,"("
T_ATWORD,1:1,30:31,"@a"
T_WHITESPACE,1,32," "
T_WORD,1:1,33:33,"<"
T_WHITESPACE,1,34," "
T_WORD,1:1,35:37,"-10"
T_CLOSEBRACKET,1,38,")"
T_WHITESPACE,1,39," "
T_OPENCURLY,1,40,"{"
T_WHITESPACE,1:2,41:0,"\n"
T_CLOSECURLY,2,1,"}"
