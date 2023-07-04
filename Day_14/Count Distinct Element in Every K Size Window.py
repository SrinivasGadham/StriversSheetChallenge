from os import *
from sys import *
from collections import *
from math import *
def countDistinctElements(arr, k):
    n=len(arr)
    if k==1:
        return [1 for i in range(n)]
    d={}
    ele=0
    for i in range(k):
        if d.get(arr[i])==None:
            d[arr[i]]=0
            ele += 1
        d[arr[i]] += 1
    j=0
    ans=[ele]
    for i in range(k,n):
        d[arr[j]] -= 1
        if d[arr[j]]==0:
            ele -= 1
        if d.get(arr[i],0)==0:
            d[arr[i]]=0
            ele += 1
        d[arr[i]] += 1
        ans.append(ele)
        j += 1
    return ans
    
  