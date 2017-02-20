#!/usr/bin/python


import MySQLdb as m
db = m.connect("localhost","root","root123","DATA")
cursor = db.cursor()
sql = "select * from employee"
cursor.execute(sql)
data = cursor.fetchall()
db.commit()
for row in data:
   print str(row)

db.close()
