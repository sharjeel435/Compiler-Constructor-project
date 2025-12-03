
"""
Run all test cases and display beautiful organized results.
"""
from lexer import Lexer 
from enhanced_parser import EnhancedParser 
from optimizer import Optimizer 
from code_generator import CodeGenerator 
from interpreter import Interpreter 


TEST_CASES =[
("counter = 15","counter = 15"),
("balance = 100 - 45","balance = 55"),
("average = (8 + 12) / 2","average = 10"),
("area = 5.5 * 3.2","area = 17.6"),
("total = 25 - 5 * 2 + 8 / 4","total = 17"),
("calculation = ((10 - 2) * (3 + 1)) / 4","calculation = 8"),
("value = 2.5 * (1.2 + 3.8) - 1.5","value = 11.0"),
("score = 5 * 3 + 10 / 2 - 4","score = 16"),
]

def run_test (code ,expected ):
    """Run a single test case through the full pipeline."""
    try :

        lexer =Lexer (code )
        tokens =lexer .tokenize ()


        enhanced =EnhancedParser (tokens )
        ast ,ir =enhanced .parse ()


        optimizer =Optimizer ()
        optimized_ir =optimizer .constant_folding (ir )
        optimized_ir =optimizer .dead_code_elimination (optimized_ir )


        code_gen =CodeGenerator ()
        final_code =code_gen .generate (optimized_ir )


        interpreter =Interpreter ()
        env =interpreter .run (final_code )


        user_vars ={k :v for k ,v in sorted (env .items ())if not k .startswith ('t')}


        passed =False 
        if expected :
            var_name ,expected_val =expected .split (' = ')
            var_name =var_name .strip ()
            if var_name in user_vars :
                try :
                    passed =float (user_vars [var_name ])==float (expected_val )
                except :
                    passed =str (user_vars [var_name ])==expected_val 

        return {
        'code':code ,
        'expected':expected ,
        'result':user_vars ,
        'passed':passed ,
        'ir_lines':len (ir ),
        'instructions':len (final_code )
        }
    except Exception as e :
        return {
        'code':code ,
        'expected':expected ,
        'result':None ,
        'passed':False ,
        'error':str (e ),
        'ir_lines':0 ,
        'instructions':0 
        }

def print_header ():
    """Print a beautiful header."""
    print ("\n"+"="*80 )
    print ("  MATHSCRIPT COMPILER - TEST SUITE RUNNER  ".center (80 ))
    print ("="*80 +"\n")

def print_test_result (num ,test ):
    """Print a single test result beautifully."""
    status ="✓ PASS"if test ['passed']else "✗ FAIL"
    status_color ="\033[92m"if test ['passed']else "\033[91m"
    reset_color ="\033[0m"

    print (f"Test {num }: {status_color }{status }{reset_color }")
    print (f"  Input:    {test ['code']}")
    print (f"  Expected: {test ['expected']}")

    if test ['result']is not None :
        result_str =', '.join ([f"{k }: {v }"for k ,v in test ['result'].items ()])
        print (f"  Result:   {{{result_str }}}")
        print (f"  IR Lines: {test ['ir_lines']} | Generated Instructions: {test ['instructions']}")
    else :
        print (f"  Error:    {test .get ('error','Unknown error')}")

    print ()

def print_summary (results ):
    """Print a summary of all tests."""
    passed =sum (1 for r in results if r ['passed'])
    total =len (results )

    print ("="*80 )
    print (f"  SUMMARY: {passed }/{total } tests passed  ".center (80 ))
    print ("="*80 )
    print ()


    for i ,(code ,expected ),result in zip (range (1 ,total +1 ),TEST_CASES ,results ):
        status ="✓"if result ['passed']else "✗"
        print (f"  [{status }] Test {i :1d}: {code :<50} → {result ['expected']}")

    print ()

def main ():
    """Run all tests and display results."""
    print_header ()

    results =[]
    for i ,(code ,expected )in enumerate (TEST_CASES ,1 ):
        print (f"\n{'─'*80 }")
        print (f"Test Case {i }/{len (TEST_CASES )}")
        print (f"{'─'*80 }\n")

        result =run_test (code ,expected )
        results .append (result )
        print_test_result (i ,result )

    print_summary (results )


    passed =sum (1 for r in results if r ['passed'])
    if passed ==len (results ):
        print ("  🎉 All tests passed! Compiler is working correctly.\n")
        return 0 
    else :
        failed =len (results )-passed 
        print (f"  ⚠️  {failed } test(s) failed. Review the output above.\n")
        return 1 

if __name__ =='__main__':
    exit (main ())
