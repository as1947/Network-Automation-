#!/usr/bin/python3
import getpass
import telnetlib

HOST = "192.168.122.72"
user = input("Enter your telnet username: ")

password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
# Be sure that if you configured enable password you should use this section :

tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name Python_VLAN_2_New\n")
tn.write(b"exit\n")
tn.write(b"end\n")
tn.write(b"exit\n")

# **End section should be exactly like this line**
print(tn.read_all())
