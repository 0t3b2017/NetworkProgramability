from netmiko import ConnectHandler
from datetime import datetime

nx01 = {
    'device_type': 'cisco_nxos',
    'ip': '192.168.122.71',
    'username': 'admin',
    'password': 'admin'}

nx02 = {
    'device_type': 'cisco_nxos',
    'ip': '192.168.122.72',
    'username': 'admin',
    'password': 'admin'}


all_devices = [nx01, nx02]
core_devices = [nx01, nx02]

with open('get_nxos_status_cmd') as n:
    lines = n.read().splitlines()

print("Connecting to Core Devices...")
print("Commands to execute")
print(lines)
print("Total commands to be applied: {}".format(len(lines)))

for devices in core_devices:
    start_time = datetime.today().strftime('%Y%b%d-%H%M')
    ip = devices['ip']
    start_msg = str("Getting status of host {} on {}\n\n".format(ip, start_time))
    net_connect = ConnectHandler(**devices)
    output = ''
    hostname = str(net_connect.send_command('show hostname')).strip()
    for cmd in lines:
        prompt = str(net_connect.find_prompt())
        output += str('\n\n{} {}\n'.format(prompt, cmd))
        output += net_connect.send_command_timing(cmd)
        #output += net_connect.send_command(cmd)

    print start_msg
    print output
    file = open(("{}_{}.txt".format(hostname, start_time)), "w")
    file.write(start_msg)
    file.write(output)
    file.close()
"""
    ## Make tftp copy of running-config and startup config
    output += net_connect.send_command_timing('copy running-config tftp://192.168.122.10/backup vrf management')
    print(output)
    file = open(("{}_{}-running"), "w")
    file.write(start_msg)
    file.write(output)
    file.close()

    output += net_connect.send_command_timing('copy running-config tftp://192.168.122.10/backup vrf management')
    print(output)
    file = open(("{}_{}-running"), "w")
    file.write(start_msg)
    file.write(output)
    file.close()
"""
"""
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