%{
#include <stdio.h>
#include "y.tab.h"
%}

%%
[ \t\n]+	;
LOCUS	return GBKKEY;
[a-zA-Z0-9_][a-zA-Z0-9_\n]+	return VALUE;
<<EOF>>     return END_OF_FILE;
%%