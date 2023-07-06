from os import *
from sys import *
from collections import *
from math import *

# Binary Tree node structure
class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right


def LCAinaBST(root, p, q):
    if root==None:
        return None
    curr=root.data
    if curr<p.data and curr<q.data:
        return LCAinaBST(root.right,p,q)
        
    if curr>p.data and curr>q.data:
        return LCAinaBST(root.left,p,q)
    return root