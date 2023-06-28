# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameterOfBinaryTree(root):
    if root==None:
        return 0
    def diameter(node,maxi):
        if node == None:
            return [0,maxi]
        lh,maxi=diameter(node.left,maxi)
        rh,maxi=diameter(node.right,maxi)
        maxi=max(maxi,lh+rh)
        return [1 + max(lh,rh),maxi]
    maxi=float('-inf')
    return diameter(root,maxi)[1]
    # return maxi