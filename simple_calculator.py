#!/usr/bin/python
#program for simple calculator
operator = raw_input("enter character")  
var1 = raw_input("enter variable 1")     #taking input and converting into integer
var1 = int(var1)
var2 = raw_input("enter variable 2")       #taing input and converting into integer
var2 = int(var2)

if operator == '+':                         #continue if condition for '-' , '*' ,'/'
   var3 = var1+var2
   print var3
str1 = "end of program"
print str1
