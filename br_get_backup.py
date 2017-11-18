from netmiko import ConnectHandler
from datetime import datetime

sw1 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.15.1',
    'username': 'roberto',
    'password': 'cisco',
}

sw2 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.15.2',
    'username': 'roberto',
    'password': 'cisco',
}

sw3 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.15.3',
    'username': 'roberto',
    'password': 'cisco',
}

sw4 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.15.4',
    'username': 'roberto',
    'password': 'cisco',
}

r1 = {
    'device_type': 'cisco_ios',
    'ip': '136.166.97.253',
    'username': 'roberto',
    'password': 'cisco',
}

r2 = {
    'device_type': 'cisco_ios',
    'ip': '136.166.97.254',
    'username': 'roberto',
    'password': 'cisco',
}

ap1 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.15.21',
    'username': 'roberto',
    'password': 'cisco',
}

ap2 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.15.22',
    'username': 'roberto',
    'password': 'cisco',
}

ap3 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.15.23',
    'username': 'roberto',
    'password': 'cisco',
}

ap4 = {
    'device_type': 'cisco_ios',
    'ip': '172.31.15.24',
    'username': 'roberto',
    'password': 'cisco',
}

aps = [ap1, ap2, ap5, ap4]
routers = [r1, r2]
switches = [sw4, sw3, sw2, sw1]
all = [ap1, ap2, ap3, ap4, r1, r2, sw4, sw3, sw2, sw1]

with open('br_get_status_aps') as f:
    lines = f.read().splitlines()
print "\033[33mGetting config access-point...\033[m"
print lines

for devices in aps:
    net_connect = ConnectHandler(**devices)
    output = nnet_connect.send_command("show running-config")
    dt = datetime.now()
    print output
    file = open("bkp_{}_{}".format(devices, datetime.now().strftime('%Y-%m-%d_%H-%M')), "w")
    file.write(output)
    file.close()

