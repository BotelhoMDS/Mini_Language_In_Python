import ply.yacc as yacc
from lex import lexer

class parser(object):

    def __init__(self):
        self.lexer = lexer()
        self.lexer.build()
        self.tokens = self.lexer.tokens
        self.reserved = self.lexer.reserved
        self.parser = yacc.yacc(module=self)



    def p_program(self,p):
        '''program : PROGRAM ID body'''
        
    def p_body(self,p):
        '''body : DECLARE declaration_list BEGIN statement_list END'''

    def p_declaration_list(self,p):
        '''declaration_list : declaration declaration
                            | declaration'''
    def p_declaration(self,p):
        '''declaration : type identifier_list COMMA identifier_list SEMICOLON
                | type identifier_list SEMICOLON'''

    def p_type(self,p):
        '''type : INTEGER 
                | DECIMAL'''

    def p_identifier_list(self,p):
        '''identifier_list : ID COMMA identifier_list
                            | ID '''   

    def p_statement_list(self,p): #revisar depois 
        '''statement_list : statement statement_prime

                        ''' 
    def p_statement_prime(self,p):
        ''' statement_prime : statement
                            | SEMICOLON'''

    def p_statement(self,p):
        '''statement : assign_statement
                    | if_statement
                    | while_statement
                    | for_statement
                    | read_statement
                    | write_statement
                    | do_while_statement
                    '''
        
    def p_assign_statement(self,p):
        '''assign_statement : ID ASSIGN expression'''

    def p_if_statement(self,p):
        '''if_statement : IF condition THEN statement_list END
                        | IF condition THEN statement_list ELSE statement_list END'''

    def p_while_statement(self,p):
        '''while_statement : WHILE condition DO statement_list END'''
    
    def p_do_while_statement(self,p):
        '''do_while_statement : DO statement_list WHILE condition END'''

    def p_for_statement(self,p):
        '''for_statement : FOR assign_statement TO condition DO statement_list END'''

    def p_read_statement(self,p):
        '''read_statement : READ LPAREN ID RPAREN'''

    def p_write_statement(self,p):
        '''write_statement : WRITE LPAREN writable RPAREN'''
    def p_writable(self,p):
        '''writable : simple_expression
                        | literal'''
    def p_condition(self,p):
        '''condition : expression'''
    def p_expression(self,p):
        '''expression : simple_expression
                    | simple_expression relop simple_expression'''
    def p_relop(self,p):
        '''relop : EQUAL 
                | LESS 
                | LESSEQUAL 
                | GREATER 
                | GREATEREQUAL 
                | LESSGREATER'''

    def p_simple_expression(self,p):
        '''simple_expression : term
                            | LPAREN simple_expression RPAREN INTERROGATION simple_expression COLON simple_expression
                            | simple_expression addop term
                            | simple_expression mulop term
                            | LPAREN simple_expression RPAREN
                       '''

    def p_addop(self,p):
        '''addop : PLUS 
                | MINUS 
                | OR'''

    def p_mulop(self,p):
        '''mulop : MULTI 
                | DIVIDE 
                | MOD 
                | AND'''

    def p_term(self,p):
        '''term : factor_a
                | term mulop factor_a'''
        
    def p_factor_a(self,p):
        '''factor_a : factor 
                | NOT factor 
                | MINUS factor'''

    def p_factor(self,p):
        '''factor : ID 
                | NUMBER 
                | LPAREN expression RPAREN'''

    def p_literal(self,p):
        '''literal : LITERAL'''

   

    