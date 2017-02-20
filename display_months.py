#!/usr/bin/python

list_value = [ 'jan' , 'feb' , 'mar' , 'april' , 'may' , 'june' , 'july' , 'aug' , 'sep' , 'oct' , 'nov' , 'dec' ]
value = raw_input(" ")
value = int(value)
end = value*3
start =end-3
print list_value[start : end]
