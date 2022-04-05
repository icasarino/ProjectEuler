# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 20:29:54 2022

@author: Ignacio
"""

from math import sqrt

def evalPitagoras(a,b):
    return sqrt(b**2 + a**2)

def evalPerimetro(p,a,b,c):
    return p == a + b + c

perim = 1000
maxLen = 0
maxPerim = 0 
c = 0
for p in range(perim+1):
    resultados = []
    for a in range(1,int(p*0.5)):
        for b in range(1,int(p*0.5)):
            c = evalPitagoras(a, b)
            if evalPerimetro(p, a, b, c):
                r = [a,b,c]
                r.sort()
                resultados.append(r)

    maxCurrLen = len(set(map(tuple,resultados)))
    if maxCurrLen > maxLen:
        maxLen = maxCurrLen
        maxPerim = p
    
print(maxPerim, maxLen)




