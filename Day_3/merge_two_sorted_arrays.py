from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    i=0 
    j=0
    res=[]
    while i<(m+n):
        
        if arr1[i]>=arr2[j]:
            arr1[i],arr2[j]=arr2[j],arr1[i]
            i+=1
        else:
            i+=1
            
    if i<m:
        for k in range(i,m):
            res.append(arr1[k])
            
    if j<n:
        for k in range(j,n):
            res.append(arr2[k])
    # print("Res=",res)
    arr1=res
    return arr1
    




    # Write your code here.
    pass
