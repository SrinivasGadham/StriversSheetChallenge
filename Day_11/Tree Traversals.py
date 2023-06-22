from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
def inorder(root,ino):
    if root==None:
        return
    inorder(root.left,ino)
    ino.append(root.data)
    inorder(root.right,ino)
def preorder(root,pre):
    if root==None:
        return
    pre.append(root.data)
    preorder(root.left,pre)
    preorder(root.right,pre)
def postorder(root,post):
    if root==None:
        return
    postorder(root.left,post)
    postorder(root.right,post)
    post.append(root.data)
    


def getTreeTraversal(root):
    if root==None:
        return []
    ino=[]
    pre=[]
    post=[]
    inorder(root,ino)
    preorder(root,pre)
    postorder(root,post)

    res=[]
    res.append(ino)
    res.append(pre)
    res.append(post)
    # print(res)
    return res
