from lex import lexer
import ply.yacc as yacc
from yacc import parser

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

x = parser()



try:
    s = read_file('./lexer_tests/teste9.txt')
except EOFError:
    print("Error")
result = x.parser.parse(s)
print(result)
