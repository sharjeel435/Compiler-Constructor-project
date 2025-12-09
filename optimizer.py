import re 

class Optimizer :

    def __init__ (self ):

        pass 
    def constant_folding (self ,ir ):

        consts ={}

        out =[]

        num_re =re .compile (r"^-?\d+(?:\.\d+)?$")

        for instr in ir :

            m_num =re .match (r"^(t\d+) = ([-]?\d+\.?\d*)$",instr )

            m_op =re .match (r"^(t\d+) = ([\w\.-]+)\s*([+\-\*/])\s*([\w\.-]+)$",instr )

            m_assign =re .match (r"^(\w+) = (t\d+|[-]?\d+\.?\d*|\w+)$",instr )

            if m_num :

                t ,val =m_num .groups ()

                consts [t ]=float (val )if '.'in val else int (val )

                out .append (instr )

            elif m_op :

                t ,a ,op ,b =m_op .groups ()

                aval =consts .get (a )if a in consts else (float (a )if num_re .match (a )else None )

                bval =consts .get (b )if b in consts else (float (b )if num_re .match (b )else None )

                if aval is not None and bval is not None :

                    if op =='+':res =aval +bval 

                    elif op =='-':res =aval -bval 

                    elif op =='*':res =aval *bval 

                    else :res =aval /bval 

                    if isinstance (res ,float )and res .is_integer ():

                        res =int (res )

                    consts [t ]=res 

                    out .append (f"{t } = {res }")

                else :

                    out .append (instr )

            elif m_assign :

                left ,right =m_assign .groups ()

                if right in consts :

                    out .append (f"{left } = {consts [right ]}")

                    consts [left ]=consts [right ]

                else :

                    out .append (instr )

            else :

                out .append (instr )

        return out 


    def dead_code_elimination (self ,ir ):
       
        used_vars = set()
        final_vars = set()
    
        for instr in ir:
            matches = re.findall(r'\b(t\d+|[a-zA-Z_]\w*)\b', instr)
            for match in matches:
                if '=' in instr:
                    parts = instr.split('=')
                   
                    if len(parts) > 1 and match in parts[1]:
                        used_vars.add(match)
                
                    if len(parts) > 0 and not match.startswith('t'):
                        final_vars.add(match)
        
        optimized = []
        for instr in ir:
            m = re.match(r'^(t\d+)\s*=', instr)
            if m:
                var = m.group(1)
        
                if var in used_vars:
                    optimized.append(instr)
            else:
        
                optimized.append(instr)
        
        return optimized if len(optimized) < len(ir) else ir 

