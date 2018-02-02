# The intention of this scritp is to create a big configuration for get output status...

from netmiko import ConnectHandler
import re

qtd_vlan = 56

with open('big_config_devices') as f:
    devices = f.read().splitlines()

for device in devices:
    sw = {
        'device_type': 'cisco_ios',
        'ip': device,
        'username': 'roberto',
        'password': 'cisco',
    }

    net_connect = ConnectHandler(**sw)

    comandos = ''

    ## Create vlans
    # for i in range(105, 177):
    #   comandos += "vlan {} \n name VLAN_{} \n".format(i, i)

    vlans_regex = re.compile(r'^\d+', flags=re.MULTILINE)
    sh_vlan = net_connect.send_command('show vlan brief')
    #print(sh_vlan)
    vlans = vlans_regex.findall(str(sh_vlan))
    print(vlans)
    for vlan in vlans:
        #print(vlan)
        comandos += 'interfprint(vlan)##### FIXME FIXMEace vlan {} \n hsrp 1 \n'.format(vlan)

    output = net_connect.send_config_set(comandos)
    #output += net_connect.send_config_set("name VLAN{}".format(i))
    print(output)
