#program to add two objects in python
#!/usr/bin/python
class ClassName :
      def __init__(self,a):   #constructor variables which are defined here can be accessed anywhere throughout the class
       self.a = a
       print 'object created'
   
      def __str__(self):          
       return str(self.a)          #inbuilt __str__ function           
    
      def sqr(self):
          return self.a**2      

      def __del__(self):
        print 'objectremove'
    
      def __add__(self,other):
        return self.a+other.a
    
      def __sub__(self,other):
        return self.a-other.a
  
      def __mul__(self,other):
        return self.a*other.a

              
obj2 = ClassName(20)             #creating an instance of that class using object 
obj = ClassName(10)         
print obj.sqr()                    #calling the method using object created as referenece
print obj2+obj                   #this will call inbuilt __add__ method to add two objects
print obj2-obj
print obj*obj2
del obj
