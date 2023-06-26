from typing import *

from collections import defaultdict
def depthFirstSearch(V: int, E: int, edges: List[Tuple[int, int]]):
    def dfs(root,l):
        if root in visited:
            return
        visited.add(root)
        l.append(root)
        for adj in graph[root]:
            dfs(adj,l)
        return sorted(l)
        
    graph=defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    visited=set()
    res=[]
    for i in range(V):
        if i not in visited:
            res.append(dfs(i,[]))
    # print(res)
    res.sort(key=lambda x:x[0])
    return res



    
