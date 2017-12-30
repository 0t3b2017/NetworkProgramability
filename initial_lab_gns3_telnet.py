"""
Create a initial configuration on new devices in a GNS Project. Those configurations are:
-> hostname
-> username
-> domain name
-> mgmt interface
-> ip address
-> dns server
-> gateway / default route
-> crypto key
-> enable ssh
-> configure ssh vty
-> login local

## FUTURE
-> authentication features
-> tacacs
-> radius
-> routing features
-> switching features

telnet to localhost device's tcp port

"""
import sys
import time
import telnetlib

new_hostname = "SW1"
username = "roberto"
password = "cisco"
domain_name = "h3b.lab"
mgmt_interface = "gi0/0"
ip_address = "192.168.122.71"
mask = "255.255.255.0"
dns_server ="192.168.122.1"
gateway = "192.168.122.1"
crypto_key_size = "1024"
enable_ssh = True
#configure ssh vty
#login local
HOST = "127.0.0.1"
PORT = "5004"


tn = telnetlib.Telnet(host=HOST, port=PORT)

tn.write(b"\n")

#tn.read_until(b"Username: ")
#tn.write(username.encode('ascii') + b"\n")


#with open("initial_lab_cmds.txt") as f:
#    cmds = f.read().splitlines()

tn.write(b"enable\n")
#tn.write("cisco\n")
tn.write(b"conf t\n")
tn.write(b"host {}\n".format(new_hostname))

tn.write(b"int {}\n".format(mgmt_interface))
tn.write(b"no switchport\n")
tn.write(b"ip address {} {}\n".format(ip_address, mask))
tn.write(b"ip domain-name {}\n".format(domain_name))
tn.write(b"username {} privilege 15 secret {}\n".format(username, password))
tn.write(b"\n")
tn.write(b"\n")
tn.write(b"crypto key generate rsa modulus {}\n".format(crypto_key_size))
tn.write(b"ip ssh version 2\n")
tn.write(b"line vty 0 15\n")
tn.write(b"transport input ssh\n")
tn.write(b"login local\n")
tn.write(b"\n")
tn.write(b"end\n")
tn.write(b"wr\n")
time.sleep(5)
tn.write(b"exit\n")
print("DEBUG")

#print(tn.read_all())

#print(tn.read_all().decode('ascii'))
#print(tn.read_some().decode('ascii'))

tn.close()
print(tn.read_all().decode('ascii'))

print("DEBUG")
