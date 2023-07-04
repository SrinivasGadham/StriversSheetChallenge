from os import *
from sys import *
from collections import *
from math import *

def getPreOrderTraversal(root):
    if root is None:
        return []

    
    result = []
    result.append(root.data)  
    result.extend(getPreOrderTraversal(root.left))  
    result.extend(getPreOrderTraversal(root.right))  

    return result
