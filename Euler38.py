# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 19:53:05 2022

@author: Ignacio
"""


limit = 50000

def getConcat(num):
    
    concat = str(num)
    
    for i in range(2,7):
        concat += str(num*i)
        if len(concat) >= 9:
            break

    return concat

def validLength(concat):
    return len(concat) == 9


def isPandigital(concat):
    
    l = ['1','2','3','4','5','6','7','8','9']
    
    num = [elem for elem in l if elem in concat]
    
    return validLength(concat) and len(num) == 9



for base in range(limit):
    
    concatenation = getConcat(base)
    if isPandigital(concatenation):
        print(base,concatenation)    
    