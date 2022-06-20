#!/usr/bin/python3
import getpass
import telnetlib

# Telnet into Router R1 

HOST = "192.168.122.9"
user = input("Enter your telnet username: ")

password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")

tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
# Be sure that if you configured enable password you should use this section :
tn.write(b"enable\n")
tn.write(b"cisco\n")
# If you did not use enable password start from this section
tn.write(b"conf t\n")
tn.write(b"int l0\n")
# sample config that you would be sure that you changed your configuration
tn.write(b"des THIS IS JUST FOR TEST\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"exit\n")
# **End section should be exactly like this line**
print(tn.read_all())
