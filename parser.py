from lexer import tokenize 

class Parser :
    def __init__ (self ,tokens ):
        self .tokens =tokens 
        self .current_token_index =0 
        self .temp_count =0 

    def current_token (self ):
        return self .tokens [self .current_token_index ]if self .current_token_index <len (self .tokens )else None 

    def consume (self ):
        self .current_token_index +=1 

    def parse (self ):
        return self .statement ()

    def statement (self ):
        token =self .current_token ()
        if token and token [0 ]=='IDENTIFIER'and self .peek (1 )=='ASSIGN':
            return self .variable_declaration ()
        return self .expression ()

    def variable_declaration (self ):
        variable =self .current_token ()[1 ]
        self .consume ()
        self .consume ()
        expr ,code =self .expression ()
        return ('assign',variable ,expr ),code 

    def expression (self ):
        term ,code =self .term ()
        while self .current_token ()and self .current_token ()[0 ]in ('PLUS','MINUS'):
            operator =self .current_token ()[0 ]
            self .consume ()
            right_term ,right_code =self .term ()
            temp_var =self .new_temp ()
            code +=right_code 
            code .append (f"{temp_var } = {term } {operator } {right_term }")
            term =temp_var 
        return term ,code 

    def term (self ):
        factor ,code =self .factor ()
        while self .current_token ()and self .current_token ()[0 ]in ('TIMES','DIVIDE'):
            operator =self .current_token ()[0 ]
            self .consume ()
            right_factor ,right_code =self .factor ()
            temp_var =self .new_temp ()
            code +=right_code 
            code .append (f"{temp_var } = {factor } {operator } {right_factor }")
            factor =temp_var 
        return factor ,code 

    def factor (self ):
        token =self .current_token ()
        if token [0 ]=='NUMBER':
            self .consume ()
            return token [1 ],[]
        elif token [0 ]=='IDENTIFIER':
            self .consume ()
            return token [1 ],[]
        elif token [0 ]=='LPAREN':
            self .consume ()
            expr ,code =self .expression ()
            if self .current_token ()and self .current_token ()[0 ]=='RPAREN':
                self .consume ()
            return expr ,code 
        raise SyntaxError ("Unexpected token")

    def peek (self ,offset ):
        if self .current_token_index +offset <len (self .tokens ):
            return self .tokens [self .current_token_index +offset ][0 ]
        return None 

    def new_temp (self ):

        self .temp_count +=1 
        return f"t{self .temp_count }"


user_input =input ("Enter a math expression (e.g., x*3+9=4): ")


tokens =list (tokenize (user_input ))


parser =Parser (tokens )
ast ,intermediate_code =parser .parse ()


print ("AST:",ast )


print ("\nIntermediate Code:")
for line in intermediate_code :
    print (line )
