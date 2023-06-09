from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    uni=set(arr)
    d={}
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]]=[]
            d[arr[i]].append(i)
        else:
            d[arr[i]].append(i)
    res=[]
    for i in range(len(arr)):
        if s-arr[i] in d:
            for x in d[s-arr[i]]:
                if x<i:
                    res.append(sorted([arr[i],s-arr[i]]))
    res.sort(key=lambda x:x[0])
    return res
                
    


        