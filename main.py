"""
MathScript Compiler - Professional Main Entry Point with Detailed Output
Executes 30 complex test cases with comprehensive compilation stage visualization
"""

from lexer import Lexer
from enhanced_parser import EnhancedParser
from optimizer import Optimizer
from code_generator import CodeGenerator
from interpreter import Interpreter
from test_cases_30 import TEST_CASES_30
import re
import sys

class CompilerStats:
    """Statistics tracker for compilation"""
    def __init__(self):
        self.total_tokens = 0
        self.total_ir_lines = 0
        self.total_opt_reductions = 0
        self.total_instructions = 0
        self.tests_passed = 0
        self.tests_failed = 0

stats = CompilerStats()

def compile_and_run(source_code):
    """Compile and run source code through the full pipeline"""
    try:
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        
        enhanced = EnhancedParser(tokens)
        ast, ir = enhanced.parse()
        
        optimizer = Optimizer()
        optimized_ir = optimizer.constant_folding(ir)
        optimized_ir = optimizer.dead_code_elimination(optimized_ir)
        
        code_gen = CodeGenerator()
        final_code = code_gen.generate(optimized_ir)
        
        interpreter = Interpreter()
        env = interpreter.run(final_code)
        
        user_vars = {k: v for k, v in sorted(env.items()) if not re.match(r'^t\d+$', k)}
        
        return {
            'result': user_vars,
            'tokens': tokens,
            'ir': ir,
            'optimized_ir': optimized_ir,
            'instructions': final_code,
            'success': True
        }
    except Exception as e:
        return {
            'result': None,
            'tokens': None,
            'ir': None,
            'optimized_ir': None,
            'instructions': None,
            'success': False,
            'error': str(e)
        }

def format_section_header(title, width=80):
    """Format a section header"""
    padding = width - len(title) - 2
    left_pad = padding // 2
    right_pad = padding - left_pad
    return f"|{' ' * left_pad}{title}{' ' * right_pad}|"

def print_beautiful_header():
    """Print beautiful main header"""
    width = 80
    print("\n" + "+" + "=" * (width - 2) + "+")
    print(format_section_header("MATHSCRIPT COMPILER - 30 COMPLEX TESTS"))
    print(format_section_header("Professional Compilation Pipeline Analysis"))
    print("+" + "=" * (width - 2) + "+\n")

def print_test_header(test_num, total):
    """Print test header"""
    width = 80
    header = f"TEST {test_num:02d} / {total:02d}"
    print("\n" + "-" * width)
    print(f" {header}".ljust(width))
    print("-" * width + "\n")

def print_input_output(source_code, result, expected):
    """Print input and output with comparison"""
    print(f"  INPUT CODE:\n    {source_code}\n")
    print(f"  EXPECTED OUTPUT:\n    {expected}\n")
    print(f"  ACTUAL OUTPUT:\n    {result}\n")

def print_tokens(tokens):
    """Print tokens in formatted way"""
    print("  LEXICAL ANALYSIS (Tokens):")
    token_list = list(tokens)
    for i, (token_type, token_val) in enumerate(token_list, 1):
        print(f"    [{i:2d}] {token_type:12s} = {token_val}")
    return token_list

def print_ir(ir, title="INTERMEDIATE CODE (Three-Address Code)"):
    """Print IR code"""
    print(f"\n  {title}:")
    for i, line in enumerate(ir, 1):
        print(f"    {i:2d}. {line}")

def print_statistics(tokens, ir, optimized_ir, instructions):
    """Print compilation statistics"""
    ir_reduction = len(ir) - len(optimized_ir)
    reduction_pct = (ir_reduction / len(ir) * 100) if len(ir) > 0 else 0
    
    print(f"\n  COMPILATION STATISTICS:")
    print(f"    Tokens Generated:        {len(tokens):3d}")
    print(f"    IR Lines (Original):     {len(ir):3d}")
    print(f"    IR Lines (Optimized):    {len(optimized_ir):3d}")
    print(f"    Optimization Reduction:  {ir_reduction:3d} lines ({reduction_pct:.1f}%)")
    print(f"    Machine Instructions:    {len(instructions):3d}")
    
    stats.total_tokens += len(tokens)
    stats.total_ir_lines += len(ir)
    stats.total_opt_reductions += ir_reduction
    stats.total_instructions += len(instructions)

def print_test_result(passed, expected, actual):
    """Print test result with pass/fail"""
    width = 80
    status = "PASS" if passed else "FAIL"
    symbol = "[+]" if passed else "[-]"
    
    result_line = f" {symbol} TEST RESULT: {status}".ljust(width)
    if passed:
        print("\n" + "=" * width)
        print(result_line.ljust(width))
        print("=" * width)
    else:
        print("\n" + "*" * width)
        print(result_line.ljust(width))
        print("*" * width)
        print(f"  Expected: {expected}")
        print(f"  Got:      {actual}")

def run_30_complex_tests():
    """Run all 30 complex test cases with detailed analysis"""
    print_beautiful_header()
    
    for idx, (code, expected_vars) in enumerate(TEST_CASES_30, 1):
        print_test_header(idx, len(TEST_CASES_30))
        
        # Compile and run
        output = compile_and_run(code)
        
        if not output['success']:
            print(f"  ERROR: {output['error']}")
            print_test_result(False, expected_vars, None)
            stats.tests_failed += 1
            continue
        
        result = output['result']
        
        # Display input and output
        print_input_output(code, result, expected_vars)
        
        # Display tokens
        tokens = print_tokens(output['tokens'])
        
        # Display IR stages
        print_ir(output['ir'])
        print_ir(output['optimized_ir'], "OPTIMIZED CODE (After Constant Folding & DCE)")
        
        # Display instructions
        print(f"\n  GENERATED INSTRUCTIONS (Bytecode):")
        for i, instr in enumerate(output['instructions'], 1):
            print(f"    {i:2d}. {instr}")
        
        # Display statistics
        print_statistics(tokens, output['ir'], output['optimized_ir'], output['instructions'])
        
        # Check result
        all_match = True
        if result is None:
            all_match = False
        else:
            for var_name, expected_val in expected_vars.items():
                if var_name not in result:
                    all_match = False
                    break
                
                actual_val = result[var_name]
                try:
                    if abs(float(actual_val) - float(expected_val)) > 1e-5:
                        all_match = False
                        break
                except:
                    if str(actual_val) != str(expected_val):
                        all_match = False
                        break
        
        if all_match:
            stats.tests_passed += 1
        else:
            stats.tests_failed += 1
        
        print_test_result(all_match, expected_vars, result)
    
    # Print final summary
    print_final_summary()

def print_final_summary():
    """Print comprehensive final summary"""
    total_tests = stats.tests_passed + stats.tests_failed
    pass_percentage = (stats.tests_passed / total_tests * 100) if total_tests > 0 else 0
    
    print("\n\n" + "+" + "=" * 78 + "+")
    print(format_section_header("FINAL COMPILATION REPORT"))
    print("+" + "=" * 78 + "+")
    
    print(f"\n  TEST RESULTS:")
    print(f"    Total Tests:             {total_tests:3d}")
    print(f"    Tests Passed:            {stats.tests_passed:3d}")
    print(f"    Tests Failed:            {stats.tests_failed:3d}")
    print(f"    Success Rate:            {pass_percentage:6.2f}%")
    
    print(f"\n  OVERALL STATISTICS:")
    print(f"    Total Tokens Generated:  {stats.total_tokens:5d}")
    print(f"    Total IR Lines:          {stats.total_ir_lines:5d}")
    print(f"    Total Optimizations:     {stats.total_opt_reductions:5d} lines removed")
    print(f"    Total Instructions:      {stats.total_instructions:5d}")
    
    avg_tokens = stats.total_tokens / total_tests if total_tests > 0 else 0
    avg_ir = stats.total_ir_lines / total_tests if total_tests > 0 else 0
    avg_instructions = stats.total_instructions / total_tests if total_tests > 0 else 0
    
    print(f"\n  AVERAGES PER TEST:")
    print(f"    Avg Tokens:              {avg_tokens:7.2f}")
    print(f"    Avg IR Lines:            {avg_ir:7.2f}")
    print(f"    Avg Instructions:        {avg_instructions:7.2f}")
    
    print("\n" + "+" + "=" * 78 + "+")
    
    if stats.tests_failed == 0:
        print("\n  [SUCCESS] All tests passed! Compiler is functioning correctly.\n")
        return 0
    else:
        print(f"\n  [WARNING] {stats.tests_failed} test(s) failed. Review details above.\n")
        return 1

def main():
    """Main entry point"""
    exit_code = run_30_complex_tests()
    return exit_code

if __name__ == "__main__":
    sys.exit(main())

