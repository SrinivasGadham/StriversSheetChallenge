from math import *
from collections import *
from sys import *
from os import *

def fourSum(arr, target):
    n=len(arr)
    d={}
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] not in d:
                d[arr[i]+arr[j]]=[]
                d[arr[i]+arr[j]].append([i,j])
            else:
                d[arr[i]+arr[j]].append([i,j])
    for i in range(n):
        for j in range(i+1,n):
            summ=arr[i]+arr[j]
            if target-summ in d:
                s=set()
                for x in d[summ]:
                    for y in x:
                        s.add(y)
                for x in d[target-summ]:
                    for y in x:
                        s.add(y)
                if len(s)>=4:
                    return "Yes"
    return "No"
                

    
