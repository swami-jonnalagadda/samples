#!/usr/bin/python
#program to print the reverse of a string
var1 = raw_input("enter a sentence")#input a string from console
string = str(var1)  #convert the variable to a string using str function type conversion
words = string.split(" ")  # splitting the string using string.split()
words = list(words)       # converting the broken string into a list 
words.reverse()   # applying list.reverse() to reverse the string
rev_word = ''.join(rev_word)   #use join() to join the reversed list
print rev_word   #print reverse words

