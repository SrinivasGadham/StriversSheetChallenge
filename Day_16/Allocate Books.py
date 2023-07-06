from os import *
from sys import *
from collections import *
from math import *

def ayushGivesNinjatest(n, m, time):
    def check(val):
        count=0
        sum=0
        for i in range(m):
            if time[i]>val:
                return False
            elif sum+time[i]>val:
                sum=time[i]
                count+=1
            else:
                sum+=time[i]
        if sum>val:
            return False
        elif sum<=val:
            count+=1
        if count>n:
            return False

        else:
            return True
    ans=float('inf')
    low=0
    high=int(1e20)
    while low<=high:
        mid=(low+high)//2
        if check(mid):
            ans=min(ans,mid)
            high=mid-1
        else:
            low=mid+1
    return ans
        





    