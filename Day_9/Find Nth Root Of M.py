import numpy as np
from math import ceil
from math import exp, log
def NthRoot(n: int, m: int) -> int:
    def mul(val,power):
        if power==1:
            return val
        half=mul(val,power//2)
        if power&1:
            return half*half*val
        return half*half
    def bn(n,m):
        low=1

        high=10**5
        
        while low<=high:
            mid=(low+high)//2

            if mul(mid,n)<m:
                low=mid+1
            elif mul(mid,n)>m:
                high=mid-1
            else:
                return mid
        return -1
    return bn(n,m)
    

    

    