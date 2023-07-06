from os import *
from sys import *
import collections
from math import *

from typing import *

  
def uniqueSubsets(n :int,A :List[int]) -> List[List[int]]:
    #
    key = lambda Q,x: tuple(sorted( list(Q) + [x] ))
    #
    B   = set()
    #
    for x in A:
        B |= { key(Q,x) for Q in B }
        B |= { (x,) }
    return  list(map(list,B)) + [[]]
    
