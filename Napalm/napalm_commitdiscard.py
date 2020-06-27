import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.73', 'prajwal', 'cisco')
iosvl2.open()

print ('Accessing 192.168.122.73')
iosvl2.load_merge_candidate(filename='acl1')
diffs = iosvl2.compare_config()
print(diffs)
choice = input("Y commit , N discard ")
if choice == 'Y':
    print('Commiting ...')
    iosvl2.commit_config()
    iosvl2.close()
    print('commited..')
elif choice == 'N':
    print('discarding..')
    iosvl2.discard_config()
    iosvl2.close()
else:
    print("Press 'Y' commit or 'N' discard  ")
    return(choice)

