from os import *
from sys import *
from collections import *
from math import *

def uniqueSubstrings(input ) :
    s=input

    n=len(s)
    i=0
    d={}
    ans=0
    for j in range(n):
        if s[j] in d:
            i=max(d[s[j]],i)
        ans=max(ans,j-i+1)
        d[s[j]]=j+1
    return ans

    # Write your code here.