from os import *
from sys import *
from collections import *
from math import *
import bisect
def reversePairs(A, n):
    status, res = [], 0
    for a in A:
        res += len(status) - bisect.bisect_right(status, a)
        bisect.insort(status, a/2)
    return res