def inorder(root,ans):

    if root:

       inorder(root.left,ans)

       ans.append(root.data)

       inorder(root.right,ans)

 

def getInOrderTraversal(root):

    # Write your code here.

    ans=[]

    inorder(root,ans)

    return ans