

"""

Comprehensive Test Suite with Clear Phases and Clean Interface

Designed for 100/100 test pass rate with detailed reporting

"""



from lexer import Lexer 

from enhanced_parser import EnhancedParser 

from optimizer import Optimizer 

from code_generator import CodeGenerator 

from interpreter import Interpreter 

import sys 





TEST_CASES =[

{

"id":1 ,

"name":"Basic Variable Assignment",

"input":"counter = 15",

"expected":{"counter":15 },

"complexity":"Level 1"

},

{

"id":2 ,

"name":"Subtraction Operation",

"input":"balance = 100 - 45",

"expected":{"balance":55 },

"complexity":"Level 2"

},

{

"id":3 ,

"name":"Division with Grouping",

"input":"average = (8 + 12) / 2",

"expected":{"average":10 },

"complexity":"Level 3"

},

{

"id":4 ,

"name":"Decimal Multiplication",

"input":"area = 5.5 * 3.2",

"expected":{"area":17.6 },

"complexity":"Level 3"

},

{

"id":5 ,

"name":"Complex Multi-Operation Expression",

"input":"result = (100 + 50) / 2 - 25 * 2",

"expected":{"result":25 },

"complexity":"Level 4"

},

{

"id":6 ,

"name":"Triple Nested Groupings",

"input":"value = (((15 + 5) * 2) - 10) / 2",

"expected":{"value":15 },

"complexity":"Level 5"

},

{

"id":7 ,

"name":"Large Scale Decimal Computation",

"input":"profit = 1000 + 2000 - (500 * 1.5) + 200",

"expected":{"profit":2450 },

"complexity":"Level 5"

},

{

"id":8 ,

"name":"Moderately Complex Expression",

"input":"total = ((200 - 50) * (2 + 1)) / 3 + 100",

"expected":{"total":250 },

"complexity":"Level 6"

}

]





class ComprehensiveTestSuite :

    """Test Suite Manager with Phase Tracking"""



    def __init__ (self ):

        self .results =[]

        self .total_tests =len (TEST_CASES )

        self .passed =0 

        self .failed =0 



    def format_header (self ,text ,level =1 ):

        """Format section headers"""

        if level ==1 :

            print ("\n"+"="*80 )

            print (f"  {text }")

            print ("="*80 )

        elif level ==2 :

            print (f"\n  ▶ {text }")

            print ("  "+"-"*76 )



    def format_test_box (self ,test_id ,test_name ):

        """Format test case header"""

        print (f"\n  ┌─ TEST CASE #{test_id }: {test_name }")

        print (f"  │")



    def print_phase (self ,phase_num ,phase_name ):

        """Print phase indicator"""

        print (f"  │  [PHASE {phase_num }] {phase_name }")



    def print_detail (self ,label ,value ,indent =2 ):

        """Print detail line"""

        prefix ="  │"if indent ==2 else "  │  "

        if isinstance (value ,list ):

            print (f"{prefix }  {label }:")

            for item in value :

                print (f"{prefix }    • {item }")

        else :

            print (f"{prefix }  {label }: {value }")



    def run_test (self ,test_case ):

        """Run a single test case through all phases"""

        test_id =test_case ["id"]

        test_name =test_case ["name"]

        source_code =test_case ["input"]

        expected =test_case ["expected"]

        complexity =test_case ["complexity"]



        self .format_test_box (test_id ,test_name )

        self .print_detail ("Input Code",source_code )

        self .print_detail ("Complexity",complexity )

        self .print_detail ("Expected Result",str (expected ))



        try :



            self .print_phase (1 ,"LEXICAL ANALYSIS")

            lexer =Lexer (source_code )

            tokens =lexer .tokenize ()

            self .print_detail ("Tokens Generated",str (tokens )[:60 ]+"..."if len (str (tokens ))>60 else str (tokens ))





            self .print_phase (2 ,"PARSING & IR GENERATION")

            enhanced =EnhancedParser (tokens )

            ast ,ir =enhanced .parse ()

            ir_display =[str (line )[:70 ]for line in ir ]

            self .print_detail ("Three-Address Code",ir_display )





            self .print_phase (3 ,"CODE OPTIMIZATION")

            optimizer =Optimizer ()

            optimized_ir =optimizer .constant_folding (ir )

            optimized_ir =optimizer .dead_code_elimination (optimized_ir )

            opt_display =[str (line )[:70 ]for line in optimized_ir ]

            self .print_detail ("Optimized Code",opt_display )





            self .print_phase (4 ,"CODE GENERATION")

            code_gen =CodeGenerator ()

            final_code =code_gen .generate (optimized_ir )

            gen_display =[str (line )[:70 ]for line in final_code ]

            self .print_detail ("Generated Instructions",gen_display )





            self .print_phase (5 ,"EXECUTION & RESULT")

            interpreter =Interpreter ()

            env =interpreter .run (final_code )

            user_vars ={k :v for k ,v in sorted (env .items ())if not k .startswith ('t')}

            self .print_detail ("Actual Result",str (user_vars ))





            self .print_phase (6 ,"VERIFICATION & SCORING")

            if user_vars ==expected :

                status ="✓ PASSED"

                self .passed +=1 

                score ="100/100"

            else :

                status ="✗ FAILED"

                self .failed +=1 

                score ="0/100"



            self .print_detail ("Status",status )

            self .print_detail ("Score",score )



            print (f"  │")

            print (f"  └─ Test Complete\n")



            self .results .append ({

            "test_id":test_id ,

            "name":test_name ,

            "status":"PASS"if user_vars ==expected else "FAIL",

            "expected":expected ,

            "actual":user_vars 

            })



        except Exception as e :

            self .failed +=1 

            print (f"  │  [ERROR] {str (e )}")

            print (f"  │")

            print (f"  └─ Test Failed with Exception\n")

            self .results .append ({

            "test_id":test_id ,

            "name":test_name ,

            "status":"ERROR",

            "error":str (e )

            })



    def run_all_tests (self ):

        """Run all test cases"""

        self .format_header ("MATHSCRIPT COMPILER - COMPREHENSIVE TEST SUITE",1 )

        print (f"\n  Total Test Cases: {self .total_tests }")

        print (f"  Test Complexity Levels: 1-6")

        print (f"  Target Score: 100/100 for all tests\n")



        for i ,test_case in enumerate (TEST_CASES ,1 ):

            self .run_test (test_case )



        self .print_summary ()



    def print_summary (self ):

        """Print comprehensive summary"""

        self .format_header ("TEST SUMMARY REPORT",1 )



        print (f"\n  ┌─ Overall Statistics")

        print (f"  │")

        print (f"  │  Total Tests:     {self .total_tests }")

        print (f"  │  Passed:          {self .passed } ✓")

        print (f"  │  Failed:          {self .failed } ✗")



        pass_percentage =(self .passed /self .total_tests *100 )if self .total_tests >0 else 0 

        print (f"  │  Pass Rate:       {pass_percentage :.1f}%")



        if pass_percentage ==100 :

            print (f"  │  Final Grade:     A+ (100/100) ★ PERFECT ★")

        elif pass_percentage >=90 :

            print (f"  │  Final Grade:     A ({pass_percentage :.0f}/100)")

        elif pass_percentage >=80 :

            print (f"  │  Final Grade:     B ({pass_percentage :.0f}/100)")

        else :

            print (f"  │  Final Grade:     C ({pass_percentage :.0f}/100)")



        print (f"  │")

        print (f"  └─ End of Summary\n")





        self .format_header ("DETAILED RESULTS TABLE",1 )

        print (f"\n  {'ID':<4} {'Test Name':<40} {'Status':<8} {'Score':<8}")

        print (f"  {'-'*4 } {'-'*40 } {'-'*8 } {'-'*8 }")



        for result in self .results :

            status_symbol ="✓ PASS"if result ["status"]=="PASS"else "✗ FAIL"if result ["status"]=="FAIL"else "⚠ ERROR"

            score ="100/100"if result ["status"]=="PASS"else "0/100"

            print (f"  {result ['test_id']:<4} {result ['name']:<40} {status_symbol :<8} {score :<8}")



        print ()





def main ():

    """Main entry point"""

    try :

        suite =ComprehensiveTestSuite ()

        suite .run_all_tests ()





        sys .exit (0 if suite .failed ==0 else 1 )



    except Exception as e :

        print (f"\n[FATAL ERROR] {str (e )}")

        sys .exit (1 )





if __name__ =="__main__":

    main ()

