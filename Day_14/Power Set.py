from os import *
from sys import *
from collections import *
from math import *
def helper2(idx,temp,v,res):
    if idx == len(v):
        res.append(temp.copy())
        return
    
    helper2(idx+1,temp,v,res) # take
    helper2(idx+1,temp+[v[idx]],v,res) # dont take

def pwset(v):
    res = []
    helper2(0,[],v,res)
    return res