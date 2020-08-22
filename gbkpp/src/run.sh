lex gbkformat.l
yacc -d gbkparser.y
gcc lex.yy.c y.tab.c -o parser