import re 


token_specification =[
('NUMBER',r'\d+\.\d+|\d+'),
('IDENTIFIER',r'[A-Za-z][A-Za-z0-9]*'),
('PLUS',r'\+'),
('MINUS',r'-'),
('TIMES',r'\*'),
('DIVIDE',r'/'),
('ASSIGN',r'='),
('LPAREN',r'\('),
('RPAREN',r'\)'),
('SKIP',r'[ \t\n]+'),
('MISMATCH',r'.'),
]

def tokenize (code ):
    for mo in re .finditer ('|'.join (f'(?P<{pair [0 ]}>{pair [1 ]})'for pair in token_specification ),code ):
        kind =mo .lastgroup 
        value =mo .group ()
        if kind =='SKIP':
            continue 
        elif kind =='MISMATCH':
            raise RuntimeError (f'{value !r } unexpected')
        yield kind ,value 


class Lexer :
    """Simple Lexer wrapper that provides `tokenize()` as a method.

    Keeps the original `tokenize` generator for other modules.
    """
    def __init__ (self ,source_code :str ):
        self .source_code =source_code 
        self ._tokens =None 

    def tokenize (self ):
        self ._tokens =list (tokenize (self .source_code ))
        return self ._tokens 
