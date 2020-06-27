import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'prajwal', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print (json.dumps(ios_output, indent=4))

iosvl2.close()

##**********************without json format*****************************************#######
# from napalm import get_network_driver
# driver = get_network_driver('ios')
# iosvl2 = driver('192.168.122.72', 'prajwal', 'cisco')
# iosvl2.open()
#
# ios_output = iosvl2.get_facts()
# print (ios_output)