import re 

instr ="STORE 17 INTO total"
m_store =re .match (r"^STORE\s+([\w\.-]+)\s+INTO\s+(\w+)$",instr )
if m_store :
    right ,left =m_store .groups ()
    print (f"Matched: right={right !r }, left={left !r }")
    try :
        val =float (right )if '.'in right else int (right )
        print (f"Parsed val={val }, type={type (val )}")
    except Exception as e :
        print (f"Parse error: {e }")
else :
    print ("No regex match")
