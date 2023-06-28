from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def getTopView(root):
    def dfs(node,i,level):
        if node==None:
            return []
        d[i].append([node.val,i,level])
        dfs(node.left,i-1,level+1)
        dfs(node.right,i+1,level+1)
    d=defaultdict(list)
    dfs(root,0,0)
    temp=list(d.keys())
    temp.sort()
    res=[]
    for i in temp:
        d[i].sort(key=lambda x:x[2])
        res.append(d[i][0][0])
    return res


# Taking input.
def takeInput():

    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1):
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()

        leftChild = arr[index]

        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1
        rightChild = arr[index]

        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)

        index += 1

    return root

# Printing the tree nodes.
def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()


# Main.
T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = getTopView(root)
    printAns(ans)