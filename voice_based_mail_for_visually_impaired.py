#!/usr/bin/env python
# coding: utf-8

# # Voice Based Email for Visually Impaired

# In[ ]:


#Libraries required for the Project

import speech_recognition as sr
import smtplib
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
from email.header import decode_header


# In[ ]:


#Voice Out
def voice(tsname):
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)


# In[ ]:


#Fetch project name

print ("-"*60)
print ("       Project: Voice based Email for visually impaired")
print ("-"*60)

#project name

ts = gTTS(text="Project: Voice based Email for visually impaired", lang='en')
tsname=("C:/Users/user/Desktop/name.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
ts.save(tsname)
voice(tsname)


# In[ ]:


#login from OS

login = os.getlogin
print ("You are logged In from : "+login())
ts = gTTS(text="You are logged in from " +login(), lang='en')
tsname=("C:/Users/user/Desktop/login.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
ts.save(tsname)
voice(tsname)


# ## IMAP4_SSL
# 
# IMAP4_SSL is used to establish connection to the server.  
# **Syntax**: connection=impalib.IMAP4_SSL(hostname, port)  
# Here,  
# **hostname**: imap.gmail.com  
# **port**: 993  
# 
# Next, open connection to the email service by use of the stored credentials.  
# **Syntax**:imap_object.login(username,password)  
# Here,  
# **username**=unm  
# **password**=psw

# In[ ]:


#Login to the mail account through IMAP

imap = imaplib.IMAP4_SSL('imap.gmail.com',993)                                          
unm = ('<email_id>')                                                        
psw = ('<password>')                                                                  
imap.login(unm,psw) 


# ## SMTP
# 
# Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.  
# **Syntax**: SMTP_object=smtplib.SMTP(hostname, port)  
# Here,  
# **hostname**: smtp.gmail.com  
# **port**: 587  
#   
# To identify yourself to the server, **.ehlo()** (ESMTP) should be called after creating an .SMTP() object, and again after .starttls().  
# 
# An unsecured SMTP connection is created and then encrypted using **.starttls()**.
# 
# Next, open connection to the email service by use of the stored credentials.  
# **Syntax**:SMTP_object.login(username,password)  
# Here,  
# **username**=unm  
# **password**=psw
# 

# In[ ]:


#Login to the mail account through SMTP

mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
sender=unm
recipient='<recipient_email_id>'
mail.login(unm,psw)


# In[ ]:


#Login to the mail account

print ("You are logged In from : " + unm)
ts = gTTS(text="You are logged in from " + unm, lang='en')
tsname=("C:/Users/user/Desktop/login.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
ts.save(tsname)
voice(tsname)


# In[ ]:


#to re-enter the choice
def reenter():
    ts = gTTS(text="Please repeat your choice ", lang='en')
    tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    


# In[ ]:


#voice not recognized error
def googlerec():
    print("Google Speech Recognition could not understand audio.")
    ts = gTTS(text="Google Speech Recognition could not understand audio.", lang='en')
    tsname=("C:/Users/user/Desktop/error.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    


# In[ ]:


#could not request results error
def googlereq():
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
    ts = gTTS(text="Could not request results from Google Speech Recognition service; {0}", lang='en')
    tsname=("C:/Users/user/Desktop/error.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    


# In[ ]:


#Function to logout from the mail account

def logout(): 
    
    print("Do you want to log out?")
    ts=gTTS(text="Do you want to log out",lang='en')
    tsname=("C:/Users/user/Desktop/logout.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    
    def logch():
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print ("Your choice:")
            audio=r.listen(source)
            print ("ok done!!")
            
        try:
            #voice recognition part
            
            global ch
            ch=r.recognize_google(audio)
            print ("You said : "+ch)
            ts = gTTS(text="You said "+ch, lang='en')
            tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
            ts.save(tsname)
            voice(tsname)
            
        except sr.UnknownValueError:
            googlerec()
            reenter()
            logch()
            
        except sr.RequestError as e:
            googlereq()
            reenter()
            logch()
            
    logch()
    if ch=="yes":
        mail.close() #to close the mail
        imap.logout() #to logout from the mail
        print("You have been logged out. Thank You!")
        ts = gTTS(text="You have been logged out Thank You ", lang='en')
        tsname=("C:/Users/user/Desktop/logout.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
        ts.save(tsname)
        voice(tsname)
    elif ch=="no":
        choice()
    else :
        reenter()
        logch()


# In[ ]:


#Function for the choice Compose a mail

def option1():
    
    ts = gTTS(text="Enter subject: ", lang='en')
    tsname=("C:/Users/user/Desktop/subject.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    
    #Function to input subject from the user
    def subject():
        
        #voice recognition part
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print ("Enter Subject:")
            audio=r.listen(source)
            print ("ok done!!")
            
        try:
            global sub
            sub=r.recognize_google(audio)
            print ("You said : "+sub)
            ts = gTTS(text="You said "+sub, lang='en')
            tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
            ts.save(tsname)
            voice(tsname)
            
        #voice not recognized error 
        except sr.UnknownValueError:
            googlerec()
            reenter()
            subject()
            
        except sr.RequestError as e:
            googlereq()
            reenter()
            subject()
            
    subject()
    print ("Your Subject is: "+sub)
    ts = gTTS(text="Your Subject is " +sub, lang='en')
    tsname=("C:/Users/user/Desktop/subject.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    
    ts = gTTS(text="Enter your message: ", lang='en')
    tsname=("C:/Users/user/Desktop/message.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    
    #Function to input message from the user
    def message():
        
        #voice recognition part
        r = sr.Recognizer() 
        
        with sr.Microphone() as source:
            print ("Your message :")
            audio=r.listen(source)
            print ("ok done!!")
            
        try:
            global msg
            msg=r.recognize_google(audio)
            print ("You said : "+msg)
            ts = gTTS(text="Your said "+msg, lang='en')
            tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
            ts.save(tsname)
            voice(tsname)
            
        #voice not recognized error
        except sr.UnknownValueError:
            googlerec()
            reenter()
            message()
            
        except sr.RequestError as e:
            googlereq()
            reenter()
            message()
            
    message()
    print ("Your message is: "+msg)
    ts = gTTS(text="Your message is " +msg, lang='en')
    tsname=("C:/Users/user/Desktop/message.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    
    #Function to send mail to the sender
    def mailsend():
        header='To:'+recipient+'\n'+'From:'+sender+'\n'+'subject:'+sub+'\n'
        global msg
        msg=header+msg
        mail.sendmail(sender, recipient, msg)
        print ("Congratulations! Your mail has been sent. ")
        ts = gTTS(text="Congratulations! Your mail has been sent. ", lang='en')
        tsname=("C:/Users/user/Desktop/send.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
        ts.save(tsname)
        voice(tsname)
        mail.close()
        
    ts = gTTS(text="Do you want to send the mail?", lang='en')
    tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    
    #Function to confirm whether to send mail or not
    def sendchoice():
        
        #voice recognition part
        r = sr.Recognizer() 
        
        with sr.Microphone() as source:
            print ("Do you want to send the mail?")
            audio=r.listen(source)
            print ("ok done!!")
            
        try:
            global msg
            ch=r.recognize_google(audio)
            print ("You said : "+ch)
            ts = gTTS(text="Your said "+ch, lang='en')
            tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
            ts.save(tsname)
            voice(tsname)
            if(ch=="yes") :
                mailsend()
            elif (ch=="no"):
                option1()
            else :
                reenter()
                sendchoice()  
                
        #voice not recognized error
        except sr.UnknownValueError:
            googlerec()
            reenter()
            sendchoice()
            
        except sr.RequestError as e:
            googlereq()
            reenter()
            sendchoice()
            
    sendchoice()
    logout()


# In[ ]:


#Function to count total number of mails in the inbox

def countmails():
    
    imap.select("inbox") #to select inbox 
    
    typ, messageIDs = imap.search(None, "ALL") #to fetch all inbox mails
    
    messageIDsString = str( messageIDs[0], encoding='utf8' )
    listOfSplitStrings = messageIDsString.split(" ") #split to get individual IDs
    
    print ("Number of mails in your inbox :"+str(len(listOfSplitStrings))) #length of listOfSplitStrings is total mails present
    ts = gTTS(text="Total Number of mails in your inbox are :"+str(len(listOfSplitStrings)), lang='en')
    
    tsname=("C:/Users/user/Desktop/total.mp3") #Example: path -> C:\Users\user\Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)


# In[ ]:


#Function to count total number of unseen mails in the inbox

def countunseen():
    
    imap.select("inbox") #to select inbox 
    print("Checking for new e-mails for ",sender,".", sep='')
    typ, messageIDs = imap.search(None, "UNSEEN") #to fetch unseen inbox mails
    messageIDsString = str( messageIDs[0], encoding='utf8' )
    listOfSplitStrings = messageIDsString.split(" ") #split to get individual IDs
    
    #length of listOfSplitStrings is total unseen mails present
    
    if len(listOfSplitStrings) == 0:
        print("You have no new e-mails.")
        ts = gTTS(text="You have no new e-mails.", lang='en')                              
        tsname=("C:/Users/user/Desktop/unseen.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
        ts.save(tsname)
        voice(tsname)
        
    elif len(listOfSplitStrings) == 1:
        print("You have",len(listOfSplitStrings),"new e-mail.")
        ts = gTTS(text="You have one unseen email", lang='en')                              
        tsname=("C:/Users/user/Desktop/unseen.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
        ts.save(tsname)
        voice(tsname)
        
    else:
        print("You have",len(listOfSplitStrings),"new e-mails.")
        ts = gTTS(text="Total Number of unseen mails in your inbox are :"+str(len(listOfSplitStrings)), lang='en')           
        tsname=("C:/Users/user/Desktop/unseen.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
        ts.save(tsname)
        voice(tsname)


# In[ ]:


#Function to read unseen mails from the inbox

def readunseen():
    
    imap.select('"[Gmail]/All Mail"',readonly = True)
    response, messages = imap.search(None,'UnSeen') #to fetch all unseen mails in inbox
    messages = messages[0].split()
    
    try: 
        latest = int(messages[-1]) #fetching mails from last
        
    except IndexError:
        print("No Unseen Mails")
        ts = gTTS("You have no unseen mails", lang='en')
        tsname=("C:/Users/user/Desktop/nounseen.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
        ts.save(tsname)
        voice(tsname)
        return
    
    #reading all unseen mails upto n
    for i in range(latest, latest-int(text), -1):
        
        #fetching mail information
        res, msg = imap.fetch(str(i), "(RFC822)") 
        
        for response in msg:
            if isinstance(response, tuple):
                
                #message_from_bytes(s) returns a message object structure from a string
                msg = email.message_from_bytes(response[1])
                
                #to read date of the mail
                print(msg["Date"])
                ts = gTTS(text="Date :"+str(msg["Date"]), lang='en')
                tsname=("C:/Users/user/Desktop/time.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
                ts.save(tsname)
                voice(tsname)
                
                #to read sender of the mail
                print("From: "+msg["From"])
                ts = gTTS(text="From :"+str(msg["From"]), lang='en')
                tsname=("C:/Users/user/Desktop/from.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
                ts.save(tsname)
                voice(tsname)
                
                #to read subject of the mail
                print("Subject: "+msg["Subject"])
                ts = gTTS(text="Subject :"+str(msg["Subject"]), lang='en')
                tsname=("C:/Users/user/Desktop/subject.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
                ts.save(tsname)
                voice(tsname)


# In[ ]:


#Function to read sent mails from the sent box

def readsent():
    
    imap.select('"[Gmail]/Sent Mail"',readonly = True) #fetching sent mails
    response, messages = imap.search(None,'ALL')
    messages = messages[0].split()           
    
    latest = int(messages[-1]) #fetching mails from last
    #oldest = int(messages[0]) #fetching mails from start
    
    #reading all sent mails upto n
    for i in range(latest, latest-int(text), -1):
        
        #fetching mail information
        res, msg = imap.fetch(str(i), "(RFC822)")
        
        for response in msg:
            if isinstance(response, tuple):
                
                #message_from_bytes(s) returns a message object structure from a string
                msg = email.message_from_bytes(response[1])
                
                #to read date of the mail
                print(msg["Date"])
                ts = gTTS(text="Date :"+str(msg["Date"]), lang='en')
                tsname=("C:/Users/user/Desktop/time.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
                ts.save(tsname)
                voice(tsname)
                
                #to read receiver of the mail
                print("To: "+msg["To"])
                ts = gTTS(text="To :"+str(msg["To"]), lang='en')
                tsname=("C:/Users/user/Desktop/to.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
                ts.save(tsname)
                voice(tsname)
                
                #to read subject of the mail
                print("Subject: "+msg["Subject"])
                ts = gTTS(text="Subject :"+str(msg["Subject"]), lang='en')
                tsname=("C:/Users/user/Desktop/subject.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
                ts.save(tsname)
                voice(tsname)


# In[ ]:


#Function to read latest mail from the inbox

def searchmail(): 
    
    stat, total = imap.select('Inbox') #to select inbox   
    
    result, data = imap.uid('search',None, "ALL") #search mails
    inbox_item_list = data[0].split()
    
    new = inbox_item_list[-1] #fetching mails from last                 
    #old = inbox_item_list[0] #fetching mails from start
    
    result2, email_data = imap.uid('fetch', new, '(RFC822)')  #fetching mail information
    
    raw_email = email_data[0][1].decode("utf-8") #decoding utf-8 encoding                                            
    email_message = email.message_from_string(raw_email)
    
    print ("From: "+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    
    stat, data1 = imap.fetch(total[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser") #using Beautifulsoup to parse some content from a html page
    txt = soup.get_text()
    print ("Body :"+txt)
    
    #reading from,subject and body of the latest mail
    ts = gTTS(text="From: "+email_message['From']+" .Your subject: "+str(email_message['Subject'])+" .body of the mail: "+txt, lang='en')
    tsname=("C:/Users/user/Desktop/mail.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)


# In[ ]:


#Function to provide options for choice Check your Inbox

def menuoption2() :
    
    print ("Option 1: Count total number of mails \nOption 2: Read Latest Mail with Body \nOption 3: Read n unseen mails \nOption 4: Read n sent mails")
    ts = gTTS(text="Option 1: Count total number of mails .Option 2: Read Latest Mail with Body .Option 3: Read n unseen mails .Option 4: Read n sent mails", lang='en')
    tsname=("C:/Users/user/Downloads/menu.mp3")
    ts.save(tsname)
    music = pyglet.media.load(tsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(tsname)
    ts = gTTS(text="Your choice ", lang='en')
    tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    option2()


# In[ ]:


def option2():
    #voice recognition part
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print ("Your choice:")
        audio=r.listen(source)
        print ("ok done!!")
        
    try:
        ch=r.recognize_google(audio)
        if ch=="1":
            print ("You said : "+ch)
            ts = gTTS(text="You said "+ch, lang='en')
            tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
            ts.save(tsname)
            voice(tsname)
            countmails()
            countunseen()
            logout()
        elif ch=="Tu":
            ch=2;
            print ("You said : "+str(ch))
            ts = gTTS(text="You said "+str(ch), lang='en')
            tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
            ts.save(tsname)
            voice(tsname)
            searchmail()
            logout()
        elif ch=="3":
            def nounseen():
                #voice recognition part
                
                r = sr.Recognizer()

                with sr.Microphone() as source:
                    print ("Enter the number of unseen mails to read :")
                    audio=r.listen(source)
                    print ("ok done!!")
                    

                try:
                    global text
                    text=r.recognize_google(audio)
                    print ("You said : "+text)
                    ts = gTTS(text="You said " +text, lang='en')
                    tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
                    ts.save(tsname)
                    voice(tsname)
                    if text.isdigit():
                        readunseen()
                        logout()
                    else :
                        reenter()
                        nounseen()

                except sr.UnknownValueError:
                    googlerec()
                    reenter()
                    nounseen()

                except sr.RequestError as e:
                    googlereq()
                    reenter()
                    nounseen()

            print ("You said : "+ch)
            ts = gTTS(text="You said "+ch, lang='en')
            tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
            ts.save(tsname)
            voice(tsname)
            ts = gTTS(text="Enter the number of unseen mails to read :", lang='en')
            tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
            ts.save(tsname)
            voice(tsname)
            nounseen()
            
        elif ch=="4":
            def nosent():
                #voice recognition part
                
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print ("Enter the number of sent mails to read :")
                    audio=r.listen(source)
                    print ("ok done!!")

                try:
                    global text
                    text=r.recognize_google(audio)
                    print ("You said : "+text)
                    ts = gTTS(text="You said " +text, lang='en')
                    tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
                    ts.save(tsname)
                    voice(tsname)
                    if text.isdigit():
                        readsent()
                        logout()
                    else :
                        reenter()
                        nosent()
                        
                        
                except sr.UnknownValueError:
                    googlerec()
                    reenter()
                    nosent()

                except sr.RequestError as e:
                    googlereq()
                    reenter()
                    nosent()

            print ("You said : "+ch)
            ts = gTTS(text="You said "+ch, lang='en')
            tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
            ts.save(tsname)
            voice(tsname)
            ts = gTTS(text="Enter the number of sent mails to read :", lang='en')
            tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
            ts.save(tsname)
            voice(tsname)
            nosent()
            
        else:
            reenter()
            option2()
            
    except sr.UnknownValueError:
        googlerec()
        reenter()
        option2()
        
    except sr.RequestError as e:
        googlereq()
        reenter()
        option2()


# In[ ]:


#Function to give two choices: Compose a mail and Check your Inbox

def choice():
    
    print ("1. Compose a mail.\n2. Check your inbox. ")
    ts = gTTS(text="option 1. Compose a mail. option 2. Check your inbox. Your choice ", lang='en')
    tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
    ts.save(tsname)
    voice(tsname)
    
    def func():
        #voice recognition part
        
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print ("Your choice:")
            audio=r.listen(source)
            print ("ok done!!")
            
        try:
            text=r.recognize_google(audio)
            if text=="1":
                print ("You said : "+text)
                ts = gTTS(text="You said "+text, lang='en')
                tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
                ts.save(tsname)
                voice(tsname)
                option1()
            elif text=="Tu":
                text=2
                print ("You said : "+str(text))
                ts = gTTS(text="You said "+str(text), lang='en')
                tsname=("C:/Users/user/Desktop/choice.mp3") #path -> C:/Users/user/Desktop> just change with your desktop directory
                ts.save(tsname)
                voice(tsname)
                menuoption2()
            else:
                reenter()
                func()
                
        except sr.UnknownValueError:
            googlerec()
            reenter()
            func()
            
        except sr.RequestError as e:
            googlereq()
            reenter()
            func()
    func()


# In[ ]:


choice()

