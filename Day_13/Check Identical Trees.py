from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree Node class structure
class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
              
        
def identicalTrees(root1, root2):
    if root1==None and root2==None:
        return True
    if root1==None or root2==None:
        return False
    if root1.data!=root2.data:
        return False
    return identicalTrees(root1.left,root2.left) and identicalTrees(root1.right,root2.right)

    