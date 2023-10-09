# Mini_Language_In_Python
The final project for the discipline ECOI26 - Compiler  

#### How to run the project - Como rodar o projeto
To run the project, install the following packages in your virtual environment:
Para rodar o projeto, instale os seguintes pacotes no seu ambiente virtual:


```
pip install ply

```

```
pip intall pytest

```
in the terminal, run the following command:
no terminal, rode o seguinte comando:

```
python3 local_run.py
```


You can see the test wrinting in **local_run.py** file in the line six. 
if you want to run another test, just change the name of the file in the line six.
you can put a text file for teste, change the string in test for the function read_file like in the line fourteen.

Você pode ver o teste escrito no arquivo **local_run.py** na linha seis.
se você quiser rodar outro teste, apenas mude o nome do arquivo na linha seis.
você pode colocar um arquivo de texto para teste, mude a string no teste para a função read_file como na linha quatorze.




for run the test, run the following command in the terminal:

```
pytest test_lexer.py 
```

#### THE GRAMMAR OF MINI LANGUAGE - A GRAMÁTICA DA LINGUAGEM MINI


| Símbolo  (symbol)  | Regra de Produção   (Production rule)                |
|------------|-----------------------------------|
| program    | ::= program identifier body         |
| body       | ::= [declare decl-list] begin stmt-list end |
| decl-list  | ::= decl {";" decl}*               |
| decl       | ::= type ident-list                |
| ident-list | ::= identifier {"," identifier}*  |
| type       | ::= integer | decimal             |
| stmt-list  | ::= stmt {";" stmt}*               |
| stmt       | ::= assign-stmt | if-stmt | while-stmt | read-stmt | write-stmt |
| assign-stmt | ::= identifier ":=" simple_expr  |
| if-stmt    | ::= if condition then stmt-list end |
|            | ::= if condition then stmt-list else stmt-list end |
| condition  | ::= expression                    |
| do-while-stmt | ::= do stmt-list stmt-suffix     |
| stmt-suffix | ::= while condition               |
| for-stmt   | ::= for assign-stmt to condition do stmt-list end |
|            | ::= while condition do stmt-list end |
| read-stmt  | ::= read "(" identifier ")"       |
| write-stmt | ::= write "(" writable ")"        |
| writable   | ::= simple-expr | literal         |
| expression | ::= simple-expr | simple-expr relop simple-expr |
| simple-expr | ::= term | simple-expr addop term | "(" simple-expr ")" ? simple-expr ":" simple-expr |
| term       | ::= factor-a | term mulop factor-a |
| factor-a   | ::= factor | not factor | "-" factor |
| factor     | ::= identifier | constant | "(" expression ")" |
| relop      | ::= "=" | ">" | ">=" | "<" | "<=" | "<>" |
| addop      | ::= "+" | "-" | or               |
| mulop      | ::= "*" | "/" | mod | and        |
| shiftop    | ::= "<<" | ">>" | "<<<" | ">>>"  |
| constant   | ::= digit {digit}*               |
| literal    | ::= " “" {caractere} "”"         |
| identifier | ::= letter {letter | digit}*     |
| letter     | ::= ... (list of letters)        |
| digit      | ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| caractere  | ::= ... (list of ASCII characters, except " ) |


#### LEXER - ANALISADOR LÉXICO
About the lexer constrution and model, we use the PLY package, this package is a python package criated for the construction of lexers and parsers, it use lex and yacc to do this.

in the lexer we created the tokens and the rules for the tokens, the tokens are the symbols of the language, like the operators, the reserved words, the identifiers, the numbers, etc. the rules are the regular expressions that define the tokens in the text file. We as too the symbol table, who is reposible for save the identifiers in the text file for each escope.

