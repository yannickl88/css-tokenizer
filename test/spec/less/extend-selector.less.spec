.big-division,
.big-bag:extend(.bag),
.big-bucket:extend(.bucket) {
}
============TEST
T_WORD,1:1,1:13,".big-division"
T_COMMA,1,14,","
T_WHITESPACE,1:2,15:0,"\n"
T_WORD,2:2,1:8,".big-bag"
T_COLON,2,9,":"
T_WORD,2:2,10:15,"extend"
T_OPENBRACKET,2,16,"("
T_WORD,2:2,17:20,".bag"
T_CLOSEBRACKET,2,21,")"
T_COMMA,2,22,","
T_WHITESPACE,2:3,23:0,"\n"
T_WORD,3:3,1:11,".big-bucket"
T_COLON,3,12,":"
T_WORD,3:3,13:18,"extend"
T_OPENBRACKET,3,19,"("
T_WORD,3:3,20:26,".bucket"
T_CLOSEBRACKET,3,27,")"
T_WHITESPACE,3,28," "
T_OPENCURLY,3,29,"{"
T_WHITESPACE,3:4,30:0,"\n"
T_CLOSECURLY,4,1,"}"
