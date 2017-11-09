#!/usr/bin/env python

from netmiko import ConnectHandler

sw1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.71',
    'username': 'roberto',
    'password': 'cisco',
}

sw2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'roberto',
    'password': 'cisco',
}

sw3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.73',
    'username': 'roberto',
    'password': 'cisco',
}

sw4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.74',
    'username': 'roberto',
    'password': 'cisco',
}

sw5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.75',
    'username': 'roberto',
    'password': 'cisco',
}

core = [sw2, sw1]
access = [sw5, sw4, sw3]

with open('ios_cisco_design_guide') as f:
    lines = f.read().splitlines()
print "\033[33mConfiguring access devices...\033[m"
print lines

for devices in access:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output

with open('ios_core') as f:
    lines = f.read().splitlines()
print "\033[33mConfiguring Core devices\033[m"
print lines

for devices in core:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output
