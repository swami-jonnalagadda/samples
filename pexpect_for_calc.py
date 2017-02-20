import pexpect
import sys
m = pexpect.spawn('python calc.py')
m.logfile_read = sys.stdout
m.expect("enter character")
m.sendline("+")
m.expect("enter variable 1")
m.sendline('34')
m.expect("enter variable 2")
m.sendline('45')
m.expect("end of program")


m.close
