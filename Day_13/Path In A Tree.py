from os import *
from sys import *
from collections import *
from math import *

from typing import List


class TreeNode:   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pathInATree(root: TreeNode, x: int) -> List[int]:
    def path(node,arr,target):
        if node==None:
            return False
        arr.append(node.data)
        if node.data==target:
            return True
        
        if path(node.left,arr,target) or path(node.right,arr,target):
            return True
        arr.pop()
        return False
    arr=[]
    path(root,arr,x)
    return arr
    


    