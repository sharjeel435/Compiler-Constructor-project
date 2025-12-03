from lexer import Lexer 
from enhanced_parser import EnhancedParser 
from optimizer import Optimizer 
from code_generator import CodeGenerator 
from interpreter import Interpreter 

code ="total = ((200 - 50) * (2 + 1)) / 3 + 100"
print (f"Testing: {code }\n")

lexer =Lexer (code )
tokens =list (lexer .tokenize ())

parser =EnhancedParser (tokens )
ast ,ir =parser .parse ()

optimizer =Optimizer ()
opt_ir =optimizer .constant_folding (ir )
opt_ir =optimizer .dead_code_elimination (opt_ir )

codegen =CodeGenerator ()
instructions =codegen .generate (opt_ir )

print ("Generated Instructions:")
for i ,instr in enumerate (instructions ):
    print (f"  {i }: {instr }")
print ()

interpreter =Interpreter ()
env =interpreter .run (instructions )

print (f"Environment returned: {env }")
print (f"Type: {type (env )}")
print (f"Keys: {list (env .keys ())}")
print ()


for i ,instr in enumerate (instructions ):
    print (f"Instruction {i }: {instr }")
    if "STORE"in instr :
        print (f"  -> This is STORE instruction")

        import re 
        m =re .match (r"^STORE\s+([-\w\.]+)\s+INTO\s+(\w+)$",instr )
        if m :
            print (f"  -> Regex MATCHED: {m .groups ()}")
        else :
            print (f"  -> Regex DID NOT MATCH")
