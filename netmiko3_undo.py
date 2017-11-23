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

with open('ios_config_undo') as f:
    lines = f.read().splitlines()
print lines

all_devices = [sw1, sw2, sw3, sw4, sw5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print output

