from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def maxSubarraySum(arr, n):
    max_sub = [-1 for i in range(n)]
    max_sub[0] = arr[0]
    for i in range(1, n):
        max_sub[i] = (max(max_sub[i-1]+arr[i], arr[i]))
    if max(max_sub) < 0:
        return 0
    return max(max_sub)

    # Your code here
    # return the answer
    # return


# taking inpit using fast I/O
def takeInput():

    n = int(input())

    if (n == 0):
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


# main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
