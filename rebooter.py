import sys
import telnetlib

HOST = "192.168.1.1"
user = "admin"
password = "admin"

tn = telnetlib.Telnet(HOST)

print tn.read_until("Login: ")
tn.write(user + "\n")

print tn.read_until("Password: ")
tn.write(password + "\n")

tn.write("reboot\n")
tn.write("exit\n")

print tn.read_all()
