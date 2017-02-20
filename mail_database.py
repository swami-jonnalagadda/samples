import smtplib
import getpass
import MySQLdb as m
db = m.connect("localhost","root","root123","DATA")
cursor = db.cursor()
sql = "select * from employee"
cursor.execute(sql)
data = cursor.fetchall()
db.commit()
#print data
s1 = 'salary\t\t\temployeeid\t\t\tEmployee_name\n'
s2=''
print s1
for i in data:
  s = '%s\t\t\t%s\t\t\t%s\n' % (i)
  s2=s2+s
  print s



host = "smtp.gmail.com"
port=587
server=smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username=raw_input("gmail")
password=getpass.getpass()
server.login(username,password)
to=raw_input("to")
sub=raw_input("sub")
mes=s1
mess=''
for line in s2:
 mess=mess+line
messs=mes+mess
message="subject: %s\n\n %s" %(sub,messs)
server.sendmail(username,to,message)

