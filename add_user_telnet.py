## Python 3
import getpass
import sys
import telnetlib

add_user = "bkpredes"

with open("devices.list", "r") as f:
    devices = f.readlines()

with open("add_user_telnet.cmd", "r") as f:
    commands = f.readlines()


for HOST in devices:
    HOST = input("Enter the IP address or Hostname: ")
    user = input("Enter your remote account: ")
    password = getpass.getpass()

    # Connect to device
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write("enable\n")
    tn.write("cisco\n")

    # Create $USER
    tn.write(b"conf t\n")
    tn.write(b"userinterface loop 0\n")
    tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
    tn.write(b"interface loop 1\n")
    tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
    tn.write(b"router ospf 1\n")
    tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
    tn.write(b"end\n")
    tn.write(b"copy running-config startup-config\n")
    tn.write(b"\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))


