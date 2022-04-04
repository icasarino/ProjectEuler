# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:24:35 2022

@author: Ignacio
"""

limit = 1000000
limitSieve = 30000
discardedPrimes = []

def SieveOfErathostenes(lista:list):
    
    listaAux = lista.copy()
        
    for i in listaAux:
        for j in listaAux:
            if j % i == 0 and i != j:
                listaAux.remove(j)
    return listaAux




def even(num:int):
    
    return num & 1 == 0

def numFilter():


    SieveList = SieveOfErathostenes(list(range(2,limitSieve)))
    return [x for x in list(range(limit)) if not (even(x) or str(x)[0] == '9' or str(x)[-1] == '9' or (x <= limitSieve and x not in SieveList))]

def isPrime(num:int):

    if num == 1:
        return False
    endVal = int(num / 2) + 1    

    i = 2
    while i < endVal:
        if num % i == 0:
            return False
        i += 1
    return True
    

def isTruncatablePrime(num:int):
    
     
    prime = str(num)
    
    for i in range(len(prime)):
        if not isPrime(int(prime[i:])):
            return False
    
    for i in range(len(prime)):
        if not isPrime(int(prime[:-i+len(prime)])):
            return False
        
    return True




    
   
numbers = numFilter()[5:]
discardedPrimes = [2,3,5,7,11,13,17,19]

#print(primes)
count = 0
result = 0
i = 0


while count < 11 and i < len(numbers):

    if isTruncatablePrime(numbers[i]):
        count += 1
        result += numbers[i]
        print(numbers[i],count,result,i)
    i += 1  
    
print(result)
        
        
        
        
        
        
        
        
        
        