import getpass
import telnetlib
#telnet to mutiple host from the list.

HOST = ["192.168.122.71","192.168.122.72"]

for host in HOST:
    print("connecting to host: ",host)
    user = input("Enter your telnet username: ")
    password = getpass.getpass()

    tn = telnetlib.Telnet(host)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")


        tn.write(b"conf t\n")
        for n in range(2,10):
            tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
            tn.write(b"name Vlan_name_" + str(n).encode('ascii') + b"\n")

        tn.write(b"end\n")
        tn.write(b"wr\n")
        tn.write(b"exit\n")

        print(tn.read_all().decode('ascii'))
