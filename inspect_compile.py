from cli import compile_and_run 
import pprint 
res =compile_and_run ('total = ((200 - 50) * (2 + 1)) / 3 + 100')
pprint .pprint (res )
print ('\nuser result:',res .get ('result'))
print ('env:',res .get ('env'))
