# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:52:49 2022

@author: hyyu
"""

def prime(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                return '非植樹'
        return '植樹'
    else:
        return '非植樹'
while True:    
    a=eval(input('please input one number:'))
    if a!=-9999:
        print('{}為{}'.format(a,prime(a)))
    else:
        break
   