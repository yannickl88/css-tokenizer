.weird-element {
  content: ~"^//* some horrible but needed css hack";
}
============TEST
T_WORD,1:1,1:14,".weird-element"
T_WHITESPACE,1,15," "
T_OPENCURLY,1,16,"{"
T_WHITESPACE,1:2,17:2,"\n  "
T_WORD,2:2,3:9,"content"
T_COLON,2,10,":"
T_WHITESPACE,2,11," "
T_WORD,2:2,12:12,"~"
T_STRING,2:2,13:52,"\"^\/\/* some horrible but needed css hack\""
T_SEMICOLON,2,53,";"
T_WHITESPACE,2:3,54:0,"\n"
T_CLOSECURLY,3,1,"}"
