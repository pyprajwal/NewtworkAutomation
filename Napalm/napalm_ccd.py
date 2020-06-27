import json
from napalm import get_network_driver
driver = get_network_driver('ios')
host = ['192.168.122.72','192.168.122.73']
for ip in host:
    devices = driver(ip, 'prajwal', 'cisco')
    devices.open()

    print ('Accessing ',ip)
    devices.load_merge_candidate(filename='acl1.cfg')
    diffs = devices.compare_config()
    if len(diffs) > 0:
        print(diffs)
        choice = input("Y commit , N discard ")
        if choice == 'Y':
            print('Commiting ...')
            devices.commit_config()
            devices.close()
            print('commited!!!')
        elif choice == 'N':
            print('discarding..')
            devices.discard_config()
            devices.close()
        else:
            print("Press 'Y' commit or 'N' discard  ")

    else:
        print('No changes required.')
        devices.discard_config()

    devices.close()
