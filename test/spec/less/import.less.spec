@import (optional, reference) "foo.less";
============TEST
T_ATWORD,1:1,1:7,"@import"
T_WHITESPACE,1,8," "
T_OPENBRACKET,1,9,"("
T_WORD,1:1,10:17,"optional"
T_COMMA,1,18,","
T_WHITESPACE,1,19," "
T_WORD,1:1,20:28,"reference"
T_CLOSEBRACKET,1,29,")"
T_WHITESPACE,1,30," "
T_STRING,1:1,31:40,"\"foo.less\""
T_SEMICOLON,1,41,";"
