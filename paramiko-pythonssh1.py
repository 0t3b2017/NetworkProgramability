import paramiko
import time

ip_address = "192.168.122.253"
username = "roberto"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address, username=username, password=password)

print "Successful connection", ip_address

client = ssh_client.invoke_shell()

client.send("configure terminal\n")
client.send("int loop 0\n")
client.send("ip address 1.1.1.1 255.255.255.255\n")
client.send("int loop 1\n")
client.send("ip address 2.2.2.2 255.255.255.255\n")
client.send("router ospf 1\n")
client.send("network 0.0.0.0 255.255.255.255 area 0\n")

for n in range(2, 21):
    print "Creating VLAN " + str(n)
    client.send("vlan " + str(n) + "\n")
    client.send("name Python_VLAN " + str(n) + "\n")
    time.sleep(0.5)

client.send("end\n")

time.sleep(1)
output = client.recv(65535)
print output
print type(output)

ssh_client.close
