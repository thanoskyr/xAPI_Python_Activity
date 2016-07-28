#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Κατασκευάζει και στέλνει τα statements


from tincan import (  
    RemoteLRS,
    Statement,
    Agent,
    Verb,
    Activity,
    Context,
    LanguageMap,
    ActivityDefinition,
    Extensions,
)

#import uuid
import sys    
from resources import lrs_actor
#from easygui import msgbox 
from images import *

def xApi(verb_id,verb_disp,extension_dict):
    
    #orismos LRS 
    lrs = RemoteLRS(
        version=lrs_actor.version,
        endpoint=lrs_actor.endpoint,
        username=lrs_actor.username,
        password=lrs_actor.password,
    )

    #orismos actor 
    actor=Agent(name=lrs_actor.actorName, mbox='mailto:'+lrs_actor.actorMail,) 
    #orimos verb
    verb = Verb(
                id=verb_id,
                display=LanguageMap({'en-US': verb_disp}),
                )
    #ορισμός object
    object = Activity(
                      id='https://pithos.okeanos.grnet.gr/public/8jiz0aVKZxjVI2CvNl7XV3',
                      definition=ActivityDefinition(
                    name=LanguageMap({'en-US': 'Python file'}),
                    description=LanguageMap({'en-US': 'A python source code file'}),
                    ),
                      )
    #ορισμος extension 
    extension=Extensions(extension_dict)
    #ορισμός context
    context = Context(extensions=extension)
    #Κατασκευή statement
    statement = Statement(
                          actor=actor,
                          verb=verb,
                          object=object,
                          context=context
                          )

    # save our statement to the remote_lrs and store the response in 'response'
    print "saving the Statement..."
    response = lrs.save_statement(statement)

    if not response:
        raise ValueError("statement failed to save")
        error_icon="images/error_icon.png"
#        msgbox("Can't save statement!\n Check the file: lrs_actor.py",title="Error!!!",image=error_icon)
        print "Can't save statement!!\n Check the file: lrs_actor.py"

    print "...done     verb: " ,verb_disp 
    #ok_image="images/ok_icon.png" 
    #msgbox("Επιτυχης αποθήκευση δήλωσης\n"+'Ρήμα: '+verb_disp,title="Success",image=ok_image)
    #Δε δουλευει, πεταει exception γραφικου περιβάλλοντος tk

if __name__ == '__main__':
    ext_name_id='https://pithos.okeanos.grnet.gr/public/XtDQuAa8YUdEJwyeTbr2s5'
    ext_size_id='https://pithos.okeanos.grnet.gr/public/F7or5zEmJVjRl0eyufOWy3'
    try:
        orisma1=sys.argv[1]     
        orisma2=sys.argv[2]
        orisma3=sys.argv[3] #value of extension name of file
        orisma4=sys.argv[4] #value of extension size of file
        
        dic={ext_name_id:orisma3,ext_size_id:orisma4}
        xApi(orisma1, orisma2,dic)
    except IndexError:   
        error_im="images/error_48x48.png"
        #msgbox("Το script πρέπει να κληθει με 4 ορίσματα verb_id, verb_disp και extension_key, ext_value",title="IndexError!!!",image=error_im)   
        print "Το script πρέπει να κληθει με 4 ορίσματα verb_id, verb_disp και extension_key, ext_value"
