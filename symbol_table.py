import ply.lex as lex

class symbol_table:
    
    def __init__(self):
        self.table = {}

    def __str__(self):
        return str(self.table)
        
    
    #add a new symbol to the table and your value if it doesn't exist
    def add_symbol(self, symbol, value,type = None):
        if symbol not in self.table:
            self.table[symbol] = {"Value":value,"Type":type}
        else:
            raise Exception(f"{symbol} has already been declared")

    #verify if the symbol exists in the table
    def verify_symbol(self, symbol):
        return symbol in self.table
    
    #get the value of the symbol if it exists
    def get_symbol(self, symbol):
        if symbol in self.table:
            return self.table[symbol]
        else:
            raise Exception(f"{symbol} has not been declared")
    
    #remove the symbol from the table if it exists
    def remove_symbol(self, symbol):
        del self.table[symbol]

class escope: 
    def __init__(self):
        self.table_stack = []
    
    def push_stack(self):
        self.table_stack.append(symbol_table())

    def pop_stack(self):
        if self.table_stack:
            self.table_stack.pop()
        else:
            raise Exception("The stack of symbol table is empty")
    
    def current_table(self):
        if self.table_stack:
            return self.table_stack[-1]
        else:
            raise Exception("The stack of symbol table is empty")