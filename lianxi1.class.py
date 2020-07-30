#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

class Person():

    def __init__(self, name, weight_code = 80):
        self.name = name
        self.weight_code = weight_code

    def level(self):
        if self.name == 'heping':
            print(f'{self.name} is HCIE-DC、CCIE-RS、RHCE、RHCSA')
        elif self.name == 'zhangjian':
            print(f'{self.name} is HCNP-Cloud、CCNP-RS')
        else:
            print('No person can finded')

    def weight(self):
        print(f'{self.name} weight is {weight_code} kg')


heping = Person('heping')
heping.level()
