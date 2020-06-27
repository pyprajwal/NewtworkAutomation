import json
from napalm import get_network_driver
driver = get_network_driver('ios')
host = ['192.168.122.72','192.168.122.73']
for ip in host:
    devices = driver(ip, 'prajwal', 'cisco')
    devices.open()

    print ('Accessing ',ip)
    devices.load_merge_candidate(filename='acl1')
    diffs = devices.compare_config()
    if len(diffs) > 0:
        print(diffs)
        devices.commit_config()
    else:
        print('No changes required.')
        devices.discard_config()

    devices.close()
