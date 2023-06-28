from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''


def isBalancedBT(root):
  def dfs(root):
    if root==None:
      return [True,0]
    left,right=dfs(root.left),dfs(root.right)
    balanced=left[0] and right[0] and abs(left[1]-right[1])<=1
    return [balanced,1+max(left[1],right[1])]
  return dfs(root)[0]

