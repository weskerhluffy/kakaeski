'''
Created on 07/09/2016

@author: ernesto

'''

import sys 
import os

# The complexity for this algorithm is O(n+m) where n and m are the sizes of a and b strings respectively.
def  mergeStrings(a, b):
    # Initialize resulting string
    merged_string = ""
    
    # TODO: Validate that a and b are in fact strings
    # Store the sizes of the strings for convenience
    size_a = len(a)
    size_b = len(b)
    
    if(size_a > size_b):
        bigger_size = size_a
    else:
        bigger_size = size_b
    
    # Iterate thry the indexes of the bigger string and check that there are characters in each string for the given index to append to the resulting string
    for char_idx in range(bigger_size):
        if(char_idx < size_a):
            merged_string += a[char_idx]
        if(char_idx < size_b):
            merged_string += b[char_idx]
    
    return merged_string
        


f = open(os.environ['OUTPUT_PATH'], 'w')
    

_a = str(input())


_b = str(input())

res = mergeStrings(_a, _b);
print(res + "\n")
f.write(res + "\n")

f.close()
