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
        '''declaration_list : declaration SEMICOLON declaration_list_aux'''

    def p_declaration_list_aux(self,p):#Auxiliar pra evitar ambiguidade
        '''declaration_list_aux : declaration_list
                            | empty'''
        p[0] = p[1]
    
    def p_declaration(self,p):
        '''declaration : type identifier_list'''
        for t in p[2]:
            if not self.lexer.verify_symbol_in_this_scope(t): #dont't add the symbol if it already exists
                self.lexer.add_symbol(t, value=None) # add a new symbol to the symbol table

    def p_identifier_list(self,p):#VERIFICAR
        '''identifier_list : ID identifier_list_aux'''  
        p[0]=p[1]
        #self.type = p[1].type

    def p_identifier_list_aux(self,p):
        '''identifier_list_aux : COMMA identifier_list
                            | empty '''  
        if (len(p) == 3):
            p[0] = p[2]
        elif (len(p) == 2):
            p[0] = p[1]

    def p_type(self,p):
        '''type : INTEGER 
                | DECIMAL'''
        p[0] = p[1]

    def p_statement_list(self,p): #revisar depois 
        '''statement_list : statement SEMICOLON statement_prime'''
        p[0]=[1] 
    def p_statement_prime(self,p):
        ''' statement_prime : statement_list
                            | empty'''
        p[0] = p[1]

    def p_statement(self,p):
        '''statement : assign_statement
                    | if_statement
                    | while_statement
                    | for_statement
                    | read_statement
                    | write_statement
                    | do_while_statement
                    '''
        p[0]=p[1]

    def p_assign_statement(self,p):#Voltar pra revisar
        '''assign_statement : ID ASSIGN expression'''

    def p_if_statement(self,p):
        '''if_statement : IF condition THEN statement_list if_statement_aux'''


    def p_if_statement_aux(self,p):
        '''if_statement_aux : END
                        | ELSE statement_list END'''

    def p_while_statement(self,p):
        '''while_statement : WHILE condition DO statement_list END'''
    
    def p_do_while_statement(self,p):
        '''do_while_statement : DO statement_list do_while_statement_suffix'''

    def p_do_while_statement_suffix(self,p):
        '''do_while_statement_suffix : WHILE condition'''

    def p_for_statement(self,p):
        '''for_statement : FOR assign_statement TO condition DO statement_list END'''

    def p_read_statement(self,p):
        '''read_statement : READ LPAREN ID RPAREN'''
        
    def p_write_statement(self,p):
        '''write_statement : WRITE LPAREN writable RPAREN'''
        

    def p_writable(self,p):
        '''writable : simple_expression
                        | literal'''
        p[0]=p[1]

    def p_condition(self,p):
        '''condition : expression'''
        if p[1] == True or p[1] == False:
            p[0] = p[1]

    def p_expression(self,p):
        '''expression : simple_expression expression_aux'''

    def p_expression_aux(self,p):
        '''expression_aux : relop simple_expression
                    | empty'''
        
        p[0]=p[1]
    def p_relop(self,p):
        '''relop : EQUAL 
                | LESS 
                | LESSEQUAL 
                | GREATER 
                | GREATEREQUAL 
                | LESSGREATER'''
        p[0]=p[1]

    def p_par_expression(self,p):
        '''par_expression : LPAREN expression RPAREN'''
        p[0]=p[2]
        
    def p_simple_expression(self,p):
        '''simple_expression : term
                            | par_expression INTERROGATION simple_expression COLON simple_expression
                            | simple_expression addop term'''
        if (len(p) == 2):#term
            p[0]=p[1]


    def p_addop(self,p):
        '''addop : PLUS 
                | MINUS 
                | OR'''
        p[0]=p[1]

    def p_mulop(self,p):
        '''mulop : MULTI 
                | DIVIDE 
                | MOD 
                | AND'''
        p[0]=p[1]

    def p_term(self,p):
        '''term : factor_a
                | term mulop factor_a'''
        if (len(p) == 2):
            p[0]=p[1]

    def p_factor_a(self,p):#Ver depois
        '''factor_a : factor 
                | NOT factor 
                | MINUS factor'''
        if (len(p) == 2):
            p[0]=p[1]
        elif p[1] == 'not':
            p[0] = not p[1]
        elif p[1] == '-':
            p[0] = -p[1]

    def p_factor(self,p):
        '''factor : ID 
                | NUMBER 
                | par_expression'''

    def p_literal(self,p):
        '''literal : LITERAL'''
        p[0]=p[1]

    def p_empty(self,p): #Produções vazias, usado para retirar ambiguidades em certas regras como p_declaration_list
        'empty :'
        pass

    def p_error(self,p):
        print(f'Syntax error at {p.value!r}')

    
