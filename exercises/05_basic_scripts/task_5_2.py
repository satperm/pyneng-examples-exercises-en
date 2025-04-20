# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip = input('Ask the user to enter the IP network in the format: ').split('/')
ip_add_str = ip[0]
ip_add_list = ip_add_str.split('.')
ip_mask = ip[1]
ip_mask_str = int(ip_mask)*'1'+(32-int(ip_mask)*1)*'0'
ip_mask_list = [ip_mask_str[0:8],ip_mask_str[8:16],ip_mask_str[16:24], ip_mask_str[24:32]]
ip_template = '''Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
mask_template = '''Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
'''
print(ip_template.format(int(ip_add_list[0]),int(ip_add_list[1]),int(ip_add_list[2]),int(ip_add_list[3])))
print(mask_template.format(ip_mask,int(ip_mask_list[0],2),int(ip_mask_list[1],2),int(ip_mask_list[2],2),int(ip_mask_list[3],2)))