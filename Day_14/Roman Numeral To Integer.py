from os import *
from sys import *
from collections import *
from math import *

def romanToInt(s):
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    i=0
    count=0
    while(i<len(s)):
        if i==len(s)-1:
            count+=d[s[i]]
            i+=1
            
        elif d[s[i]]>=d[s[i+1]]:
            count+=d[s[i]]
            i+=1
        else:
            count=count-d[s[i]]+d[s[i+1]]
            i+=2
    return count


