'''
Created on 07/09/2016

@author: ernesto
'''

import sys 
import os
import operator

def  firstRepeatingLetter(s):
    min_ocurrence_idx = 256
    first_repeated_char = ""
    char_first_ocurrence = {}
    char_repeated = {}
    
    for char_idx, char_s in enumerate(s):
        if(char_s in char_first_ocurrence):
            if(char_s not in char_repeated):
                char_repeated[char_s] = char_first_ocurrence[char_s]
        else:
            char_first_ocurrence[char_s] = char_idx
    
    
    if(s):
        for char_s, char_idx in char_repeated.items():
            if(char_idx < min_ocurrence_idx):
                min_ocurrence_idx = char_idx
                first_repeated_char = char_s
    
    return first_repeated_char
    

f = open(os.environ['OUTPUT_PATH'], 'w')

_a = str(input())

res = firstRepeatingLetter(_a)
print(res + "\n")
f.write(res + "\n")

f.close()
