#!/usr/bin/python

import smtplib
import getpass
host = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(host , port)
server.ehlo()
server.starttls()
server.ehlo()
username = raw_input("gmail")
password = getpass.getpass()
server.login(username , password)
to = raw_input("to")
sub = raw_input("sub")
mes = raw_input("message")
message = "subject : %s\n\n %s"%(sub,mes)
server.sendmail(username , to ,message)
