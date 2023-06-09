from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):
    ans = 0
    for i in range(len(arr)):
        sum1  = 0
        for j in range(i,len(arr)):
            sum1 += arr[j]
            if sum1 == 0:
                if (j-i+1) > ans:
                    ans = (j-i+1)

    return ans
