%{

#include <stdio.h>
#include <string.h>

void yyerror(const char *str)
{
        fprintf(stderr,"error: %s\n",str);
}
 
int yywrap()
{
        return 1;
} 
  
main()
{
        yyparse();
}

%}

%token GBKKEY VALUE END_OF_FILE

%%
gbkfile:
        gbkproperty;

gbkproperty:
           GBKKEY VALUE
           {
               printf("ok!%d\n",$1	);
           }
            
           
%%