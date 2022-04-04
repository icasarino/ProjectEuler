# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:00:45 2022

@author: Ignacio
"""

limit=1000000


def intToBin(num:int):
    return str(bin(num))[2:]

def isPalindromic(num:str):
    
    #for i in range((len(num)//2)+1):
    #    if not num[i] == num[len(num) - 1 - i]:
   #         return False
  #return True
  
  return num == num[::-1]
    
def isDoublePalindromic(num:int):
    
    return isPalindromic(str(num)) and isPalindromic(intToBin(num))
    
    
    

result = 0
for i in range(limit):
    if i & 1 == 0:
        continue
    
    if isDoublePalindromic(i):
        result += i

print(result)
    