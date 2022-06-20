# Network-Automation
Python Scripts for Network Automation

Python scripts fro router and switch configuration
We programmatically configured the loopback addresses and OSPF on the Cisco IOS of the router 

## The router was given this IP address through DHCP.
```
conf t 
ip dhcp client update dns
ip address dhcp
```
## Configure the switch manually, We have to specify the IP address here,so we'll use 72. So hostname switch1. 
```
S1(config)#int vlan 1
S1(config-if)#ip add 192.168.122.72 255.255.255.0
S1(config-if)#exit
```
## We need to configure login details on switch 

## Configure switch for ssh 
```
S1(config)#username cisco pass
S1(config)#username cisco password cisco
S1(config)#username cisco privilege 15
S1(config)#line vty 0 4
S1(config-line)#login local
S1(config-line)#transport input all
S1(config-line)#exit
S1(config)#ip domain-name gns3lab.com
S1(config)#crypto key generate rsa
The name for the keys will be: S1.gns3lab.com
Choose the size of the key modulus in the range of 360 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [512]: 1024
% Generating 1024 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

S1(config)#
*Jun 20 05:26:30.468: %SSH-5-ENABLED: SSH 1.99 has been enabled
S1(config)#end
S1#wr
Warning: Attempting to overwrite an NVRAM configuration previously written
by a different version of the system image.
Overwrite the previous NVRAM configuration?[confirm]
*Jun 20 05:26:37.389: %SYS-5-CONFIG_I: Configured from console by console
[confirm]
Building configuration...
Compressed configuration from 1604 bytes to 941 bytes[OK]
```
### Check SSH and telnet connection to the switch  

ssh cisco@192.168.122.72

