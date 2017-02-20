#!/usr/bin/python
import pickle
mylist = [1,2,3,4,5]
my_dict = {'name':'hari'}
my_str = "asm tech ltd"
f = open('MSD' , 'w')
pickle.dump(mylist , f)
pickle.dump(my_dict , f)
f.close()
f = open('msd' , 'r')
my_list = pickle.load(f)
