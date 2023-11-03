# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:18:50 2023

@author: s_kryzanovskij20
"""

def vokon_zählen(x):
    wort = x.lower()
    count_buch = 0
    count_vok = 0
    vokalen = "aeiou"
    
    for i in wort:
        if i.isalpha():
            count_vok += 1
            if i in vokalen:
                count_vok += 1
                    
                    
        print(f"Es gibt {count_vok} vokalen und {count_buch-count_vok} Konsonanten")

print(vokon_zählen("HelloBerlin"))

