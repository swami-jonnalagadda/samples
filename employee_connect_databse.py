#!/usr/bin/python

import MySQLdb as m
db = m.connect("localhost","root","root123","DATA")
cursor = db.cursor(m.cursors.DictCursor)
sql = "select * from employee"
cursor.execute(sql)
data = cursor.fetchall()
db.commit()
for row in data:
    print row['SALARY']
    print row['EMPLOYEEID']
    print row['EMPLOYEE_NAME']
    #print row['SALARY']+print row['EMPLOYEEID']

