from netmiko import ConnectHandler
from datetime import datetime

SW1 = {
    'device_type': 'cisco_ios',
    'ip': 'sw1',
    'username': 'roberto',
    'password': 'cisco'}

SW2 = {
    'device_type': 'cisco_ios',
    'ip': 'sw2',
    'username': 'roberto',
    'password': 'cisco'}

SW3 = {
    'device_type': 'cisco_ios',
    'ip': 'sw3',
    'username': 'roberto',
    'password': 'cisco'}

SW4 = {
    'device_type': 'cisco_ios',
    'ip': 'sw4',
    'username': 'roberto',
    'password': 'cisco'}

SW5 = {
    'device_type': 'cisco_ios',
    'ip': 'sw5',
    'username': 'roberto',
    'password': 'cisco'}

all_devices = [SW5, SW4, SW3, SW2, SW1]
core_devices = [SW2, SW1]
access_devices = [SW5, SW4, SW3]

with open('get_status_cmd') as n:
    lines = n.read().splitlines()

print("Connecting to Core Devices...")
print(lines)
print("Total commands to be applied: {}".format(len(lines)))

for devices in core_devices:
    start_time = datetime.now()
    ip = devices['ip']
    start_msg = str("Getting status of host {} on {}\n\n".format(ip, start_time))
    net_connect = ConnectHandler(**devices)
    output = ''
    for cmd in lines:
        prompt = str(net_connect.find_prompt())
        output = output + str('\n\n{} {}\n'.format(prompt, cmd))
        output = output + net_connect.send_command(cmd)

    print start_msg
    print output
    file = open(("{}_{}.txt".format(ip, start_time)), "w")
    file.write(start_msg)
    file.write(output)
    file.close()

with open('get_status_cmd') as n:
    lines = n.read().splitlines()

print("Connecting to Access Devices...")
print(lines)
print("Total commands to be applied: {}".format(len(lines)))

for devices in access_devices:
    start_time = datetime.now()
    ip = devices['ip']
    start_msg = str("\n\nGetting status of host {} on {}\n\n".format(ip, start_time))
    net_connect = ConnectHandler(**devices)
    output = ''
    for cmd in lines:
        prompt = str(net_connect.find_prompt())
        output = output + str('\n\n{} {}\n'.format(prompt, cmd))
        output = output + net_connect.send_command(cmd)

    print
    print start_msg
    print output
    file = open(("{}_{}.txt".format(ip, start_time)), "w")
    file.write(start_msg)
    file.write(output)
    file.close




"""
with open('get_status_cmd') as n:
    lines = n.read().splitlines()

print("Connecting to Access Devices...")

for devices in access_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command(lines)
    start_time = datetime.now()
    start_msg = str("Getting status of host {} on {}".format(devices, start_time))
    print start_msg
    print output
    file = open("{}-start_time.txt".format(devices), "w")
    file.write(start_msg)
    file.write(output)
"""