'''

    Following is the representation for the Binary Tree Node:

    class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
'''

def isSymmetric(root) :
    if root is None:
        return True
    return issymmtrichelp(root.left,root.right)
def issymmtrichelp(rootleft,rootright):
    if rootleft==None or rootright==None:
        return rootleft==rootright
    if rootleft.data!=rootright.data:
        return False
    return issymmtrichelp(rootleft.left,rootright.right) and issymmtrichelp(rootleft.right,rootright.left)