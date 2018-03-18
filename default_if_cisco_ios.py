# coding=utf-8

# Script para desativação de interfaces - Cisco IOS

from netmiko import ConnectHandler
import re

ip = '192.168.80.129'
user = 'roberto'
pwd = 'cisco'
int = '0/0'

sw1 = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': user,
    'password': pwd,
}

if_name = re.compile(r'\w+\d/\d')

net_connect = ConnectHandler(**sw1)
output = net_connect.send_command('show ip int brief')
#print(output)

interfaces = if_name.findall(output)
found = False
for interface in interfaces:
    if int in interface:
        found = True
        int_name = interface
        int_status = net_connect.send_command('show int {} status'.format(interface))
        #print(int_status)
        if 'notconnected' in int_status or 'disabled' in int_status:
            output = net_connect.send_config_set('default interface {}'.format(interface))
            print(output)
            #output = net_connect.send_command('copy run startup'.format(interface))
            output = net_connect.send_command('wr')
            print(output)
            print('')
            print('## Configurações removidas da interface {}. ##'.format(int_name))
        else:
            print('Interface {} está UP. Nenhuma alteração foi realizada.'.format(interface))

if not found:
    print('Nenhuma interface contém {}'.format(int))
