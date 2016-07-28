#!/usr/bin/env jython
# -*- coding: utf-8 -*- 


if False:
    from org.python.pydev.editor import PyEdit #@UnresolvedImport
    cmd = 'command string'
    editor = PyEdit
    systemGlobals = {}

#--------------------------------------------------------------- REQUIRED LOCALS
#interface: String indicating which command will be executed
#As this script will be watching the PyEdit (that is the actual editor in Pydev), and this script
#will be listening to it, this string can indicate any of the methods of org.python.pydev.editor.IPyEditListener
assert cmd is not None

#interface: PyEdit object: this is the actual editor that we will act upon
assert editor is not None

if cmd == 'onCreateActions':
    import os
    direc=os.path.dirname(os.path.abspath(__file__)) #jython_scripts folder
    parrent_dir=os.path.abspath(os.path.join(direc, os.pardir)) #src folder
    
    #Optimization so that we don't create a class for a command more than once (otherwise we'd create a different class
    #definition whenever a new editor is created).
    StartXapi = systemGlobals.get('StartXapi')
    if StartXapi is None:
        Action = editor.getActionClass()
        
        class StartXapi(Action):
          
            def run(self):
                
                from os import system
                os.chdir(parrent_dir)
                system('python starter.py')
                
        systemGlobals['StartXapi'] = StartXapi
    

    editor.addOfflineActionListener("xapi", StartXapi(), 'Start xApi', True) #the user can activate this action with: Ctrl+2  xapi<ENTER>

