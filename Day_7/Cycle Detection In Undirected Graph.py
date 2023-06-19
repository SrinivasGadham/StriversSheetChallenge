from collections import defaultdict
def cycleDetection(edges, n, m):
    def dfs(root,parent):
        if root in visited:
            return 1
        
        visited.add(root)
        for i in graph[root]:
            if i!=parent:
                if dfs(i,root):
                    return 1
        return 0
            
    graph = defaultdict(list)
    for n1,n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)
    visited=set()
   
    for i in range(1,n+1):
        if i not in visited:
            if dfs(i,-1):
                return "Yes"
    return "No"



    