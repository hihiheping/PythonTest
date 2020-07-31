#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

class Person():
    def __init__(self, name):
        self.name = name

    def level(self, cert = 10):
        self.cert = cert
        if self.name == 'heping':
            print(f'{self.name} is HCIE-DC CCIE-RS RHCE RHCSA')
        elif self.name == 'zhangjian':
            print(f'{self.name} is HCNP-Cloud CCNP-RS')
        else:
            self.cert = 2
            print(f'{self.name} has no any Certification')

    def pet(self):
        print(f'{self.name} working has {self.cert} years')

heping = Person('heping')
heping.level()
heping.pet()

fengyaru =Person('fengyaru')
fengyaru.level()
fengyaru.pet()