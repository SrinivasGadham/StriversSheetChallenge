from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the Binary Tree node structure:

	class BinaryTreeNode :
	    def __init__(self, data) :
	        self.data = data
	        self.left = None
	        self.right = None

'''

def searchInBST(root, x):
    curr=root
    while curr:
        if curr.data==x:
            return True
        elif curr.data>x:
            curr=curr.left
        else:
            curr=curr.right
    return False