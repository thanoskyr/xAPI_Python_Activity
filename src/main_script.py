#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from easygui import * #@UnusedWildImport
from images import *
from enable_script import energopoihsh
from disable_script import apenergopoihsh
import os
from shutil import copy
from catchErrors import catchErrors
import sys
from resources import lrs_actor
from path import src_dir
import threading
import sched
import time
s = sched.scheduler(time.time, time.sleep)

def run():
    os.chdir(src_dir)
    im="images/python2.png"
    reply = ynbox("Enable tracking?",title='xAPI',image=im)
    #reply=raw_input("Enable tracking? (y/n)\n")
    if reply==True:
        energopoihsh()  #function of enable_script
        
        t1=threading.Thread(target = errors_thread)
        t2=threading.Thread(target = ending)
        t1.daemon=True #Ωστε να σταματα όταν σταματάει το t2
        t1.start()
        t2.start()
        
def errors_thread():
    threading.Timer(60, errors_thread).start() #ανα λεπτό καταγραφή για errors
    print 'recording...\n'
    os.chdir(src_dir) #src folder
    cur_dir = os.getcwd()
    
    copy(cur_dir+'/out.txt', cur_dir+'/tracked_out.txt') 
    catchErrors()
        #clean out.txt and tracked_out.txt
    try:
        open('out.txt', 'w').close()
    except IOError:
        image="images/io_error.png"
        msgbox("Can't clean out.txt",title="IOError!!!",image=image)
        print "Can't clean out.txt"
    try:
        open('tracked_out.txt', 'w').close()
    except IOError:
        image="images/io_error.png"
        msgbox("Can't clean tracked_out.txt",title="IOError!!!",image=image)
        print "Can't clean tracked_out.txt"
    
    
    
def ending(): 
    im_bb="images/human2.png"
    foo=buttonbox("\t  Record of your actinity is ON. \n Please don't close the window. To stop it press  'Exit' ",choices=["Exit"],image=im_bb)
    #Είτε κλείσει το παραθυρο είτε πατησει exit ειναι το ιδιο.  
    apenergopoihsh() 
    rename_console_log()
    catchErrors()
    msgbox("The record is off",title="Bye")
    print "The record is off"
    sys.exit()
    
def rename_console_log(): #rename out.txt to trackedOout.txt
    os.chdir(src_dir) #src folder
    cur_dir = os.getcwd()
    copy(cur_dir+'/out.txt', cur_dir+'/tracked_out.txt')
        
def options_form():
    title_user='User Details' 
    message_user='Please fill in your data'
    fieldNames=['Name','e-mail']
    default_user_vals=[lrs_actor.actorName,lrs_actor.actorMail] 
    fieldValues_user=multenterbox(message_user, title_user, fieldNames,values=default_user_vals)   
   
    while 1: 
        if fieldValues_user == None:
            msgbox("Programm will exit.", "Bye")
            sys.exit()
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues_user[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": break # no problems found
        fieldValues_user = multenterbox(errmsg, title_user, fieldNames, fieldValues_user)
    
    
    title_lrs="LRS details"
    message_lrs="Please fill in your LRS data.\n"
    fieldNames_lrs=['LRS Endpoint','Version', 'LRS username','LRS password']
    default_lrs_vals=[lrs_actor.endpoint,lrs_actor.version,lrs_actor.username,lrs_actor.password]
    fieldValues_lrs=[]  #@UnusedVariable
    fieldValues_lrs=multpasswordbox(message_lrs, title=title_lrs, fields=fieldNames_lrs,values=default_lrs_vals)
    
    # make sure that none of the fields was left blank
    while 1:
        if fieldValues_lrs == None:
            msgbox("Program will exit.", "Bye")
            sys.exit()
        errmsg = ""
        for i in range(len(fieldNames_lrs)):
            if fieldValues_lrs[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames_lrs[i])
        if errmsg == "": break # no problems found
        fieldValues_lrs = multenterbox(errmsg, title_lrs, fieldNames_lrs, fieldValues_lrs)
    
    os.chdir(src_dir+'/resources')
    
    #Τωρα θα γράψουμε τα παραπάνω στο αρχείο
    try:
        f=open('lrs_actor.py','w')
        
    except IOError:
        image='images/io_error.png'
        msgbox("Can't open lrs_actor.py",title="IOError!!!",image=image)
        print "Can't open lrs_actor.py"
        
    f.write('#Options File \n')
    f.write('endpoint="'+fieldValues_lrs[0]+'"\n')
    f.write('version="'+fieldValues_lrs[1]+'"\n')
    f.write('username="'+fieldValues_lrs[2]+'"\n')
    f.write('password="'+fieldValues_lrs[3]+'"\n')
    f.write('actorName="'+fieldValues_user[0]+'"\n')
    f.write('actorMail="'+fieldValues_user[1]+'"\n')
    f.close()
if __name__ == '__main__':
    
    new_user=ynbox("If you are new user or you want to edit your data 'yes'", 'New user?',choices=('[<F1>]Yes', '[<F2>]No'), image=None)
    if new_user:
        options_form()
    else:
        pass
    run()
