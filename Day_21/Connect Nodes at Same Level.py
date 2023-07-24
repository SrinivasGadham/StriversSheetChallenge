from os import *

from sys import *

from collections import *

from math import *

 

'''

    ----------------- Binary Tree node class for reference -----------------

    

    class BinaryTreeNode:

        def __init__(self, data):

            self.data = data

            self.left = None

            self.right = None

            self.next = None

'''

 

def connectNodes(root):

    

    if not root:

        return None

        

    

    queue = deque([root])

        

    

    while queue:

        size = len(queue) 

        for i in range(size):

            node = queue.popleft() 

                

            

            if i < size-1:

                node.next = queue[0] 

                    

            if node.left:

                queue.append(node.left) 

            if node.right:

                queue.append(node.right)           

                

    return root