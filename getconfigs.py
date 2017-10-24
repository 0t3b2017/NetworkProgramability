#!/usr/bin/env python

# Python 2.7

import paramiko
import time

username = "roberto"
password = "cisco"


# Open a file called myswitches (with the IP addresses to connect to)
f = open('myswitches')

# Create a loop to connect to all devices on 'myswitches' file and configure them.

for line in f:
    if line[0] != "#":
        ip_address = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address, username=username, password=password)

        print("Successful connection to ", ip_address)

        client = ssh_client.invoke_shell()

        print("Getting running-config from host {}".format(ip_address))

        client.send("terminal length 0\n")
        time.sleep(1)
        client.send("show run\n")
        time.sleep(5)
        client.send("exit\n")
  
        output = client.recv(65535)
        print output

        saveoutput = open("bkp_switch" + ip_address, "w")
        saveoutput.write(output)

        ssh_client.close()
