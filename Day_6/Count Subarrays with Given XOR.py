
from collections import *


def subarraysXor(arr, x):
    n=len(arr)
    prefix_xor=[0 for i in range(len(arr))]
    prefix_xor[0]=arr[0]
    for i in range(1,n):
        prefix_xor[i]=prefix_xor[i-1]^arr[i]
    mp=defaultdict(int)
    ans=0
    # print(prefix_xor)
    for i in range(n):
        temp=x^prefix_xor[i]
        if temp in mp:
            ans+=mp[temp]
        if temp==0:
            ans+=1
        mp[prefix_xor[i]]+=1
    return ans





    