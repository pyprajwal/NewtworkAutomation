import json
from napalm import get_network_driver

devicelist = ['192.168.122.72',
           '192.168.122.73'
           ]

for ip_address in devicelist:
    print("\n*****************************************\n")
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv = driver(ip_address, 'prajwal', 'cisco')
    iosv.open()
    iosv.load_merge_candidate(filename='acl1.cfg')
    print("\n*****************************************\n")
    print("Checking for ACL configurations..")
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        choice = input("Y commit , N discard ")
        if choice == 'Y':
            print('Commiting ...')
            iosv.commit_config()

            print('commited!!!')
        elif choice == 'N':
            print('discarding..')
            iosv.discard_config()

        else:
          print("Press 'Y' commit or 'N' discard  ")

    else:
        print('No ACL changes required.')
        iosv.discard_config()

    iosv.load_merge_candidate(filename='ospf1.cfg')
    print("\n\n")
    print("Checking for OSPF configurations..")
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        choice = input("Y commit , N discard ")
        if choice == 'Y':
            print('Committing ...')
            iosv.commit_config()

            print('commited!!!')
        elif choice == 'N':
            print('discarding..')
            iosv.discard_config()

        else:
            print("Press 'Y' commit or 'N' discard  ")

    else:
        print('No OSPF changes required.')
        iosv.discard_config()
    iosv.close()




