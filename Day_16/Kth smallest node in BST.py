from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure
   
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

'''
def kthSmallest(root, k):
    def inorder(root):
        if root is None:
            return []
        return inorder(root.left) + [root.data]  + inorder(root.right)
        
    ans = inorder(root)
    return ans[k-1]


    