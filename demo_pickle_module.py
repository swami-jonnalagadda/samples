#!/usr/bin/python
#program to demonstrate use of pickle module
import pickle          #pickle is a module : to install pickle use sudo pip install pickle
mylist = [1,2,3,4,5]
my_dict = {'name':'hari'}
my_str = "asm tech ltd"
f = open('MSD' , 'w')          #opening a file named msd if it doesnt exsist it will create a new file
pickle.dump(mylist , f)         #writes the data into that file        
print pickle.dumps(mylist)

#in json only we can convert only list or dictionary at a time but in pickle you can convert list and dict at a time      
pickle.dump(my_dict , f)
f.close()

