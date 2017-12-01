@some: ~"( max-width: "@max~")";
============TEST
T_ATWORD,1:1,1:5,"@some"
T_COLON,1,6,":"
T_WHITESPACE,1,7," "
T_TILDE,1,8,"~"
T_STRING,1:1,9:23,"\"( max-width: \""
T_ATWORD,1:1,24:27,"@max"
T_TILDE,1,28,"~"
T_STRING,1:1,29:31,"\")\""
T_SEMICOLON,1,32,";"
