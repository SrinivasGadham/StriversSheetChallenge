
from collections import *


def findDuplicate(arr:list, n:int):
    d=Counter(arr)
    for i in d.keys():
        if d[i]>1:
            return i
    