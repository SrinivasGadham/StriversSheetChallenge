from os import *
from sys import *
from collections import *
from math import *

'''
    ------- Binary Tree node structure -------
            class   BinaryTreeNode :
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

def predecessorSuccessor(root, key):
    global pred, succ
    if root:
        
        pred = None
        succ = None

        
        findPredecessorSuccessor(root, key)

        
        if pred==None:
            a=-1
        else:
            a=pred.data
        if succ==None:
            b=-1
        else:
            b=succ.data
        return a,b

def findPredecessorSuccessor(node, key):
    global pred, succ
    if node is None:
        return

    
    if node.data == key:
        
        if node.left:
            temp = node.left
            while temp.right:
                temp = temp.right
            pred = temp

        
        if node.right:
            temp = node.right
            while temp.left:
                temp = temp.left
            succ = temp

        return

    
    if key < node.data:
        succ = node
        findPredecessorSuccessor(node.left, key)
    
    else:
        pred = node
        findPredecessorSuccessor(node.right, key)
