from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def getMaxWidth(root):
  if root is None:
    return 0
  q = deque()
  maxWidth = 0
  q.append(root)
  while q:
    count = len(q)
    maxWidth = max(count, maxWidth)

    while (count is not 0):
      count = count-1
      temp = q.popleft()
      if temp.left is not None:
        q.append(temp.left)

      if temp.right is not None:
        q.append(temp.right)

  return maxWidth





    