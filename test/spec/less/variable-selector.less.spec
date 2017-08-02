@my-selector: banner;

.@{my-selector} {
  font-weight: bold;
  line-height: 40px;
  margin: 0 auto;
}
============TEST
T_ATWORD,1:1,1:12,"@my-selector"
T_COLON,1,13,":"
T_WHITESPACE,1,14," "
T_WORD,1:1,15:20,"banner"
T_SEMICOLON,1,21,";"
T_WHITESPACE,3,0,"\n\n"
T_WORD,3:3,2:2,"."
T_ATWORD,3:3,3:3,"@"
T_OPENCURLY,3,4,"{"
T_WORD,3:3,5:15,"my-selector"
T_CLOSECURLY,3,16,"}"
T_WHITESPACE,3,17," "
T_OPENCURLY,3,18,"{"
T_WHITESPACE,4,0,"\n  "
T_WORD,4:4,3:13,"font-weight"
T_COLON,4,14,":"
T_WHITESPACE,4,15," "
T_WORD,4:4,16:19,"bold"
T_SEMICOLON,4,20,";"
T_WHITESPACE,5,0,"\n  "
T_WORD,5:5,3:13,"line-height"
T_COLON,5,14,":"
T_WHITESPACE,5,15," "
T_WORD,5:5,16:19,"40px"
T_SEMICOLON,5,20,";"
T_WHITESPACE,6,0,"\n  "
T_WORD,6:6,3:8,"margin"
T_COLON,6,9,":"
T_WHITESPACE,6,10," "
T_WORD,6:6,11:11,"0"
T_WHITESPACE,6,12," "
T_WORD,6:6,13:16,"auto"
T_SEMICOLON,6,17,";"
T_WHITESPACE,7,0,"\n"
T_CLOSECURLY,7,1,"}"
