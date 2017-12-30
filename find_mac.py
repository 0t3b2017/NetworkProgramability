#!/usr/bin/env python
# coding=utf-8

"""
Script para encontrar mac-address na tabela CAM de diversos switches
"""

from netmiko import ConnectHandler
import re

mac = str(raw_input('Digite o MAC a ser procurado xxxx.xxxx.xxxx: ')).lower()

# mac_so = re.compile("[\dA-F]{2}[:-]{5}[\dA-F]{2}")

with open('switches.txt') as f:
    devices = f.read().splitlines()

for HOST in devices:

    sw = {
        'device_type': 'cisco_ios',
        'ip': HOST,
        'username': 'roberto',
        'password': 'cisco',
    }

    net_connect = ConnectHandler(**sw)
    line = net_connect.send_command('show mac address-table | inc {}'.format(mac))

    if line:
        interface = line.split()[-1]

        # PRINT SE A INTERFACE FOR ACESSO OU TRUNK
        # print("MAC Address {} encontrado na interafce {} do switch {}".format(mac, interface, HOST))

        # PRINT SE A INTERFACE FOR ACESSO
        out = net_connect.send_command('show interface ' + interface + ' switchport | inc Operational Mode')

        if 'access' in out:
            print("MAC Address {} encontrado na interafce {} do switch {}".format(mac, interface, HOST))
