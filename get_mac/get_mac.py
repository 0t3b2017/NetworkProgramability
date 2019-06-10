#!/usr/bin/env python3

### Script to get mac, interface, vlan on Cisco switches

import os
import re
import subprocess
from pprint import pprint

nodes = [
        "xba-02-01.net.intranet",
        ]

# variables
reserved_vlans = [1002, 1003, 1004, 1005]
snmp_community = os.environ.get('PY_SNMP_COMMUNITY')
vlan_id_oid = ".1.3.6.1.4.1.9.9.46.1.3.1.1.2"
vlan_mac_oid = ".1.3.6.1.2.1.17.4.3.1.1"
vlan_bridge_ports = ".1.3.6.1.2.1.17.4.3.1.2"
vlan_port_index = ".1.3.6.1.2.1.17.1.4.1.2"
vlan_port_name = ".1.3.6.1.2.1.31.1.1.1.1"

full_list = []
vlans_list = []
macs_dict = {}
bridge_port_dict = {}
bridge_ifindex_dict = {}
port_name_ifindex = {}

def mac_converter(mac_address):
    s = re.compile('\.|-|:|\s')
    mac_address_split = s.split(mac_address)
    for p, i in enumerate(mac_address_split):
        if len(i) < 2:
            mac_address_split[p] = '0{}'.format(i)
    mac_addr = ''.join(mac_address_split).lower()
    new_mac = ''
    while len(mac_addr) > 0:
        new_mac += mac_addr[:2] + ':'
        mac_addr = mac_addr[2:]
    new_mac = new_mac.rstrip(':')
    return new_mac

#for node in nodes.splitlines():
for node in nodes:
    if not node or node.startswith('#'):
        continue

    ## Step 1
    cmd = "snmpwalk -v2c -c " + snmp_community + " " +  node + " " + vlan_id_oid
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    result_ascii = result.stdout.decode('ascii')

    for vlan_id in result_ascii.splitlines():
        vlans_list.append(vlan_id.split('=')[0].split('.')[-1])

    for vlan in vlans_list:
        #print("Checking vlan {}".format(vlan))
        # Run SNMP commands to obtain the results for each vlan
        if vlan not in reserved_vlans:
            ## Used for Step 2
            cmd = "snmpwalk -v2c -c " + snmp_community + "@" + vlan + " " + "-On" + " " + node + " " + vlan_mac_oid
            result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
            macs_result = result.stdout.decode('ascii')

            ## Used for Step 3
            cmd = "snmpwalk -v2c -c " + snmp_community + "@" + vlan + " " + "-On" + " " + node + " " + vlan_bridge_ports
            result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
            bridge_result = result.stdout.decode('ascii')

            ## Used for Step 4
            cmd = "snmpwalk -v2c -c " + snmp_community + "@" + vlan + " " + "-On" + " " + node + " " + vlan_port_index
            result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
            bridge_ifindex_result = result.stdout.decode('ascii')

            ## Used for Step 5
            cmd = "snmpwalk -v2c -c " + snmp_community + "@" + vlan + " " + "-On" + " " + node + " " + vlan_port_name
            result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
            port_ifindex_result = result.stdout.decode('ascii')

            ## Step 2 - Obtain the MAC address table for each vlan
            macs_dict[vlan.strip()] = []
            for mac_addr in macs_result.splitlines():
                if "No Such Instance currently exists at this OID" in mac_addr:
                   continue
                #print(vlan, mac_addr)
                mac_addr_str = mac_addr.split('Hex-STRING:')[1].strip()
                mac_index = mac_addr.split('=')[0].split(vlan_mac_oid)[1].strip()
                macs_dict[vlan.strip()].append((mac_addr_str, mac_index))

            ## Step 3 - Determine the bridge port number for each vlan
            bridge_port_dict[vlan.strip()] = []
            for bridge_port in bridge_result.splitlines():
                if "No Such Instance currently exists at this OID" in bridge_port:
                   continue
                bridge_port_str = bridge_port.split('INTEGER:')[1].strip()
                mac_index = bridge_port.split('=')[0].split(vlan_bridge_ports)[1].strip()
                bridge_port_dict[vlan.strip()].append((bridge_port_str, mac_index))

            ## Step 4 - Map the bridge port to the ifindex
            bridge_ifindex_dict[vlan.strip()] = []
            for bridge_ifindex in bridge_ifindex_result.splitlines():
                if "No Such Instance currently exists at this OID" in bridge_port:
                   continue
                bridge_ifindex_str = bridge_ifindex.split('INTEGER:')[1].strip()
                port_index = bridge_ifindex.split('=')[0].split('.')[-1].strip()
                bridge_ifindex_dict[vlan.strip()].append((bridge_ifindex_str, port_index))

            ## Step 5 - Correlate the ifindex value with port name
            port_name_ifindex[vlan.strip()] = []
            for port_name in port_ifindex_result.splitlines():
                if "No Such Instance currently exists at this OID" in bridge_port:
                   continue
                port_name_str = port_name.split('STRING:')[1].strip()
                port_index = port_name.split('=')[0].split('.')[-1].strip()
                port_name_ifindex[vlan.strip()].append((port_name_str, port_index))

       # Step 6 - Link MAC address to port on which the address was learned
       # Generate a list with the following model
       # node, vlan, mac_addr, ifname

            for i in macs_dict[vlan.strip()]:
                mac_index = i[1]
                mac_addr = i[0]
                new_mac = mac_converter(mac_addr)
                for x in bridge_port_dict[vlan.strip()]:
                    if x[1] == mac_index:
                        bridge_port = x[0]
                        #print('bridge_port ' + bridge_port)
                        #break
                        for y in bridge_ifindex_dict[vlan.strip()]:
                            if y[1].strip() == bridge_port:
                                index = y[0]
                                #print('index ' + index)
                                #break
                                for k in port_name_ifindex[vlan.strip()]:
                                    if k[1].strip() == index:
                                        port_name = k[0]
                                        #print(port_name)
                                        full_list.append((node, vlan.strip(), new_mac, port_name))

pprint(full_list)
#print("MACS found on VLAN453: ")
#print(macs_dict['453'])
#print(port_name_ifindex)

