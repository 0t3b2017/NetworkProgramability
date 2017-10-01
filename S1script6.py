#!/usr/bin/env python

# Python 2.7
import getpass
import sys
import telnetlib

user = raw_input("Enter your remote account: ")
password = getpass.getpass()

f = open('myswitches')

for HOST in f:
    print("Configuring host {}".format(HOST))
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("configure terminal\n")

    for vlan_id in [100, 200, 300]:
       tn.write("no vlan " + str(vlan_id) + "\n")

    tn.write("end\n")
    tn.write("copy run startup\n")
    tn.write("\n")
    tn.write("exit\n")

    print tn.read_all()
