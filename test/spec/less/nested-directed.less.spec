.screen-color {
  @media screen {
    color: green;
    @media (min-width: 768px) {
      color: red;
    }
  }
  @media tv {
    color: black;
  }
}
============TEST
T_WORD,1:1,1:13,".screen-color"
T_WHITESPACE,1,14," "
T_OPENCURLY,1,15,"{"
T_WHITESPACE,2,0,"\n  "
T_ATWORD,2:2,3:8,"@media"
T_WHITESPACE,2,9," "
T_WORD,2:2,10:15,"screen"
T_WHITESPACE,2,16," "
T_OPENCURLY,2,17,"{"
T_WHITESPACE,3,0,"\n    "
T_WORD,3:3,5:9,"color"
T_COLON,3,10,":"
T_WHITESPACE,3,11," "
T_WORD,3:3,12:16,"green"
T_SEMICOLON,3,17,";"
T_WHITESPACE,4,0,"\n    "
T_ATWORD,4:4,5:10,"@media"
T_WHITESPACE,4,11," "
T_OPENBRACKET,4,12,"("
T_WORD,4:4,13:21,"min-width"
T_COLON,4,22,":"
T_WHITESPACE,4,23," "
T_WORD,4:4,24:28,"768px"
T_CLOSEBRACKET,4,29,")"
T_WHITESPACE,4,30," "
T_OPENCURLY,4,31,"{"
T_WHITESPACE,5,0,"\n      "
T_WORD,5:5,7:11,"color"
T_COLON,5,12,":"
T_WHITESPACE,5,13," "
T_WORD,5:5,14:16,"red"
T_SEMICOLON,5,17,";"
T_WHITESPACE,6,0,"\n    "
T_CLOSECURLY,6,5,"}"
T_WHITESPACE,7,0,"\n  "
T_CLOSECURLY,7,3,"}"
T_WHITESPACE,8,0,"\n  "
T_ATWORD,8:8,3:8,"@media"
T_WHITESPACE,8,9," "
T_WORD,8:8,10:11,"tv"
T_WHITESPACE,8,12," "
T_OPENCURLY,8,13,"{"
T_WHITESPACE,9,0,"\n    "
T_WORD,9:9,5:9,"color"
T_COLON,9,10,":"
T_WHITESPACE,9,11," "
T_WORD,9:9,12:16,"black"
T_SEMICOLON,9,17,";"
T_WHITESPACE,10,0,"\n  "
T_CLOSECURLY,10,3,"}"
T_WHITESPACE,11,0,"\n"
T_CLOSECURLY,11,1,"}"
