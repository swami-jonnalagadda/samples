#!/usr/bin/python
list1 = []
def file_operations():
    f1 = open('msd','r')
    f2 = f1.readlines()
    print f2
    #list1.append(f2)
    #print list1
    for i in f2:
          l=i.split(" ")
          print l
          second_letter = [x[1] for x in f2]
          print second_letter




file_operations()

