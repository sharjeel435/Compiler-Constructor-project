from lexer import Lexer 
from enhanced_parser import EnhancedParser 
from optimizer import Optimizer 
from code_generator import CodeGenerator 
from interpreter import Interpreter 











code ="result = (100 + 50) / 2 - 25 * 2"
print (f"Code: {code }")
print (f"Manual calculation: (100 + 50) / 2 - 25 * 2 = 150 / 2 - 50 = 75 - 50 = 25")
print ()

lexer =Lexer (code )
tokens =list (lexer .tokenize ())
parser =EnhancedParser (tokens )
ast ,ir =parser .parse ()

print ("Intermediate Code:")
for line in ir :
    print (f"  {line }")
print ()

optimizer =Optimizer ()
opt_ir =optimizer .constant_folding (ir )

print ("Optimized IR:")
for line in opt_ir :
    print (f"  {line }")
print ()

codegen =CodeGenerator ()
instructions =codegen .generate (opt_ir )

print ("Instructions:")
for instr in instructions :
    print (f"  {instr }")
print ()

interpreter =Interpreter ()
result =interpreter .run (instructions )
user_vars ={k :v for k ,v in sorted (result .items ())if not k .startswith ('t')}

print (f"Result: {user_vars }")
print (f"Expected: -25 (but this appears wrong)")
print (f"Correct: 25")
