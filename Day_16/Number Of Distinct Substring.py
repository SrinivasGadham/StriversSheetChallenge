from os import *
from sys import *
from collections import *
from math import *

def distinctSubstring(word):
    n=len(word)
    d=defaultdict(int)
    for i in range(len(word)):
        
        for j in range(i,n):
            s=word[i:j+1]
        
            
        
            
            
            d[s]=1
    # print(d)
    return len(d)

    
