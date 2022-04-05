# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:04:48 2022

@author: Ignacio
"""

import custmath.generics as g

limit = 10**8
primes = g.sieveOfErathostenes(limit,False)
maximum = max(filter(g.isPandigital,primes))
print(maximum)