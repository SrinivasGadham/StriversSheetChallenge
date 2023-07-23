from os import *
from sys import *
from collections import *
from math import *

def findSpans(price):
    res = [1] * len(price)
    stack = []
    for idx, p in enumerate(price):
        while stack and p >= price[stack[-1]]:
            stack.pop()
        
        res[idx] = (idx - stack[-1]) if stack else (idx + 1)
        stack.append(idx)
    
    return res