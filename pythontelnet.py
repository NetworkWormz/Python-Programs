import getpass
import sys
import telnetlib

HOST = "192.168.2.15"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")
tn.write("int lo 0\n")
tn.write("ip add 1.1.1.1 255.255.255.0\n")
tn.write("no shutdown\n")
tn.write("end\n")
tn.write("exit\n")


print tn.read_all()


