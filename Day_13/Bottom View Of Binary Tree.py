from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
import queue
import sys
from collections import OrderedDict
setrecursionlimit(10**6)


# Following is the structure used to represent the Binary Tree Node.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

	
def bottomView(root):
    # Write your code here.
    # This function returns a list of nodes which is the required bottom view of the tree.
    ans=[]
    dic={}
    nodelvl=[(root,0)]
    if root==None:
        return ans

    while nodelvl:
        
        node,lvl=nodelvl.pop(0)
        dic[lvl]=node.data
        if node.left:
            nodelvl.append((node.left,lvl-1))
        if node.right:
            nodelvl.append((node.right,lvl+1))
    for i in sorted(dic.keys()):
        ans.append(dic[i])
    return ans

        
    


# Taking level-order input using fast I/O method.
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main.
t = int(input())
while t:
    root = takeInput()
    answer = bottomView(root)
    
    print(*answer)
    t = t - 1
