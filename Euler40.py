# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:30:05 2022

@author: Ignacio
"""

concat = ''
i = 1
while len(concat) < 1000000:
    concat += str(i)
    i += 1

result = 1
for i in range(7):
    result *= int(concat[(10**i)-1])

print(result)
