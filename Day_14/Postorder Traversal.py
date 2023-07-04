from os import *
from sys import *
from collections import *
from math import *

def postorder(root,ans):
    if root:
        postorder(root.left,ans)
        postorder(root.right,ans)
        ans.append(root.data)
def getPostOrderTraversal(root):
    # Write your code here.
    ans=[]
    postorder(root,ans)
    return ans
