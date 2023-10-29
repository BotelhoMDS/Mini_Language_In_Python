import ply.lex as lex
from symbol_table import symbol_table, escope
import ply.yacc as yacc


class lexer(object):
    def __init__(self):
        self.lexer = None
        self.escope = escope()
        self.escope.push_stack() #created the global scope 

    # List of token names.   This is always required
    tokens = (
        'ID',  # Variables
        'LITERAL', # LITERALS
        'NUMBER',  # Numbers
        'PLUS',  # +
        'MINUS',  # -
        'MULTI',  # *
        'DIVIDE',  # /
        'LPAREN',  # (
        'RPAREN',  # )
        'COMMA',  # ,
        'SEMICOLON',  # ;
        'COLON',  # :
        'EQUAL',  # =
        'LESS',  # <
        'LESSEQUAL',  # <=
        'GREATER',  # >
        'GREATEREQUAL',  # >=
        'ASSIGN',  # :=
        'DOT',  # .
        'DOUBLEGREATER',  # >>
        'DOUBLELESS',  # <<
        'TRIPLELESS',  # <<<
        'TRIPLEGREATER',  # >>>
        'LESSGREATER',  # <>
        'IF',  # if
        'ELSE',  # else
        'THEN',  # then
        'WHILE',  # while
        'DO',  # do
        'FOR',  # for
        'TO',  # to
        'READ',  # read
        'WRITE',  # write
        'DECIMAL',  # Decimal numbers
        'INTEGER',  # Integer numbers
        'COMMENT',  # % comment
        'PROGRAM',  # Begin the program
        'DECLARE',  # Declare variables
        'BEGIN',  # Begin the program
        'END',  # End the program
        'AND',  # and
        'OR',  # or
        'NOT',  # not
        'MOD',  # mod , remainder of division
        'INTERROGATION',  # ?
    )

    reserved = {
        'if': 'IF',
        'else': 'ELSE',
        'while': 'WHILE',
        'for': 'FOR',
        'do': 'DO',
        'to': 'TO',
        'read': 'READ',
        'write': 'WRITE',
        'program': 'PROGRAM',
        'declare': 'DECLARE',
        'integer': 'INTEGER',
        'decimal': 'DECIMAL',
        'begin': 'BEGIN',
        'end': 'END',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'mod': 'MOD',
    }
    '''
    Functions for working with symbol table and scope 
    '''
    def new_scope(self): 
        self.escope.push_stack()
    
    def exit_scope(self):
        self.escope.pop_stack()
    
    def add_symbol(self, symbol, value):
        self.escope.current_table().add_symbol(symbol, value)

    def verify_symbol_in_this_scope(self, symbol):
        return self.escope.current_table().verify_symbol(symbol)
    def get_symbol(self, symbol): # run in the scopes from the actual for the global 
        for table in reversed(self.escope.table_stack):
            if table.verify_symbol(symbol):
                return table.get_symbol(symbol)
        return None

    def print_current_scope(self):
        print(self.escope.current_table())

    """
        Regular expression rules for simple tokens
    """
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_MULTI = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_COMMA = r','
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_EQUAL = r'='
    t_LESS = r'<'
    t_GREATER = r'>'
    t_ASSIGN = r':='
    t_DOT = r'\.'
    t_DOUBLEGREATER = r'>>'
    t_DOUBLELESS = r'<<'
    t_TRIPLELESS = r'<<<'
    t_TRIPLEGREATER = r'>>>'
    t_LESSGREATER = r'<>'
    t_INTERROGATION = r'\?'

    t_ignore = ' \t'

    """
        Regular expression rules with some action code/Regras de expressão regular com algum código de ação
    """

    def t_ID(self, t):
        r"""[a-zA-Z][a-zA-Z0-9]*"""
        t.type = self.reserved.get(t.value, 'ID')    # Check for reserved words
        if t.type == 'ID':
            if not self.verify_symbol_in_this_scope(t.value): #dont't add the symbol if it already exists
                self.add_symbol(t.value, value=None) # add a new symbol to the symbol table
        return t
    
    def t_LITERAL(self, t):
        r'\"[^"]*\"'
        return t
    def t_NUMBER(self, t):
        r"""\d+"""
        t.value = int(t.value)
        return t

    def t_DECIMAL(self, t):
        r"""\d+\.\d+"""
        t.value = float(t.value)
        return t

    def t_newline(self, t):
        r"""\n+"""
        t.lexer.lineno += len(t.value)

    def t_COMMENT(self, t):
        r"""\%.*"""
        pass
        # No return value. Token discarded

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    '''
    Lexer functions 
    '''
    
    
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

        print(f"SYMBOL TABLE")
        self.print_current_scope()

    def unit_test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            yield tok.type

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
