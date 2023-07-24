def changeTree(root): 
    if root==None:
        return
    child=0
    if root.left!=None:
        child+=root.left.data
    if root.right!=None:
        child+=root.right.data
    if child>=root.data:
        root.data=child
    else:
        if root.left!=None:
            root.left.data=root.data
        elif root.right!=None:
            root.right.data=root.data
    changeTree(root.left)
    changeTree(root.right)
    
    #backtrack
    ans=0
    if root.left:
        ans+=root.left.data
    if root.right:
        ans+=root.right.data
    if root.left or root.right:
        root.data=ans