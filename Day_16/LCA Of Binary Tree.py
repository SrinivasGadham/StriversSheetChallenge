

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowestCommonAncestor(root, x, y):
    if root==None:
        return -1
    if root.data==x or root.data==y:
        return root.data
    left=lowestCommonAncestor(root.left,x,y)
    right=lowestCommonAncestor(root.right,x,y)
    
    if left==-1:
        return right
    elif right==-1:
        return left
    else:         
        return root.data