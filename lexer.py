import re

# Regular expressions for tokens
token_specification = [
    ('NUMBER',    r'\d+\.\d+|\d+'),  # Integer or floating-point number
    ('IDENTIFIER', r'[A-Za-z][A-Za-z0-9]*'),  # Identifiers (e.g., x, y)
    ('PLUS',      r'\+'),          # Addition operator
    ('MINUS',     r'-'),           # Subtraction operator
    ('TIMES',     r'\*'),          # Multiplication operator
    ('DIVIDE',    r'/'),           # Division operator
    ('ASSIGN',    r'='),           # Assignment operator
    ('LPAREN',    r'\('),          # Left Parenthesis
    ('RPAREN',    r'\)'),          # Right Parenthesis
    ('SKIP',      r'[ \t\n]+'),    # Skip spaces and tabs
    ('MISMATCH',  r'.'),           # Any other character
]

def tokenize(code):
    for mo in re.finditer('|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification), code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected')
        yield kind, value
