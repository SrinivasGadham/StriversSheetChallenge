from os import *
from sys import *
from collections import *
from math import *
'''
   ------- Binary Tree node structure -------
           class TreeNode :
               def __init__(self, data) :
                   self.data = data
                   self.left = None
                   self.right = None
'''
def fun(root):
   if root == None:
       return 0, float('-inf'), float('inf')
   
   l_tree = fun(root.left)
   r_tree = fun(root.right)
   
   
   
   
   if l_tree[1] < root.data < r_tree[2]:
       
       
       
       count = 1 + l_tree[0] + r_tree[0]
       lar = max(l_tree[1], r_tree[1], root.data)
       sma = min(l_tree[2], r_tree[2], root.data)
       
   
   else:
       count = max(l_tree[0], r_tree[0])
       lar = float('inf')
       sma = float('-inf')
       
   return count, lar, sma
def largestBST(root):

   out = fun(root)
   return out[0]