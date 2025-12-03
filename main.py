

from lexer import Lexer 

import re 

import argparse 

from enhanced_parser import EnhancedParser 

from optimizer import Optimizer 

from code_generator import CodeGenerator 

from interpreter import Interpreter 

import os 

import sys 



def compile_and_run (source_code ,verbose =True ):

    if verbose :

        print ("="*70 )

        print ("MATHSCRIPT COMPILER - FULL PIPELINE")

        print ("="*70 )

        print (f"\nInput Code:\n{source_code }\n")





    lexer =Lexer (source_code )

    tokens =lexer .tokenize ()



    if verbose :

        print ("Tokens:")

        print (tokens )





    enhanced =EnhancedParser (tokens )

    ast ,ir =enhanced .parse ()



    if verbose :

        print ("\nIntermediate Code (Three-Address):")

        for line in ir :

            print (f"  {line }")





    optimizer =Optimizer ()

    optimized_ir =optimizer .constant_folding (ir )

    optimized_ir =optimizer .dead_code_elimination (optimized_ir )



    if verbose :

        print ("\nOptimized Code:")

        for line in optimized_ir :

            print (f"  {line }")





    code_gen =CodeGenerator ()

    final_code =code_gen .generate (optimized_ir )



    if verbose :

        print ("\nGenerated Instructions:")

        for line in final_code :

            print (f"  {line }")





    interpreter =Interpreter ()

    env =interpreter .run (final_code )





    user_vars ={k :v for k ,v in sorted (env .items ())if not re .match (r'^t\d+$',k )}



    if verbose :

        print ("\nFinal Result:")

        print (f"  {user_vars }")

        print ("="*70 +"\n")



    return user_vars 



def parse_test_cases_from_md (md_path ):

    with open (md_path ,'r',encoding ='utf-8')as f :

        lines =f .readlines ()



    tests =[]

    cur_input =None 

    cur_expected =None 

    for line in lines :

        stripped =line .strip ()

        if stripped .startswith ('**Input:**'):



            m =re .search (r'`([^`]*)`',stripped )

            if m :

                cur_input =m .group (1 ).strip ()

            else :

                cur_input =stripped .split ('**Input:**',1 )[1 ].strip ()

        elif stripped .startswith ('**Expected Output:**'):

            val =stripped .split ('**Expected Output:**',1 )[1 ].strip ()

            cur_expected =val 

        elif stripped =='---':

            if cur_input is not None and cur_expected is not None :

                tests .append ((cur_input ,cur_expected ))

            cur_input =None 

            cur_expected =None 





    if cur_input is not None and cur_expected is not None :

        tests .append ((cur_input ,cur_expected ))



    return tests 





def run_tests (md_path ,show_all =False ):

    tests =parse_test_cases_from_md (md_path )

    total =len (tests )

    passed =0 

    print (f"Running {total } tests from {md_path }")

    for idx ,(inp ,expected )in enumerate (tests ,start =1 ):



        try :

            result =compile_and_run (inp ,verbose =True )

        except Exception as e :

            print (f"Test {idx }: ERROR running pipeline for input: {inp }")

            print ("Exception:",e )

            continue 





        actual_repr =None 

        if isinstance (result ,dict ):



            m =re .match (r"\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=",inp )

            if m :

                var =m .group (1 )

                actual_repr =f"{var } = {result .get (var )}"

            else :

                actual_repr =str (result )

        else :

            actual_repr =str (result )





        def parse_assignment (s ):



            if '='in s :

                left ,right =s .split ('=',1 )

                return left .strip (),right .strip ()

            return None ,s .strip ()



        _ ,actual_val =parse_assignment (actual_repr )

        _ ,expected_val =parse_assignment (expected )



        status ='FAIL'



        try :

            a =float (actual_val )

            b =float (expected_val )

            if abs (a -b )<=1e-9 :

                passed +=1 

                status ='PASS'

        except Exception :



            def norm (s ):

                return re .sub (r"\s+"," ",s ).strip ()

            if norm (actual_repr )==norm (expected ):

                passed +=1 

                status ='PASS'



        print (f"Test {idx :02d}: {status } -- Input: {inp }")

        print (f"  Expected: {expected }")

        print (f"  Actual:   {actual_repr }")



    score =int ((passed /total )*100 )if total >0 else 0 

    print ("\nSummary:")

    print (f"  Passed: {passed }/{total }")

    print (f"  Score: {score }/100")

    return passed ,total ,score 

if __name__ =="__main__":

    parser =argparse .ArgumentParser (description ='MathScript Compiler')

    parser .add_argument ('--code','-c',help ='Source code to compile')

    parser .add_argument ('--file','-f',help ='Source file to compile')

    parser .add_argument ('--run-tests',action ='store_true',help ='Run test cases from a Test_Cases.md file')

    parser .add_argument ('--test-file',default ='Test_Cases.md',help ='Path to test cases markdown')

    parser .add_argument ('--show-all',action ='store_true',help ='Show detailed phases for all tests (not just failures)')

    args =parser .parse_args ()



    if args .run_tests :

        run_tests (args .test_file ,show_all =args .show_all )

        sys .exit (0 )



    sample ="x = 5\ny = 10\nz = x + y\ntotal = (x + y) * 2\n"

    source =sample 



    if args .code :

        source =args .code 

    elif args .file :

        try :

            with open (args .file ,'r',encoding ='utf-8')as f :

                source =f .read ()

        except Exception as e :

            print (f"Error reading {args .file }: {e }",file =sys .stderr )

            sys .exit (1 )

    elif os .path .exists ("test1.mylang"):

        try :

            with open ("test1.mylang",'r',encoding ='utf-8')as f :

                source =f .read ()

        except Exception as e :

            print (f"Error reading test1.mylang: {e }",file =sys .stderr )



    compile_and_run (source )

