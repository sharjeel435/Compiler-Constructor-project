import re 


class CodeGenerator :
    def __init__ (self ):
        pass 

    def generate (self ,ir ):
        code =[]

        temps ={}
        for instr in ir :
            m_num =re .match (r"^(t\d+) = ([-]?\d+\.?\d*)$",instr )
            if m_num :
                t ,val =m_num .groups ()
                temps [t ]=val 

        for instr in ir :
            m_num =re .match (r"^(t\d+) = ([-]?\d+\.?\d*)$",instr )
            m_op =re .match (r"^(t\d+) = ([\w\.-]+)\s*([+\-\*/])\s*([\w\.-]+)$",instr )
            m_assign =re .match (r"^(\w+) = (t\d+|[-]?\d+\.?\d*|\w+)$",instr )
            if m_num :
                t ,val =m_num .groups ()
                code .append (f"LOAD {val } INTO {t }")
            elif m_op :
                t ,a ,op ,b =m_op .groups ()
                if op =='*':code .append (f"MULTIPLY {a } AND {b } -> {t }")
                elif op =='/':code .append (f"DIVIDE {a } BY {b } -> {t }")
                elif op =='+':code .append (f"ADD {a } AND {b } -> {t }")
                else :code .append (f"SUBTRACT {a } AND {b } -> {t }")
            elif m_assign :
                left ,right =m_assign .groups ()

                if right in temps :
                    code .append (f"STORE {temps [right ]} INTO {left }")
                else :
                    code .append (f"STORE {right } INTO {left }")
            else :
                code .append (instr )
        return code 
