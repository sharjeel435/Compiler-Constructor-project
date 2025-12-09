
from lexer import tokenize 

from typing import List ,Tuple ,Dict ,Optional ,Any 

class ParseTreeNode :


    def __init__ (self ,node_type :str ,value :Any =None ):

        self .node_type =node_type 

        self .value =value 

        self .children :List ['ParseTreeNode']=[]

    def add_child (self ,child :'ParseTreeNode'):
        self .children .append (child )
        return self 

    def __repr__ (self ,level =0 ):
        indent ="  "*level 

        result =f"{indent }{self .node_type }"

        if self .value is not None :

            result +=f" ({self .value })"

        result +="\n"

        for child in self .children :

            result +=child .__repr__ (level +1 )

        return result 





class SymbolType :

    INTEGER ="INTEGER"

    FLOAT ="FLOAT"

    UNKNOWN ="UNKNOWN"



class Symbol :

    def __init__ (self ,name :str ,symbol_type :str =SymbolType .UNKNOWN ,

    value :Any =None ,initialized :bool =False ):

        self .name =name 

        self .symbol_type =symbol_type 

        self .value =value 

        self .initialized =initialized 

        self .line_declared =None 



    def __repr__ (self ):

        return f"Symbol({self .name }, {self .symbol_type }, initialized={self .initialized })"



class SymbolTable :

    """Manages variables and their properties"""

    def __init__ (self ):

        self .symbols :Dict [str ,Symbol ]={}

        self .errors :List [str ]=[]



    def declare (self ,name :str ,symbol_type :str =SymbolType .UNKNOWN )->bool :

        """Declare a new variable"""

        if name in self .symbols :

            self .errors .append (f"Variable '{name }' already declared")

            return False 



        self .symbols [name ]=Symbol (name ,symbol_type )

        return True 



    def lookup (self ,name :str )->Optional [Symbol ]:

        return self .symbols .get (name )



    def update (self ,name :str ,value :Any ,symbol_type :str =None )->bool :

        if name not in self .symbols :



            self .symbols [name ]=Symbol (name )



        symbol =self .symbols [name ]

        symbol .value =value 

        symbol .initialized =True 

        if symbol_type :

            symbol .symbol_type =symbol_type 

        return True 



    def get_all_symbols (self )->Dict [str ,Symbol ]:

        return self .symbols 



    def print_table (self ):

        print ("\n"+"="*60 )

        print ("SYMBOL TABLE")

        print ("="*60 )

        print (f"{'Variable':<15} {'Type':<12} {'Initialized':<12} {'Value':<12}")

        print ("-"*60 )

        for name ,symbol in self .symbols .items ():

            value_str =str (symbol .value )if symbol .value is not None else "N/A"

            print (f"{name :<15} {symbol .symbol_type :<12} {str (symbol .initialized ):<12} {value_str :<12}")

        print ("="*60 )


class SemanticAnalyzer :

    def __init__ (self ,symbol_table :SymbolTable ):

        self .symbol_table =symbol_table 

        self .errors :List [str ]=[]



    def analyze_assignment (self ,variable :str ,expr_value :Any ,expr_type :str ):

        symbol =self .symbol_table .lookup (variable )

        if symbol is None :

            self .symbol_table .declare (variable ,expr_type )
        self .symbol_table .update (variable ,expr_value ,expr_type )

    def infer_type (self ,value :Any )->str :

        if isinstance (value ,str ):
            try :

                if '.'in value :

                    float (value )

                    return SymbolType .FLOAT 

                else :

                    int (value )

                    return SymbolType .INTEGER 

            except ValueError :

                symbol =self .symbol_table .lookup (value )

                if symbol :

                    return symbol .symbol_type 

                return SymbolType .UNKNOWN 

        elif isinstance (value ,float ):

            return SymbolType .FLOAT 

        elif isinstance (value ,int ):

            return SymbolType .INTEGER 

        return SymbolType .UNKNOWN 



    def check_binary_operation (self ,left_type :str ,right_type :str ,operator :str )->str :

        if left_type ==SymbolType .FLOAT or right_type ==SymbolType .FLOAT :

            return SymbolType .FLOAT 

        elif left_type ==SymbolType .INTEGER and right_type ==SymbolType .INTEGER :

            if operator =='DIVIDE':

                return SymbolType .FLOAT 

            return SymbolType .INTEGER 

        return SymbolType .UNKNOWN 

    def check_identifier_usage (self ,identifier :str )->bool :

        symbol =self .symbol_table .lookup (identifier )

        if symbol is None :

            self .errors .append (f"Variable '{identifier }' used before declaration")

            return False 

        return True 

class EnhancedParser :

    def __init__ (self ,tokens :List [Tuple [str ,str ]]):

        self .tokens =tokens 

        self .current_token_index =0 

        self .temp_count =0 

        self .symbol_table =SymbolTable ()

        self .semantic_analyzer =SemanticAnalyzer (self .symbol_table )

        self .intermediate_code :List [str ]=[]

        self .type_info :Dict [str ,str ]={}

        self .parse_tree :Optional [ParseTreeNode ]=None 

    def current_token (self )->Optional [Tuple [str ,str ]]:

        return self .tokens [self .current_token_index ]if self .current_token_index <len (self .tokens )else None 

    def consume (self ):

        self .current_token_index +=1 
    def peek (self ,offset :int )->Optional [str ]:

        if self .current_token_index +offset <len (self .tokens ):

            return self .tokens [self .current_token_index +offset ][0 ]

        return None 

    def new_temp (self )->str :

        self .temp_count +=1 

        return f"t{self .temp_count }"

    def parse (self )->Tuple [ParseTreeNode ,List [str ]]:

        program_node =ParseTreeNode ("PROGRAM")
        while self .current_token ()is not None :

            prev_index =self .current_token_index 

            stmt =self .statement ()

            program_node .add_child (stmt )



            if self .current_token_index ==prev_index :

                break 

        self .parse_tree =program_node 

        return self .parse_tree ,self .intermediate_code 



    def statement (self )->ParseTreeNode :

        token =self .current_token ()
        stmt_node =ParseTreeNode ("STATEMENT")
        if token and token [0 ]=='IDENTIFIER'and self .peek (1 )=='ASSIGN':

            assign_node =self .variable_declaration ()

            stmt_node .add_child (assign_node )

        else :

            expr_node ,expr_value ,expr_type =self .expression ()

            stmt_node .add_child (expr_node )

        return stmt_node 
    def variable_declaration (self )->ParseTreeNode :

        assign_node =ParseTreeNode ("ASSIGNMENT")

        variable =self .current_token ()[1 ]

        var_node =ParseTreeNode ("IDENTIFIER",variable )

        assign_node .add_child (var_node )

        self .consume ()

        op_node =ParseTreeNode ("OPERATOR","=")

        assign_node .add_child (op_node )

        self .consume ()

        expr_node ,expr_value ,expr_type =self .expression ()

        assign_node .add_child (expr_node )

        self .semantic_analyzer .analyze_assignment (variable ,expr_value ,expr_type )

        self .intermediate_code .append (f"{variable } = {expr_value }")

        return assign_node 
    def expression (self )->Tuple [ParseTreeNode ,str ,str ]:

        expr_node =ParseTreeNode ("EXPRESSION")

        term_node ,term_value ,term_type =self .term ()

        expr_node .add_child (term_node )

        while self .current_token ()and self .current_token ()[0 ]in ('PLUS','MINUS'):

            operator =self .current_token ()[0 ]

            op_symbol ='+'if operator =='PLUS'else '-'

            op_node =ParseTreeNode ("OPERATOR",op_symbol )

            expr_node .add_child (op_node )

            self .consume ()

            right_term_node ,right_term_value ,right_term_type =self .term ()

            expr_node .add_child (right_term_node )

            result_type =self .semantic_analyzer .check_binary_operation (

            term_type ,right_term_type ,operator 

            )

            temp_var =self .new_temp ()

            self .intermediate_code .append (f"{temp_var } = {term_value } {op_symbol } {right_term_value }")

            self .type_info [temp_var ]=result_type 

            term_value =temp_var 

            term_type =result_type 

        return expr_node ,term_value ,term_type 

    def term (self )->Tuple [ParseTreeNode ,str ,str ]:

        term_node =ParseTreeNode ("TERM")

        factor_node ,factor_value ,factor_type =self .factor ()

        term_node .add_child (factor_node )

        while self .current_token ()and self .current_token ()[0 ]in ('TIMES','DIVIDE'):

            operator =self .current_token ()[0 ]

            op_symbol ='*'if operator =='TIMES'else '/'

            op_node =ParseTreeNode ("OPERATOR",op_symbol )

            term_node .add_child (op_node )

            self .consume ()

            right_factor_node ,right_factor_value ,right_factor_type =self .factor ()

            term_node .add_child (right_factor_node )

            result_type =self .semantic_analyzer .check_binary_operation (

            factor_type ,right_factor_type ,operator 

            )

            temp_var =self .new_temp ()

            self .intermediate_code .append (f"{temp_var } = {factor_value } {op_symbol } {right_factor_value }")

            self .type_info [temp_var ]=result_type 

            factor_value =temp_var 

            factor_type =result_type 


        return term_node ,factor_value ,factor_type 

    def factor (self )->Tuple [ParseTreeNode ,str ,str ]:

        token =self .current_token ()

        if token is None :

            raise SyntaxError ("Unexpected end of input while parsing factor")

        if token [0 ]=='NUMBER':
            value =token [1 ]

            factor_node =ParseTreeNode ("NUMBER",value )

            self .consume ()

            value_type =self .semantic_analyzer .infer_type (value )

            return factor_node ,value ,value_type 

        elif token [0 ]=='IDENTIFIER':

            identifier =token [1 ]

            factor_node =ParseTreeNode ("IDENTIFIER",identifier )

            self .consume ()

            symbol =self .symbol_table .lookup (identifier )

            if symbol :

                return factor_node ,identifier ,symbol .symbol_type 

            else :

                return factor_node ,identifier ,SymbolType .UNKNOWN 


        elif token [0 ]=='LPAREN':

            factor_node =ParseTreeNode ("FACTOR")

            lparen_node =ParseTreeNode ("LPAREN","(")

            factor_node .add_child (lparen_node )

            self .consume ()

            expr_node ,expr_value ,expr_type =self .expression ()

            factor_node .add_child (expr_node )

            if self .current_token ()and self .current_token ()[0 ]=='RPAREN':

                rparen_node =ParseTreeNode ("RPAREN",")")

                factor_node .add_child (rparen_node )

                self .consume ()

            else :

                raise SyntaxError ("Missing closing parenthesis")

            return factor_node ,expr_value ,expr_type 

        raise SyntaxError (f"Unexpected token: {token }")

    def get_parse_tree (self )->Optional [ParseTreeNode ]:

        return self .parse_tree 

    def print_analysis_results (self ):

        print ("\n")

        print ("PARSE TREE")

        print ("")

        if self .parse_tree is None :

            print ("No parse tree available. Did you call parse()?\n")

        else :

            print (self .parse_tree )


        self .symbol_table .print_table ()

        if self .semantic_analyzer .errors :

            print ("\n")

            print ("SEMANTIC ERRORS")

            print ("")

            for error in self .semantic_analyzer .errors :

                print (f"  ✗ {error }")

        else :

            print ("\n✓ No semantic errors detected")


        print ("\n")

        print ("THREE-ADDRESS CODE (Intermediate Representation)")

        print ("")

        for i ,line in enumerate (self .intermediate_code ,1 ):

            print (f"  {i }: {line }")

        print ("")


def main ():

    print ("MathScript Compiler - Part 2")

    print ("Enhanced Parser with Semantic Analysis")

    print ("")
    user_input =input ("\nEnter a MathScript expression (e.g., x = 3 + 5 * 2): ")

    try :

        print ("\nLEXICAL ANALYSIS (Part 1)\n")

        tokens =list (tokenize (user_input ))

        print ("Tokens:")

        for token in tokens :

            print (f"  {token }")

        print ("\nSYNTAX & SEMANTIC ANALYSIS (Part 2)\n")

        parser =EnhancedParser (tokens )

        parse_tree ,intermediate_code =parser .parse ()

        parser .print_analysis_results ()

        print ("\n✓ Compilation successful!")

    except SyntaxError as e :

        print (f"\n✗ Syntax Error: {e }")

    except RuntimeError as e :

        print (f"\n✗ Lexical Error: {e }")

    except Exception as e :

        print (f"\n✗ Error: {e }")

if __name__ =="__main__":

    main ()
