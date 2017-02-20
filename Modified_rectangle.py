#!/usr/bin/python
#program to find area and perimeter of rectangle using OOPS
#created on 18-01-2016
class Shape:
   def __init__(self):
       print 'shape'
class Rectangle(Shape):
   def __init__(self,length,width):
       self.length = length
       self.width = width
       #Shape.__init__(self)
   def area(self):
       area_rectangle = self.length*self.width
       print "area of rectangle:" , area_rectangle
   def perimeter(self):
       perimeter_rectangle = 2*(self.length+self.width)
       print "perimeter of rectangle:" , perimeter_rectangle
   def __add__(self,other):
       return (self.length+other.length , self.width+other.width)


'''object1 = Rectangle(10,5)
object1.area()

object1.perimeter()
object2 = Rectangle(20,10)
print str(object1+object2)'''
