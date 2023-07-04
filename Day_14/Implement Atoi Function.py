from os import *
from sys import *
from collections import *
from math import *

def atoi(s):
    l=list(s.strip())
    if len(l)==0:return 0
    sign = -1 if l[0]=='-' else 1

    if l[0] in "+-":del[l[0]]
    res = ""
    ret,i=0,0
    while i<len(l) and l[i].isdigit():
        res+=l[i]
        i+=1
    if len(res)==0:
        return 0
    else:
        x=int(res)
        return min((2<<30)-1,max(x*sign,-2<<30))
    
    
