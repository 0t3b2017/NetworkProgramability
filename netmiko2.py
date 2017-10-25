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

all_devices = [sw1, sw2, sw3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    """
    for n in range(2, 21):
        print "Creating VLAN ", str(n)
        config_commands = ['vlan ' + str(n), 'name Netmiko2_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print output

    """
    config_commands = ['username oteb privilege 15 password cisco',
                       'no banner motd',
                       'no banner exec',
                       'no banner login',
                       'no banner incoming',
                       'ip ssh version 2',
                       'ip ssh authentication-retries 2',
                       'ip ssh time-out 120',
                       'enable secret cisco'
                       ]
    output = net_connect.send_config_set(config_commands)
    print output

