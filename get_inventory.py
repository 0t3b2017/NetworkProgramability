#!/usr/bin/env python3
# coding=utf-8

"""
Script para coletar informações dos equipamentos
"""

from netmiko import ConnectHandler
from datetime import datetime

date = datetime.now().strftime('%d-%b-%Y-%H:%M')

with open('cisco.txt') as f:
    devices = f.read().splitlines()

for HOST in devices:
    dv = {
        'device_type': 'cisco_ios',
        'ip': HOST,
        'username': 'roberto',
        'password': 'MyP@ssw0rd',
    }

    print(HOST)

    net_connect = ConnectHandler(**dv)

    output = ""
    output += ("#" * (len(HOST) + 6) + "\n")
    output += ("#" * 2) + " " + HOST + " " + ("#" * 2) + "\n"
    output += ("#" * (len(HOST) + 6) + "\n\n")
    output += "Gathering information at {}.\n\n".format(date)

    with open('cisco_commands.txt') as f:
        commands = f.read().splitlines()

    for CMD in commands:
        output += ("*" * (len(CMD) + 6) + "\n")
        output += ("*" * 2) + " " + CMD + " " + ("*" * 2) + "\n"
        output += ("*" * (len(CMD) + 6) + "\n\n")
        output += net_connect.send_command(CMD)

    file = open('output.txt', 'a')
    file.write(output)
    file.close()
