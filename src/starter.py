#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os, sys, subprocess
from path import src_dir
if sys.platform == "win32":
    os.chdir(src_dir)
    os.startfile("main_script.pyc") 
elif sys.platform.startswith('linux') :
    os.chdir(src_dir)
    subprocess.call(['gnome-terminal','-x','./main_script.pyc']) 
    # Πρέπει το main_script.pyc να είναι +x (executable)
    #Πρέπει να είναι εγκατεστημένο το gnome-terminal
else:
    pass