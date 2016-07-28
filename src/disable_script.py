#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
from shutil import copy
from easygui import msgbox

def apenergopoihsh(): #apenergopoiei ta 2 jython scripts metonomazontas ta
    #current_dir=os.path.dirname(os.path.abspath(__file__)) #src folder
    os.chdir('jython_scripts') #apo to src phgaine sto jython_scripts folder
    #current_dir=os.getcwd()
    #print current_dir #jython_scripts
    if ['disabled_pyedit_onSave.py', 'disabled_pyedit_onSetDocument.py'] in os.listdir(".")  and ['pyedit_onSave.py', 'pyedit_onSetDocument.py'] not in os.listdir("."):
        msgbox('Already disabled')
        print 'Already disabled'
        return 
    
    
    flag=0
    try:
        copy('pyedit_onSave.py','disabled_pyedit_onSave.py') #rename
        flag=flag+1
        copy('pyedit_onSetDocument.py','disabled_pyedit_onSetDocument.py')
        flag=flag+1
            
    except:
        current_dir=os.path.dirname(os.path.abspath(__file__)) #src folder
        os.chdir(current_dir)   
        image="images/io_error.png"
        msgbox("Can't diable. Error on rename  jython scripts",title="OSError!!!",image=image) 
        print "Can't disable. Error on rename  jython scripts"
        exit()
        
    if flag==2: #an exei kanei antigrafh tote diegrapse ta pyedit_*
        os.remove('pyedit_onSave.py')
        os.remove('pyedit_onSetDocument.py')
       
        print'Disable of jython scrits done'
        flag=0  #reset flag
        return True
    
    else:
        return False

if __name__ == '__main__':
    apenergopoihsh() #Των pyedit_*