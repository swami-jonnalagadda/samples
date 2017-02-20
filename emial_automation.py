#!/usr/bin/python
#program to automate email entries  
import pexpect   #pexpect module
m_p = pexpect.spawn('python_gmail.py')   #reads data from 
m_p.timeout = 60     
m_p.expect('gmail')   #this commands expect gmail from the prgram python_gmail.py
m_p.sendline('senders email')  #please enter senders email address
m_p.expect('Password:')
m_p.sendline('give pass word')      #please enter your password here
m_p.expect('to')
m_p.sendline('to address')     #enter the reciepents address
m_p.expect('sub')
m_p.sendline('TEST')
#m_p.expect('mes')
#m_p.expect('hii this is email automation')
m_p.close()
