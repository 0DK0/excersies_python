# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:52:44 2023

@author: s_kryzanovskij20
"""

a = 1
r = 0.5
s = 0 
k = 0
limit = a/(1 - r)

while True:
    s+= a * r**k
    k+= 1
    
    print (s, end = " ")
    
    if s == limit :
        break
    







