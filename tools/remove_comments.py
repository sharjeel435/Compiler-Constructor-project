import io 

import os 

import sys 

import tokenize 



def strip_comments (source_bytes ):

    out =[]

    prev_end =(1 ,0 )

    g =tokenize .tokenize (io .BytesIO (source_bytes ).readline )

    for toknum ,tokval ,start ,end ,line in g :

        if toknum ==tokenize .COMMENT :

            continue 

        if toknum ==tokenize .ENCODING :

            continue 

        out .append ((toknum ,tokval ))

    return tokenize .untokenize (out )



def process_file (path ):

    with open (path ,'rb')as f :

        data =f .read ()

    try :

        new =strip_comments (data )

    except Exception as e :

        print (f"Failed to strip {path }: {e }")

        return False 

    with open (path ,'w',encoding ='utf-8')as f :

        f .write (new )

    return True 



if __name__ =='__main__':

    root =os .path .abspath (os .path .join (os .path .dirname (__file__ ),'..'))

    py_files =[]

    for dirpath ,dirnames ,filenames in os .walk (root ):

        for fn in filenames :

            if fn .endswith ('.py'):

                py_files .append (os .path .join (dirpath ,fn ))

    failed =[]

    for p in py_files :

        ok =process_file (p )

        if ok :

            print (f"Stripped comments: {p }")

        else :

            failed .append (p )

    if failed :

        print ('Failed files:')

        for p in failed :

            print (' -',p )

        sys .exit (1 )

    print ('Done')

