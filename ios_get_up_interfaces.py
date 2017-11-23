## Python 3
import getpass
import sys
import telnetlib

"""
HOST = input("Enter the IP address or Hostname: ")
user = input("Enter your remote account: ")
password = getpass.getpass()
"""

HOST = "192.168.122.253"
user = "roberto"
password = "cisco"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

#tn.write("enable\n")
#tn.write("cisco\n")
tn.write(b"show interface status\n")
tn.write(b"exit\n")

out = tn.read_all().decode('ascii')
print(str(out))
#print(str(out).split())
#print(tn.read_all().decode('ascii'))
