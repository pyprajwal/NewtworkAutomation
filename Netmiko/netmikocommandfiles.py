from netmiko import ConnectHandler
from getpass import getpass
#Create a dictionary representing the device.

with open('commands_file') as f:
    commands_to_send = f.read().splitlines()

with open('hostfile') as f:
    all_devices = f.read().splitlines()



for devices in all_devices:
    print("connecting to ", devices)
    username = input("Enter your SSH username: ")
    password = getpass()
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password
    }
# Establish an SSH connection to the device by passing in the device dictionary.
    net_connect = ConnectHandler(**ios_device)
    for n in range(2, 11):
        print("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        outputs = net_connect.send_config_set(config_commands)
        print(outputs)

    output = net_connect.send_config_set(commands_to_send)
    print(output)
# Execute show commands.
#     output = net_connect.send_command('show ip int brief')
#     print(output)
