#! /usr/bin/env python3
# _*_ coding: utf-8 _*_
from IPy import IP, IPSet
iplist = []
filename = '/Users/heping/Documents/ProgramCodingBackup/Python/ip.txt'
'''
windows 路径可以写成 'D:\\ip.txt'
'''
with open(filename) as ipfile:
    for line in ipfile:
        line = line.strip()
        ipaddress = IPSet([IP(line)])
        for ip in ipaddress:
            iplist.append(ip)
    ipa = IPSet(iplist)
    for x in ipa:
        print(x)