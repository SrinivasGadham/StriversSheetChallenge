from os import *
from sys import *
from collections import *
from math import *

from typing import List


def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:

    d={}

    for i in range(n):

        if arr[i] not in d:

            d[arr[i]]=0

        d[arr[i]]+=1

    a = sorted(d.items(), key=lambda x:x[1],reverse=True)

    res = []

    for i in a:

        if k>0:

            res.append(i[0])

            k-=1

        else:

            break

    res.sort()

    return res