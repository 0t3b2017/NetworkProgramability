# coding=utf-8

# Script para desativação de interfaces - Cisco IOS

from netmiko import ConnectHandler

import re

ip = '10.255.255.254'
user = 'uolcsredes'
pwd = 'mudar123'
int = '0/0'

sw1 = {
    'device_type': 'juniper',
    'ip': ip,
    'username': user,
    'password': pwd,
}

if_name = re.compile(r'ge-\d/\d/\d')

net_connect = ConnectHandler(**sw1)
output = net_connect.send_command('show interface terse')
#print(output)

# coding=utf-8

# Script para desativação de interfaces - Cisco IOS

from netmiko import ConnectHandler
import re

ip = '10.255.255.254'
user = 'uolcsredes'
pwd = 'mudar123'
int = '0/0'

sw1 = {
    'device_type': 'juniper',
    'ip': ip,
    'username': user,
    'password': pwd,
}

if_name = re.compile(r'ge-\d/\d/\d+\s')

net_connect = ConnectHandler(**sw1)
output = net_connect.send_command('show interface terse')
#print(output)

interfaces = if_name.findall(output)
#print(interfaces)

found = False

for interface in interfaces:
    if interface.strip().endswith(int):
        found = True
        int_name = interface
        print(int_name)
        
        int_status = net_connect.send_command('show interfaces {} terse media'.format(interface))
        #print(int_status)
        if 'down' in int_status:
            output = net_connect.send_command('show configuration interface {} | display set'.format(interface))
            out_cmd = net_connect.send_config_set(output.replace('set', 'delete'), exit_config_mode=False)
            print(out_cmd)
            #output = net_connect.send_command('copy run startup'.format(interface))
            output = net_connect.commit()
            print(output)

            print('')
            print('## Configurações removidas da interface {}.##'.format(int_name))

        else:
            print('Interface {} está UP. Nenhuma alteração foi realizada.'.format(interface.strip()))

if not found:
    print('Nenhuma interface contém {}'.format(int))
