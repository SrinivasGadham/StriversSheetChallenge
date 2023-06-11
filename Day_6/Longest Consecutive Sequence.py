from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    s=set(arr)
    ans=1
    for i in arr:
        temp=i
        temp_ans=1
        if temp-1 not in s:
            while temp+1 in s:
                temp_ans+=1
                temp+=1
            ans=max(ans,temp_ans)
    return ans
            

    
