#!/usr/bin/env python

## Python 2.7
import getpass
import sys
import telnetlib

# Ask for username and password
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

# Open a file called myswitches (with the IP addresses to connect to)
f = open('myswitches')

# Telnet to hosts and get the running config
for line in f:
    HOST = line.strip()
    print("Getting running-config from host {}".format(HOST))
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("terminal length 0\n")
    tn.write("show run\n")
    tn.write("exit\n")

    readoutput = tn.read_all()
    saveoutput = open("switch" + HOST, "w")
    saveoutput.write(readoutput)
    saveoutput.close

    print tn.read_all()
