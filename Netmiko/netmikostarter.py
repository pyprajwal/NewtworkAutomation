from netmiko import ConnectHandler
#Create a dictionary representing the device.
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'prajwal',
    'password': 'cisco',
}
print("connecting to ",iosv_l2_s1['ip'])
# Establish an SSH connection to the device by passing in the device dictionary.
net_connect = ConnectHandler(**iosv_l2_s1)

# Execute show commands.
# output = net_connect.send_command('show ip int brief')
# print(output)

# Execute configuration change commands (will automatically enter into config mode)
config_command=[ 'do show ip int brief',
                "router ospf 1",
                "network 0.0.0.0 255.255.255.255 area 0"]

output1 = net_connect.send_config_set(config_command)
print(output1)

# enable
# conf t
# username prajwal priv 15 password 0 cisco
#
# line vty 0 4
#     login local
#     transport input all
#
# ip domain-name cciepython.com
# crypto key generate rsa
# 1024

# end
# wr