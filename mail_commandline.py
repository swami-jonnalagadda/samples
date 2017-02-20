#!/usr/bin/python

import smtplib
import getpass
import sys
class Mail:
 def __init__(self,username):
    self.username = username
    
 def mail_server(self):
   text = ' '
   host = "smtp.gmail.com"
   port = 587
   server = smtplib.SMTP(host,port)
   server.ehlo()
   server.starttls()
   server.ehlo()
   user = self.username
   password = getpass.getpass()
   server.login(user,password)
   to = sys.arg[1]
   sub = sys.arg[3]
   with open(sys.argv[2] , 'r') as ins:
        text = ins.readlines()
   message = "subject : %s\n\n %s"%(sub,text)
   server.sendmail(user,to,message)


mail_object = Mail("career.swami.ja@gmail.com")
mail_object.mail_server()

print "mail opened"  
