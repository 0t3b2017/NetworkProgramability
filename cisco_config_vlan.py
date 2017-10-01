## Python 2.7
import getpass
import sys
import telnetlib

HOST = "192.168.12.254"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("configure terminal\n")
tn.write("vlan 2\n name vIT\n")
tn.write("exit\n")
tn.write("vlan 3\n name vRI\n")
tn.write("exit\n")
tn.write("vlan 4\n name vDMZ\n")
tn.write("exit\n")
tn.write("vlan 5\n name vCAM5\n")
tn.write("exit\n")
tn.write("end\n")
tn.write("copy run startup\n")
tn.write("\n")
tn.write("exit\n")

print tn.read_all()
