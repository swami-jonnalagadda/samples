#!/usr/bin/python
#program for adding & subtracting two matrices.
class Matrix:
 def __init__(self,a):    
  self.a = a
  #self.r = r
  #self.c = c
"""definig a matrix using class matrix is a list containg lists inside """
 def Matrix1(self):
   num = int(raw_input("enter value"))
   for i in range(num):
     row = []
     for j in range(num):
        column = input()
        row.append(column)
     self.a.append(row)
     print self.a
#creating a method to add 
 def __add__(self,other):
   if len(self.a) == len(other.a):  #self.a is one matrix ,other.a is another matrix checking if both contain same nop of elements
     print "same number of elements in both matrix"
     for i in self.a:
      for j in other.a:
       if len(i) == len(j):      
          break
     print "columns equal" #checking if each elemnt is a list and each elemnet has same number of elemnts
     newmatrix = []
     for m in range(len(self.a)):
         row1=[]            
         for n in range(len(self.a[0])):
	     x=self.a[m][n] + other.a[m][n]
	     row1.append(x)
         newmatrix.append(row1)
     print newmatrix
   else:
     print "no of rows and columns are not same matrix addition cannot be performed"
#creating a method to subtract 
 def __sub__(self,other):
   if len(self.a) == len(other.a):
     print "same number of elements in both matrix"
     for i in self.a:
      for j in other.a:
       if len(i) == len(j):
          break
     print "columns equal"
     newmatrix = []
     for m in range(len(self.a)):
         row1=[]            
         for n in range(len(self.a[0])):
	     x=self.a[m][n] - other.a[m][n]
	     row1.append(x)
         newmatrix.append(row1)
     print newmatrix
    
                          

obj1 = Matrix([])
obj1.Matrix1()
obj2 = Matrix([])
obj2.Matrix1()


obj1+obj2
                          
                         



