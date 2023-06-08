from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    n=len(intervals)
    l=[]
    for i in range(n):
        temp=[]
        temp.append(intervals[i].start)
        temp.append(intervals[i].end)
        l.append(temp)
    
    l.sort(key=lambda x:x[0])
    
    res1=[]
    old_start,old_end=l[0][0],l[0][1]
    i=1
    new_end=float('-inf')
    while(i<n):
        new_start,new_end=l[i][0],l[i][1]
        if new_start>old_end:
            res1.append((old_start,old_end))
            old_start,old_end=new_start,new_end
            old_end=max(old_end,new_end)
        else:
            old_end=max(old_end,new_end)
        i+=1
    res1.append((old_start,max(old_end,new_end)))
    return res1

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(*res[i])
