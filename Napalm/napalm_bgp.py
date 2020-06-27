import json
from napalm import get_network_driver
driver = get_network_driver('ios')
ip = ['192.168.122.72','192.168.122.71']
for host in ip:
    devices = driver(host, 'prajwal', 'cisco')
    devices.open()
    print("connecting to ",host)
    bgp_neighbors = devices.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent=4))

    devices.close()

