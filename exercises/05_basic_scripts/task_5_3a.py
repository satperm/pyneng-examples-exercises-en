# -*- coding: utf-8 -*-
"""
Task 5.3a

Copy and change the script from task 5.3 in such a way that, depending on
the selected mode, different questions were asked in the request for the VLAN number
or VLAN list:
* for access: 'Enter VLAN number:'
* for trunk: 'Enter the allowed VLANs:'

Restriction: All tasks must be done using the topics covered in this and previous chapters.
This task can be solved without using the if condition and for/while loops.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

intf_mode = input('Enter interface mode (access/trunk): ')
intf_name = input('Enter interface type and number: ')
vlan_dict = { 'trunk':'Enter the allowed VLANs:', 'access': 'Enter VLAN number:' }
vlan_number = input(vlan_dict[intf_mode])
print("interface "+ intf_name )

if intf_mode == 'access':
    for line in access_template:
        if line.startswith('switchport access vlan'):
            print(line.format(vlan_number))
        else:
            print(line)
else:
    for line in trunk_template:
        if line.startswith('switchport trunk allowed vlan'):
            print(line.format(vlan_number))
        else:
            print(line)