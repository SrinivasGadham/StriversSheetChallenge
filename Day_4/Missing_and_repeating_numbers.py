from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    total_sum=sum(arr)
    sum_need_to_be=(n*(n+1))//2
    arr=set(arr)
    for i in range(1,n+1):
        if i not in arr:
            missing_number=i
            break
    return missing_number,total_sum-(sum_need_to_be-missing_number)

