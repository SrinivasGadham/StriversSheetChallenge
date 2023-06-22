from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def nextGreater(arr,n):
    
    ngri=[-1 for i in range(n)]
    stack=[]
    for i in range(n):
        while stack and arr[stack[-1]]<arr[i]:
            ngri[stack.pop()]=i
        stack.append(i)
    ngr=[]
    for i in range(n):
        if ngri[i]!=-1:
            ngr.append(arr[ngri[i]])
        else:
            ngr.append(-1)
    return ngr
    
    
    
    
    
    
    
    
    
    
    
    
    



#Main

t = int(stdin.readline().rstrip())

while t>0:
    
    n=int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    z=(nextGreater(arr,n))
    for i in z:
        print(i,end=" ")
    print()
    
    t -= 1
