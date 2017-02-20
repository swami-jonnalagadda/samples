#!/usr/bin/python
import re
str1 = raw_input("enter a string:")
search_integer = re.findall('\d+\w+' , str1)
if search_integer:
           print search_integer
si1 = re.findall('\d+' , str1)
if si1:
   print si1
si2 = re.findall('\w+' , str1)
if si2:
   print si2
else:
   print "no match"
