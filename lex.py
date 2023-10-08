import ply.lex as lex


class lexer(object):
    # List of token names.   This is always required
    tokens = (
        'ID',  # Variables
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
    }

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

    t_ignore = ' \t'

    """
        Regular expression rules with some action code/Regras de expressão regular com algum código de ação
    """

    def t_ID(self, t):
        r"""[a-zA-Z_][a-zA-Z_0-9]*"""
        t.type = self.reserved.get(t.value, 'ID')    # Check for reserved words
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

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

    def unit_test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            yield tok.type

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
