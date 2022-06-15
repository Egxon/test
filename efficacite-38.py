# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 19:17:03 2022

@author: XXX Anonymized by JMB XXX
"""

# Retourne une chaine de caractères en supprimant les espaces
# S'il existe des espaces consécutifs, ceux-ci ne sont pas supprimés
def erase(cc):
    newStr=""
    lengthStr = len(cc)
    for i in range(0,lengthStr):
        char = cc[i]
        if ord(char) != 32:
            newStr+=char
        else:
            if ((i+1<lengthStr) & (i-1>=0)):
                if (ord(cc[i+1]) == 32) | (ord(cc[i-1]) == 32):
                    newStr+=char
    return newStr
