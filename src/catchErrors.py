#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import xAPI_script
from easygui import msgbox
import os

def catchErrors():
    #πιάνει τα σφάλματα από την console που κάνει ο χρήστης
    try:
        cdir=os.path.dirname(os.path.abspath(__file__)) #src folder
        f=open(cdir+'/tracked_out.txt',"r")
    except IOError:
        image='images/io_error.png'
        msgbox("Cannot open tracked_out.txt",title="IOError!!!",image=image)  
        print "Cannot open tracked_out.txt"
## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines
    lines = f.readlines()
    f.close()

    for line in lines:
    
        if 'SyntaxError' in line:
            sfalma, ext = line.split(":",1) 
            verb_id='https://pithos.okeanos.grnet.gr/public/59bQWGYBTnyB01Q2Z1ZCQ2'
            verb_disp='syntaxErred'
            xAPI_script.xApi(verb_id, verb_disp, getExtension(ext))
        elif 'IOError' in line:
            verb_id='https://pithos.okeanos.grnet.gr/public/RCF4PRXbBEFdFzrY5uxRg4'
            verb_disp='ioErred'
            sfalma, ext = line.split(":",1) 
            xAPI_script.xApi(verb_id, verb_disp, getExtension(ext)) 
        elif 'IndexError' in line:
            verb_id='https://pithos.okeanos.grnet.gr/public/RNVdfxilIDOz8DVltIc6x4'
            verb_disp='indexErred'
            sfalma, ext = line.split(":",1) 
            xAPI_script.xApi(verb_id, verb_disp, getExtension(ext))
        elif 'KeyError' in line: 
            verb_id='https://pithos.okeanos.grnet.gr/public/Z3RtCRnFnJvQyA04KeQBx1'
            verb_disp='keyErred'
            sfalma, ext = line.split(":",1) 
            xAPI_script.xApi(verb_id, verb_disp, getExtension(ext))
        elif 'IndentationError' in line:
            verb_id='https://pithos.okeanos.grnet.gr/public/m2YoJlD87N1dqE5zycW9u4'
            verb_disp='indentationErred'
            sfalma, ext = line.split(":",1) 
            xAPI_script.xApi(verb_id, verb_disp, getExtension(ext))
        elif 'NameError' in line:
            verb_id='https://pithos.okeanos.grnet.gr/public/HabaurkiRh3sTLiWPaZxe5'
            verb_disp='nameErred'
            sfalma, ext = line.split(":",1) 
            xAPI_script.xApi(verb_id, verb_disp, getExtension(ext))
        elif 'OverflowError' in line: 
            verb_id='https://pithos.okeanos.grnet.gr/public/xTDGmQLzEEbGhAjmGZfny2'
            verb_disp='overflowErred'
            sfalma, ext = line.split(":",1) 
            xAPI_script.xApi(verb_id, verb_disp, getExtension(ext))
        elif 'ZeroDivisionError' in line: 
            verb_id='https://pithos.okeanos.grnet.gr/public/YO7GsQvXOGihNBzaLhB4i'
            verb_disp='zeroDivisionErred'
            sfalma, ext = line.split(":",1) 
            xAPI_script.xApi(verb_id, verb_disp, getExtension(ext))
        elif 'AttributeError' in line:
            verb_id='https://pithos.okeanos.grnet.gr/public/Sg7V9ErtjZaDYJe96kGSt2'
            verb_disp='attributeErred'
            sfalma, ext = line.split(":",1) 
            xAPI_script.xApi(verb_id, verb_disp, getExtension(ext))
        elif 'TypeError' in line:
            verb_id='https://pithos.okeanos.grnet.gr/public/a2MiYmMu8TmCGfCoaoxXG1'
            verb_disp='typeErred'
            sfalma, ext = line.split(":",1) 
            xAPI_script.xApi(verb_id, verb_disp, getExtension(ext))
        
        #Ομοίως και για τα άλλα ρήματα
        else:
            pass
        
        
            # Καθαριζω το αρχειο
    try:
        open('tracked_out.txt', 'w').close()
    except IOError:
        image="images/io_error.png"
        msgbox("Cannot clean tracked_out.txt",title="IOError!!!",image=image) 
        print "Cannot clean tracked_out.txt"
def getExtension(ext): #returns dictionary with one member
    if ext.endswith('\n'):
        ext=ext[:-1]    #κοβω τα δυο τελευταια αν ειναι newline
    ext_dic={"https://pithos.okeanos.grnet.gr/public/4BkAG81ozWCuNxkXEo0ga2":ext}    
    return ext_dic
    
if __name__ == '__main__':
    catchErrors()