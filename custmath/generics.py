# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:17:26 2022

@author: Ignacio
"""

def even(num:int):
    return num % 2 == 0

def odd(num:int):
    return num % 2 != 0


def sieveOfErathostenes(limit:int,ordered:bool=False):
    numbers = [x for x in range(limit)]
    
    for i in range(2,limit):
        if numbers[i] != 0:
            for j in range(i, limit, +i):
                if i != j:
                    numbers[j] = 0
    
    if ordered:
        return sorted(set(numbers) ^ {0,1})
    
    return set(numbers) ^ {0,1}


def isPrime(num:int):
    
    endVal = int(num/2) + 1

    for i in range(2,endVal):
        if num % i == 0:
            return False
    return True

def rotateLeft(num:int,amount:int):    
    numStr = str(num)
    return numStr[amount:] + numStr[:amount]

def rotateRight(num:int,amount:int):    
    numStr = str(num)
    return numStr[-amount:] + numStr[:-amount]

def isPandigital(num:int,n:int=False):
    
    numStr = str(num)
    
    ''' TO CHECK FOR SPECIFIC PANDIGITAL LENGTHS '''
    if not n:
        n = len(numStr) 
    ''' '''
    
    l = list(map(str,list(range(1,n+1))))

    nums = [elem for elem in l if elem in numStr]   
    return len(numStr) == n and len(nums) == n


