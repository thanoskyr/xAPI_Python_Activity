#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
from shutil import copy
from easygui import msgbox
from path import src_dir 

def energopoihsh(): #energopoiei ta 2 jython scripts
    os.chdir(src_dir)
    os.chdir('jython_scripts')
    
    if ['disabled_pyedit_onSave.py', 'disabled_pyedit_onSetDocument.py'] not in os.listdir(".")  and ['pyedit_onSave.py', 'pyedit_onSetDocument.py'] in os.listdir("."):
        msgbox('Already enabled')
        print 'Already enabled'
        return #Ηδη ενεργοποιημενο και βγαινει από τη συνάρτηση
    
    
    flag=0
    try:
        copy('disabled_pyedit_onSave.py','pyedit_onSave.py') #rename
        flag=flag+1
        copy('disabled_pyedit_onSetDocument.py','pyedit_onSetDocument.py')
        flag=flag+1
            
    except : 
        os.chdir(src_dir)
        image="images/io_error.png"
        msgbox("Can't enable. Error on rename jython scripts",title="OSError!!!",image=image) 
        print "Can't enable. Error on rename jython scripts"
        exit()
        
    if flag==2: #an exei ginei h antigrafh ...
        os.remove('disabled_pyedit_onSave.py')
        os.remove('disabled_pyedit_onSetDocument.py')
        
        current_dir=os.path.dirname(os.path.abspath(__file__)) #src folder 
        os.chdir(current_dir)
        try:
            open('out.txt', 'w').close() #καθαρισμός out.txt 
        except IOError:
            image="images/io_error.png"
            msgbox("Can't clean out.txt",title="IOError!!!",image=image) 
            print "Can't clean out.txt"
        print'Enable of jython scripts done' #προαιρετικα
        flag=0  #reset flag
        return True
    else:
        return False

if __name__ == '__main__':
    energopoihsh()