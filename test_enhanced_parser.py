"""
MathScript Compiler - Part 2 Test Suite
Comprehensive test cases for Parser, Semantic Analyzer, and Code Generator
"""

from lexer import tokenize 
from enhanced_parser import EnhancedParser ,SymbolTable 
import sys 

class TestCase :
    """Represents a single test case"""
    def __init__ (self ,name :str ,input_code :str ,description :str ,
    expected_variables :dict =None ,should_pass :bool =True ):
        self .name =name 
        self .input_code =input_code 
        self .description =description 
        self .expected_variables =expected_variables or {}
        self .should_pass =should_pass 
        self .result =None 
        self .errors =[]

class TestSuite :
    """Test suite for Part 2 components"""

    def __init__ (self ):
        self .tests =[]
        self .passed =0 
        self .failed =0 
        self .setup_tests ()

    def setup_tests (self ):
        """Define all test cases"""


        self .tests .append (TestCase (
        name ="TC1: Simple Assignment",
        input_code ="x = 5",
        description ="Basic variable assignment with integer",
        expected_variables ={"x":("INTEGER",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC2: Float Assignment",
        input_code ="pi = 3.14",
        description ="Variable assignment with floating-point number",
        expected_variables ={"pi":("FLOAT",True )},
        should_pass =True 
        ))


        self .tests .append (TestCase (
        name ="TC3: Addition",
        input_code ="sum = 10 + 20",
        description ="Addition operation",
        expected_variables ={"sum":("INTEGER",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC4: Subtraction",
        input_code ="diff = 100 - 45",
        description ="Subtraction operation",
        expected_variables ={"diff":("INTEGER",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC5: Multiplication",
        input_code ="product = 5 * 3",
        description ="Multiplication operation",
        expected_variables ={"product":("INTEGER",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC6: Division",
        input_code ="quotient = 10 / 2",
        description ="Division operation (always produces float)",
        expected_variables ={"quotient":("FLOAT",True )},
        should_pass =True 
        ))


        self .tests .append (TestCase (
        name ="TC7: Integer + Float",
        input_code ="result = 5 + 2.5",
        description ="Mixed type addition (should result in FLOAT)",
        expected_variables ={"result":("FLOAT",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC8: Float * Integer",
        input_code ="area = 5.5 * 3",
        description ="Mixed type multiplication",
        expected_variables ={"area":("FLOAT",True )},
        should_pass =True 
        ))


        self .tests .append (TestCase (
        name ="TC9: Precedence Test 1",
        input_code ="result = 2 + 3 * 4",
        description ="Multiplication before addition",
        expected_variables ={"result":("INTEGER",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC10: Precedence Test 2",
        input_code ="result = 10 - 2 * 3",
        description ="Multiplication before subtraction",
        expected_variables ={"result":("INTEGER",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC11: Division Precedence",
        input_code ="result = 20 / 4 + 2",
        description ="Division before addition",
        expected_variables ={"result":("FLOAT",True )},
        should_pass =True 
        ))


        self .tests .append (TestCase (
        name ="TC12: Simple Parentheses",
        input_code ="result = (5 + 3) * 2",
        description ="Parentheses override precedence",
        expected_variables ={"result":("INTEGER",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC13: Nested Parentheses",
        input_code ="result = ((10 - 2) * (3 + 1)) / 4",
        description ="Multiple levels of nested parentheses",
        expected_variables ={"result":("FLOAT",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC14: Complex Grouping",
        input_code ="result = (8 + 12) / 2",
        description ="Division with grouped numerator",
        expected_variables ={"result":("FLOAT",True )},
        should_pass =True 
        ))


        self .tests .append (TestCase (
        name ="TC15: Multiple Operations",
        input_code ="result = 25 - 5 * 2 + 8 / 4",
        description ="Chain of multiple operations",
        expected_variables ={"result":("FLOAT",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC16: Mixed Float Expression",
        input_code ="value = 2.5 * (1.2 + 3.8) - 1.5",
        description ="Complex expression with floats",
        expected_variables ={"value":("FLOAT",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC17: Long Expression",
        input_code ="score = 5 * 3 + 10 / 2 - 4",
        description ="Long chained expression",
        expected_variables ={"score":("FLOAT",True )},
        should_pass =True 
        ))


        self .tests .append (TestCase (
        name ="TC18: Decimal Multiplication",
        input_code ="area = 5.5 * 3.2",
        description ="Multiplication of two floats",
        expected_variables ={"area":("FLOAT",True )},
        should_pass =True 
        ))

        self .tests .append (TestCase (
        name ="TC19: Decimal Addition",
        input_code ="total = 10.5 + 20.3",
        description ="Addition of floating-point numbers",
        expected_variables ={"total":("FLOAT",True )},
        should_pass =True 
        ))


        self .tests .append (TestCase (
        name ="TC20: Single Number",
        input_code ="constant = 42",
        description ="Assignment of single number",
        expected_variables ={"constant":("INTEGER",True )},
        should_pass =True 
        ))

    def run_test (self ,test :TestCase ):
        """Run a single test case"""
        try :

            tokens =list (tokenize (test .input_code ))


            parser =EnhancedParser (tokens )
            parse_tree ,intermediate_code =parser .parse ()


            if parser .semantic_analyzer .errors :
                if test .should_pass :
                    test .result ="FAIL"
                    test .errors =parser .semantic_analyzer .errors 
                    return False 
                else :
                    test .result ="PASS"
                    return True 


            symbol_table =parser .symbol_table .get_all_symbols ()

            for var_name ,(expected_type ,expected_init )in test .expected_variables .items ():
                if var_name not in symbol_table :
                    test .result ="FAIL"
                    test .errors .append (f"Variable '{var_name }' not found in symbol table")
                    return False 

                symbol =symbol_table [var_name ]
                if symbol .symbol_type !=expected_type :
                    test .result ="FAIL"
                    test .errors .append (
                    f"Type mismatch for '{var_name }': expected {expected_type }, got {symbol .symbol_type }"
                    )
                    return False 

                if symbol .initialized !=expected_init :
                    test .result ="FAIL"
                    test .errors .append (
                    f"Initialization mismatch for '{var_name }': expected {expected_init }, got {symbol .initialized }"
                    )
                    return False 

            test .result ="PASS"
            return True 

        except Exception as e :
            test .result ="FAIL"
            test .errors .append (f"Exception: {str (e )}")
            return False 

    def run_all_tests (self ):
        """Run all test cases"""
        print ("="*80 )
        print ("MathScript Compiler - Part 2 Test Suite")
        print ("="*80 )
        print (f"Running {len (self .tests )} test cases...\n")

        for i ,test in enumerate (self .tests ,1 ):
            print (f"[{i }/{len (self .tests )}] {test .name }")
            print (f"    Input: {test .input_code }")
            print (f"    Description: {test .description }")

            if self .run_test (test ):
                print (f"    Result: ✓ PASS")
                self .passed +=1 
            else :
                print (f"    Result: ✗ FAIL")
                for error in test .errors :
                    print (f"           {error }")
                self .failed +=1 
            print ()


        print ("="*80 )
        print ("TEST SUMMARY")
        print ("="*80 )
        print (f"Total Tests: {len (self .tests )}")
        print (f"Passed: {self .passed } ({self .passed /len (self .tests )*100 :.1f}%)")
        print (f"Failed: {self .failed } ({self .failed /len (self .tests )*100 :.1f}%)")
        print ("="*80 )

        return self .failed ==0 

def run_detailed_test (test_input :str ):
    """Run a detailed test showing all phases"""
    print ("\n"+"="*80 )
    print (f"DETAILED TEST: {test_input }")
    print ("="*80 )

    try :

        print ("\n1. LEXICAL ANALYSIS")
        print ("-"*80 )
        tokens =list (tokenize (test_input ))
        print ("Tokens:")
        for token in tokens :
            print (f"  {token }")


        print ("\n2. SYNTAX & SEMANTIC ANALYSIS")
        print ("-"*80 )
        parser =EnhancedParser (tokens )
        parse_tree ,intermediate_code =parser .parse ()


        print ("\nParse Tree:")
        print (parse_tree )


        parser .symbol_table .print_table ()


        if parser .semantic_analyzer .errors :
            print ("\nSemantic Errors:")
            for error in parser .semantic_analyzer .errors :
                print (f"  ✗ {error }")
        else :
            print ("\n✓ No semantic errors")


        print ("\n3. INTERMEDIATE CODE GENERATION")
        print ("-"*80 )
        print ("Three-Address Code:")
        for i ,line in enumerate (intermediate_code ,1 ):
            print (f"  {i }: {line }")

        print ("\n"+"="*80 )
        print ("✓ Test completed successfully!")
        print ("="*80 )

    except Exception as e :
        print (f"\n✗ Error: {e }")
        import traceback 
        traceback .print_exc ()

def main ():
    """Main test runner"""
    print ("MathScript Compiler - Part 2 Testing\n")
    print ("Choose an option:")
    print ("1. Run full test suite")
    print ("2. Run detailed test on custom input")
    print ("3. Run detailed test on predefined examples")

    choice =input ("\nEnter choice (1-3): ").strip ()

    if choice =="1":
        suite =TestSuite ()
        success =suite .run_all_tests ()
        sys .exit (0 if success else 1 )

    elif choice =="2":
        test_input =input ("\nEnter MathScript expression: ")
        run_detailed_test (test_input )

    elif choice =="3":
        examples =[
        "x = 5",
        "result = 2 + 3 * 4",
        "area = (5 + 3) * 2",
        "value = 2.5 * (1.2 + 3.8) - 1.5",
        "complex = ((10 - 2) * (3 + 1)) / 4"
        ]

        for example in examples :
            run_detailed_test (example )
            input ("\nPress Enter to continue to next test...")

    else :
        print ("Invalid choice!")

if __name__ =="__main__":
    main ()