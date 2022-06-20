#!/usr/bin/env python3

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type':'cisco_ios',
    'ip':'192.168.122.72',
    'username':'cisco',
    'password':'cisco',
}

net_connect = ConnectHandler(**iosv_l2_s1)
ouput = net_connect.send_command('show ip int brief')
print(ouput)
print(f"\n Cisco SWitch Version \n")
ouput = net_connect.send_command('show version')
print(ouput)
