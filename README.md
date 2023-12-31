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

```
python local_run_parser.py
```

for you can run the syntatic moduler and the semantic, you will need run the **local_run_parser.py**, it call the yacc moduler created in the **yacc.py**. 

Para você rodar o modulo sintatico, você deve rodar o arquivo **lcoal_run_parser.py**, ele utilizará o yacc no arquivo **yacc.py** para criar as regras sintaticas e semânticas. 




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

#### SYNTATIC - ANALISADOR SINTÁTICO
About the syntatic we use the yacc for create the roles for verify the oder in the grammer, yacc use the LLAR for build the derivation tree. A semantic analyzer is a crucial tool in computational linguistics and natural language processing (NLP). Its primary function is to understand and interpret the meaning of texts or sentences. The semantic analyzer goes beyond grammatical analysis, which focuses on sentence structure, and aims to understand the contextual meaning and relationships between words.

To achieve this, the semantic analyzer employs algorithms and artificial intelligence models trained to recognize linguistic patterns and associate them with meanings. This approach enables machines to comprehend human language more deeply, facilitating applications such as automatic translation, virtual assistants, sentiment analysis in texts, and more.

The main challenge in semantic analysis is dealing with the ambiguity and variety of human language, necessitating ongoing improvements and adaptations in the models used.


#### SEMANTIC - ANALISADOR SEMÂNTICO
The yacc librarie allows us create the roles for verify context in the code. 

#### CODE GENERATION - GERADOR DE CÓDIGO

The code generation is the final part of the front end of our copiler, but in our project until this moment, we don't construct it, but if you wanna try, you can use the LLVM, it is a librarie for infraestruture project for compilers and he has a librarie for python. **(llvmlite)**

#### PROJECT MEMBERS/CONTACT

If you have any questions, please contact us, and if the project helped you, leave a star so that more people can find it! If there are changes or improvements, contribute to us so that more people have access to the compiled knowledge! Happy studying, **see you later and thanks for the fish!**

Se tiver alguma dúvida entre em contato conosco, e se o projeto te ajudou deixe uma estrela para que mais pessoas se encontrem! Se houver alterações ou melhorias, contribua conosco para que mais pessoas tenham acesso ao conhecimento em compilado! Bons estudos, **até logo e obrigado pelos peixes** 

- Arthur Laender De Paula - crashertn@gmail.com
- Hiroto Sato Tanaka - hirotosato12@gmail.com
- Harisson Douglas Siqueira Pires - harissonsiqueira@gmail.com
- Matheus Botelho Menezes dos Santos - matheus.botelho@unifei.edu

#### REFERENCES/REFERÊNCIAS 

https://www.dabeaz.com/ply/ply.html - The documentation base for the project 

https://youtu.be/6DoYU3LiM0A?si=0OB3OVstMdLB3mZI - Yotube video with informations about Ply 

 