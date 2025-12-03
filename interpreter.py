import re 





class Interpreter :

    def __init__ (self ):

        pass 



    def run (self ,code ):



        env ={}



        def get_val (name ):

            """Get the value of a variable or parse it as a literal"""

            if name in env :

                return env [name ]

            try :

                if '.'in name :

                    return float (name )

                return int (name )

            except (ValueError ,TypeError ):

                return None 



        for instr in code :

            instr =instr .strip ()





            m_load =re .match (r"^LOAD\s+([-]?\d+\.?\d*)\s+INTO\s+(\w+)$",instr )



            m_store =re .match (r"^STORE\s+([-\w\.]+)\s+INTO\s+(\w+)$",instr )



            m_op =re .match (r"^(MULTIPLY|DIVIDE|ADD|SUBTRACT)\s+([-\w\.]+)\s+(?:AND|BY)\s+([-\w\.]+)\s+->\s+(\w+)$",instr )



            if m_load :

                val ,t =m_load .groups ()

                env [t ]=float (val )if '.'in val else int (val )

            elif m_op :

                op ,a ,b ,t =m_op .groups ()

                aval =get_val (a )

                bval =get_val (b )

                if aval is None or bval is None :

                    continue 

                if op =='ADD':

                    res =aval +bval 

                elif op =='SUBTRACT':

                    res =aval -bval 

                elif op =='MULTIPLY':

                    res =aval *bval 

                elif op =='DIVIDE':

                    res =aval /bval 

                else :

                    continue 



                if isinstance (res ,float )and res .is_integer ():

                    res =int (res )

                env [t ]=res 

            elif m_store :

                right ,left =m_store .groups ()

                val =get_val (right )



                if val is None :

                    try :

                        val =float (right )if '.'in right else int (right )

                    except (ValueError ,TypeError ):

                        pass 

                if val is not None :

                    env [left ]=val 

        return env 

