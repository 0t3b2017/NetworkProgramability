#!/usr/bin/env python

"""
This is a script used to add interfaces tagged to some VLANs.
Used in Brocade switches
by: 0T3B
"""

import paramiko
import time

ip_address = "192.168.122.253"
username = "roberto"
password = "cisco"
interface = '10/18'

"""
vlan_first = int(input("Enter the first VLAN: "))
vlan_last = int(input("Enter the last VLAN: "))
"""

vlan_first = 100
vlan_last = 1049

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

print "Successful connection", ip_address

client = ssh_client.invoke_shell()

client.send("configure terminal\n")

for n in range(vlan_first, vlan_last + 1):
    print "Adding VLAN " + str(n)
    client.send("vlan " + str(n) + "\n")
    client.send("tagged ethernet " + str(interface) + "\n")
    time.sleep(2)

client.send("end\n")

client.send("wr mem\n")

time.sleep(1)
output = client.recv(65535)
print output

ssh_client.close()
