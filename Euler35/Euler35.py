# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 12:14:06 2022

@author: Ignacio
"""

init = 2
end = 100000
globalNumList = list(range(init,end+1))

def SieveOfErathostenes(lista:list):
    
    listaAux = lista.copy()
        
    for i in listaAux:
        for j in listaAux:
            if j % i == 0 and i != j:
                listaAux.remove(j)
    return listaAux       
    

def rotate(num:int):
    
    numStr = str(num)
    
    rotations = []
    for _ in range(len(numStr)-1):
        numStr = numStr[1:] + numStr[:1]
        rotations.append(int(numStr))
      
    return rotations


def isPrime(num:int):

    endVal = int(num / 2) + 1    

    i = 2
    while i <= endVal:
        if num % i == 0:
            return False
        i += 1
    return True
      

def isCircularPrime(num:int):

    rotations = rotate(num)
    rotCheck = [x for x in rotations if isPrime(x)]

    return len(rotations) == len(rotCheck)



primesInRange = SieveOfErathostenes(globalNumList)
circularPrimesInRange = list(filter(lambda x: isCircularPrime(x), primesInRange))
print(len(circularPrimesInRange))








