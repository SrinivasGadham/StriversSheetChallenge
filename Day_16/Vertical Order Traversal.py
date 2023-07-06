from collections import defaultdict







def verticalOrderTraversal(root):
    if root is None:
        return []

    
    vertical_levels = defaultdict(list)

    
    queue = [(root, 0)]  

    while queue:
        node, distance = queue.pop(0)

        
        vertical_levels[distance].append(node.data)

        
        if node.left:
            queue.append((node.left, distance - 1))

        
        if node.right:
            queue.append((node.right, distance + 1))

    
    vertical_order = [vertical_levels[key] for key in sorted(vertical_levels.keys())]
    res=[]
    for i in vertical_order:
        for j in i:
            res.append(j)
    return res
