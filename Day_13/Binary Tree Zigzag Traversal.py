from os import *
from sys import *
from collections import *
from math import *

# BinaryTreeNode class definition
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
import queue
def zigZagTraversal(root):
    if not root:
        return []
    ans=[]
    que=queue.Queue()
    que.put(root)
    x=1
    while que.qsize():
        n=que.qsize()
        l=[]
        while(n):
            node=que.get()
            l.append(node.data)
            if node.left:
                que.put(node.left)
            if node.right:
                que.put(node.right)
            n-=1
        if x&1:
            ans.append(l)
        else:
            ans.append(l[::-1])
        x+=1
    res=[]
    for i in ans:
        for j in i:
            res.append(j)
    return res
    