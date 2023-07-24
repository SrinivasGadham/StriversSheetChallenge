def getPath(root,leaf,stack):

 

    if root is None:

        return False

 

    if root.data==leaf:

        stack.append(root)

        return True

 

    stack.append(root)

    

    if (root.left and getPath(root.left,leaf,stack)) or (root.right and getPath(root.right,leaf,stack)):

        return True

 

    stack.pop()

    return False

 

 

def invertBinaryTree(root, leaf):

    

    if root is None:

        return None

 

    stack=[]

    getPath(root,leaf,stack)

    new_root=parent=stack.pop()

    

    while stack:

        curr_node=stack.pop()

        if curr_node.left==parent:

            curr_node.left=None

            parent.left=curr_node

        else:

            curr_node.right=curr_node.left

            curr_node.left=None

            parent.left=curr_node

        parent=parent.left

 

    return new_root