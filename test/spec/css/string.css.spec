span { content: "f\"oo"; }
============TEST
T_WORD,1:1,1:4,"span"
T_WHITESPACE,1,5," "
T_OPENCURLY,1,6,"{"
T_WHITESPACE,1,7," "
T_WORD,1:1,8:14,"content"
T_COLON,1,15,":"
T_WHITESPACE,1,16," "
T_STRING,1:1,17:23,"\"f\\\"oo\""
T_SEMICOLON,1,24,";"
T_WHITESPACE,1,25," "
T_CLOSECURLY,1,26,"}"
