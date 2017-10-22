#!/usr/bin/python3

from time import sleep

vlan_first = int(input("Enter the first VLAN: "))
vlan_last = int(input("Enter the last VLAN: "))

# num_int = int(input("How many interfaces? "))

host = input("Enter the hostname or ip address: ")
interface1 = "ethernet10/15"
interface2 = "ethernet10/16"

phrase = ("Connecting to the host {} ...".format(host))
print("")
#print("#" * len(phrase))
print(phrase)
#print("#" * len(phrase))
print("")
sleep(3)
print("enable")
print("configure terminal")
for vlan_id in range(vlan_first,vlan_last + 1):
    print(" vlan {}".format(vlan_id))
    print(" tagged {}".format(interface1))
    print(" tagged {}".format(interface2))
    print(" exit\n")
print(" end")
print("write memory")
print("exit")
