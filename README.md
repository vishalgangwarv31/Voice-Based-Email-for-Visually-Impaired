# Voice-Based-Email-for-Visually-Impaired  

<p align="center">
 <img src="https://user-images.githubusercontent.com/54893688/120467228-928ecf00-c3bd-11eb-9efa-24858b488b90.png" border="0" width="260" height="280" /></p>
<p align="center">
  
**Open-Source Voice Based Emailing System for Visually Impaired.**
  
## About

[This project](https://github.com/Dikshabisht7/Voice-Based-Email-for-Visually-Impaired/blob/main/voice_based_mail_for_visually_impaired.ipynb) is a `python-based` application that uses speech to text voice response to enable visually impaired people to manage their email accounts with their voice
alone, as well as read, send, and perform all other useful tasks. The system will prompt voice commands to the user to perform a specific action, and the user will 
respond accordingly. The main advantage of this project is that it eliminates the use of a mouse; instead, the user will have to respond through voice only.  

## Features

1. [Compose email via voice](https://github.com/Dikshabisht7/Voice-Based-Email-for-Visually-Impaired/blob/main/compose_mail.ipynb)
2. [Count total number of mails](https://github.com/Dikshabisht7/Voice-Based-Email-for-Visually-Impaired/blob/main/total_number_mails.ipynb)  
3. [Count number of unseen mails](https://github.com/Dikshabisht7/Voice-Based-Email-for-Visually-Impaired/blob/main/total_number_unseen_mails.ipynb)  
4. [Fetch unseen mails](https://github.com/Dikshabisht7/Voice-Based-Email-for-Visually-Impaired/blob/main/unseen_mails.ipynb)  
5. [Fetch sent mails](https://github.com/Dikshabisht7/Voice-Based-Email-for-Visually-Impaired/blob/main/sent_mails.ipynb)
6. [Read latest mail](https://github.com/Dikshabisht7/Voice-Based-Email-for-Visually-Impaired/blob/main/latest_mail.ipynb)  

## Windows Installation  

  `C:\Users\Diksha>git clone https://github.com/Dikshabisht7/Voice-Based-Email-for-Visually-Impaired.git`

  `C:\Users\Diksha>cd Voice-Based-Email-for-Visually-Impaired`
  
  `C:\Users\Diksha>python3 -m pip install -r requirements.txt`

  `C:\Users\Diksha>python3 voice_based_mail_for_visually_impaired.py`

## Installers 

- ### gTTS 

    gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API. Write spoken mp3 data to a file, 
    a file-like object (bytestring) for further audio manipulation, or stdout. Or simply pre-generate Google Translate TTS request URLs to feed to an external 
    program. 

    #### Python Installation  

    `pip install gTTS`

    #### Conda Installation  

    `conda install -c tdido gtts-token`

- ### speech_recognition

    Library for performing speech recognition, with support for several engines and APIs, online and offline.

    #### Python Installation

    `pip install SpeechRecognition`  

    #### Conda Installation

    `conda install -c conda-forge speechrecognition` 
  
- ### smtplib

    The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon. 

    #### Python Installation

    `pip install smtplib`

    #### Conda Installation  

    `conda install -c conda-forge aiosmtplib`

- ### imaplib
  
    IMAP is an email retrieval protocol which does not download the emails. It just reads them and displays them. This is very useful in low bandwidth 
    condition. Python’s client side library called imaplib is used for accessing emails over imap protocol.

    #### Python Installation  

    `pip install imap`

    #### Conda Installation  

    `conda install -c conda-forge imapclient`
  
- ### BeautifulSoup
  
    Beautiful Soup is a library for pulling data out of HTML and XML files. It provides ways of navigating, searching, and modifying parse trees.

    #### Python Installation  

    `pip install beautifulsoup4`

    #### Conda Installation  

    `conda install -c anaconda beautifulsoup4`
  
- ### pyglet
  
    pyglet is a cross-platform windowing and multimedia library for Python, intended for developing games and other visually rich applications. 

    #### Python Installation  

    `pip install pyglet`

    #### Conda Installation  

    `conda install -c conda-forge pyglet`

## Modification

- If you want to save the mp3 files in other directory then just follow the below instruction.
  
- Just add your desktop directory in code where I have used path words in several lines. If you don't know your desktop directory then just open 
terminal or command prompt and paste the below code. Like: C:\Users\user\Desktop (this is my desktop directory).
  
  `%userprofile%\Desktop`
  
- Paste your email id and password in line 83 and 84. Also paste recipient email id in line 116.

- Allow the less secure apps: ON.

## Usage

`python3 voice_based_mail_for_visually_impaired.py`
