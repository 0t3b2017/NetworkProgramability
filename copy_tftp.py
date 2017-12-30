
#!/usr/bin/env python

"""
This is a script used to add interfaces tagged to some VLANs.
Used in Brocade switches
by: 0T3B
"""

import paramiko
import time

ip_address = "192.168.122.71"
username = "roberto"
password = "abc@123"

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

client.send("copy running-config tftp://192.168.122.178/" + ip_address + "\n")
client.send("\n")
client.send("\n")

time.sleep(1)
output = client.recv(65535)
print output

ssh_client.close()
