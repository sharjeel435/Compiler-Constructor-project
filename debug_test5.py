import sys 
sys .path .insert (0 ,'.')
from lexer import Lexer 
from enhanced_parser import EnhancedParser 
from optimizer import Optimizer 
from code_generator import CodeGenerator 
from interpreter import Interpreter 

code ='total = 25 - 5 * 2 + 8 / 4'
print ('INPUT:',code )
print ()

lexer =Lexer (code )
tokens =list (lexer .tokenize ())
print ('TOKENS:',tokens )
print ()

parser =EnhancedParser (tokens )
ast ,ir =parser .parse ()
print ('IR (before optimization):')
for line in ir :
    print ('  ',line )
print ()

optimizer =Optimizer ()
opt_ir =optimizer .optimize (ir )
print ('OPTIMIZED IR:')
for line in opt_ir :
    print ('  ',line )
print ()

codegen =CodeGenerator ()
instructions =codegen .generate (opt_ir )
print ('GENERATED INSTRUCTIONS:')
for instr in instructions :
    print ('  ',instr )
print ()

interpreter =Interpreter ()
result =interpreter .run (instructions )
print ('RESULT:',result )
print ()
print ('EXPECTED: {\'total\': 17}')
