# -*- coding: utf-8 -*-
"""
Task 5.2a

Copy and modify the script from task 5.2 so that, if the user entered a host address
rather than a network address, convert the host address to a network address
and print the network address and mask, as in task 5.2.

An example of a network address (all host bits are equal to zero):
* 10.0.1.0/24
* 190.1.0.0/16

Host address example:
* 10.0.1.1/24 - host from network 10.0.1.0/24
* 10.0.5.195/28 - host from network 10.0.5.192/28

If the user entered the address 10.0.1.1/24, the output should look like this:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different host/mask combinations, for example:
    10.0.5.195/28, 10.0.1.1/24

Hint:
The network address can be calculated from the binary host address and the netmask.
If the mask is 28, then the network address is the first 28 bits host addresses + 4 zeros.
For example, the host address 10.1.1.195/28 in binary will be:
bin_ip = "00001010000000010000000111000011"

Then the network address will be the first 28 characters from bin_ip + 0000
(4 because in total there can be 32 bits in the address, and 32 - 28 = 4)
00001010000000010000000111000000

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
ip = input('Ask the user to enter the IP network in the format: ').split('/')
ip_add_str = ip[0]
ip_add_list = ip_add_str.split('.')
ip_mask = ip[1]
ip_mask_str = int(ip_mask)*'1'+(32-int(ip_mask)*1)*'0'
ip_mask_list = [ip_mask_str[0:8],ip_mask_str[8:16],ip_mask_str[16:24], ip_mask_str[24:32]]
tmp_ip_template = '''
{0:08b}{1:08b}{2:08b}{3:08b}
'''
ip_add_bin_str = str(tmp_ip_template.format(int(ip_add_list[0]),int(ip_add_list[1]),int(ip_add_list[2]),int(ip_add_list[3])))
#print(ip_add_bin_str)
ip_add_bin_fin_str = ip_add_bin_str[0:int(ip_mask)+1]+(32-int(ip_mask)*1)*'0'
#print(ip_add_bin_fin_str)
ip_add_fin_list = [ip_add_bin_fin_str[1:9],ip_add_bin_fin_str[9:17],ip_add_bin_fin_str[17:25], ip_add_bin_fin_str[25:33]]

ip_template = '''Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
mask_template = '''Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
'''
print(ip_template.format(int(ip_add_fin_list[0],2),int(ip_add_fin_list[1],2),int(ip_add_fin_list[2],2),int(ip_add_fin_list[3],2)))
print(mask_template.format(ip_mask,int(ip_mask_list[0],2),int(ip_mask_list[1],2),int(ip_mask_list[2],2),int(ip_mask_list[3],2)))