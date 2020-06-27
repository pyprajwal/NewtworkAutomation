import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

f = open ('myswitches')

for IP in f:
    IP=IP.strip()
    print ("Configuring Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"conf t\n")

        for n in range(2,11):
            tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
            tn.write(b"name Vlan_name_" + str(n).encode('ascii') + b"\n")

        tn.write(b"int loop 1\n")
        tn.write(b"ip add 2.2.2.2 255.255.255.255\n")

        # tn.write(b"router ospf 1\n")
        # tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")

        tn.write(b"end\n")
        tn.write(b"exit\n")
        print(tn.read_all().decode('ascii'))
