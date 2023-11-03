# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:29:30 2023

@author: s_kryzanovskij20
"""

x = "Hello, Berlin"

x_liste = list(x)

count_letters = []

for buchstabe in x_liste:

    count_letters.append(buchstabe.isalpha())

print(sum(count_letters))

