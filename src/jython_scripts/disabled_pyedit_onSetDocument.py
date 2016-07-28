#!/usr/bin/env jython
if False:
    from org.python.pydev.editor import PyEdit #@UnresolvedImport
    cmd = 'command string'
    editor = PyEdit
    systemGlobals = {}
    
assert cmd is not None
assert editor is not None

if cmd=='onSetDocument':#verb=opened
    import sys

    def get_os_version(): #vriskei to onoma tou leitourgikou
        ver = sys.platform.lower()
        if ver.startswith('java'):
            import java.lang
            ver = java.lang.System.getProperty("os.name").lower()
        return ver
    
    verb_id='http://activitystrea.ms/schema/1.0/open'
    verb_disp='opened'
    
    name_of_file=editor.getEditorFile().getName()
    size_of_file=editor.getEditorFile().length() #το μεγεθος σε bytes
    import os
    from os import system

    direc=os.path.dirname(os.path.abspath(__file__))
    parrent_dir=os.path.abspath(os.path.join(direc, os.pardir)) #src folder
    
    if get_os_version()=='linux':
        os.chdir(parrent_dir)
        system('python2.7 '+'xAPI_script.py '+verb_id+' '+verb_disp+' '+name_of_file+' '+str(size_of_file)) 
    elif 'windows' in get_os_version(): #windows C:\Python27
        system("python  "+parrent_dir+'\\xAPI_script.py '+verb_id+' '+verb_disp+' '+name_of_file+' '+str(size_of_file)) 
    else:
        print 'Not supported OS'

    