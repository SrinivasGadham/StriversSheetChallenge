from os import *
from sys import *
from collections import *
from math import *

def jobScheduling(jobs):

    jobs=sorted(jobs,key= lambda x : x[1],reverse = True )
    max_profit=0
    max_time=max(jobs,key= lambda x :x[0])
    slots=[-1]*max_time[0]
    for job in jobs:
        for j in range(job[0],0,-1):
            if slots[j-1]==-1:
                slots[j-1]=job[1]
                max_profit+=job[1]
                break
    return max_profit