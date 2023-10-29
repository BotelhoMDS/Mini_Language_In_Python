from lex import lexer
import ply.yacc as yacc


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

test_lexer = lexer()

test_lexer.build()
test_lexer.test(
    ' a = 3 + 4 -> aki234asd Esse ? é o _ if "Hello World" do Mini Language : in Python L3x3r '  
)

parse = yacc.yacc()

while True: 
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parse(s)
    print(result)

"""
if you want teste your owned file, just uncomment the code below and change the path to your file

test_lexer.test(
   read_file('./lexer_tests/teste1.txt')
)
"""