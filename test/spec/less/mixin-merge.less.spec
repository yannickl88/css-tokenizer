.mixin() {
  transform+_: scale(2);
}
.myclass {
  .mixin();
  transform+_: rotate(15deg);
}
============TEST
T_WORD,1:1,1:6,".mixin"
T_OPENBRACKET,1,7,"("
T_CLOSEBRACKET,1,8,")"
T_WHITESPACE,1,9," "
T_OPENCURLY,1,10,"{"
T_WHITESPACE,2,0,"\n  "
T_WORD,2:2,3:13,"transform+_"
T_COLON,2,14,":"
T_WHITESPACE,2,15," "
T_WORD,2:2,16:20,"scale"
T_OPENBRACKET,2,21,"("
T_WORD,2:2,22:22,"2"
T_CLOSEBRACKET,2,23,")"
T_SEMICOLON,2,24,";"
T_WHITESPACE,3,0,"\n"
T_CLOSECURLY,3,1,"}"
T_WHITESPACE,4,0,"\n"
T_WORD,4:4,1:8,".myclass"
T_WHITESPACE,4,9," "
T_OPENCURLY,4,10,"{"
T_WHITESPACE,5,0,"\n  "
T_WORD,5:5,3:8,".mixin"
T_OPENBRACKET,5,9,"("
T_CLOSEBRACKET,5,10,")"
T_SEMICOLON,5,11,";"
T_WHITESPACE,6,0,"\n  "
T_WORD,6:6,3:13,"transform+_"
T_COLON,6,14,":"
T_WHITESPACE,6,15," "
T_WORD,6:6,16:21,"rotate"
T_OPENBRACKET,6,22,"("
T_WORD,6:6,23:27,"15deg"
T_CLOSEBRACKET,6,28,")"
T_SEMICOLON,6,29,";"
T_WHITESPACE,7,0,"\n"
T_CLOSECURLY,7,1,"}"
