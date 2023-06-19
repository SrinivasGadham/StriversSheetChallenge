from collections import defaultdict
def detectCycleInDirectedGraph(n, edges):
    def dfs(p,pathvisited):
        if p in visited and p in pathvisited:
            return 1
        visited.add(p)
        pathvisited.add(p)
        for x in graph[p]:
            if dfs(x,pathvisited):
                return 1
        pathvisited.remove(p)
        return 0
        
    graph=defaultdict(list)
    for n1,n2 in edges:
        graph[n1].append(n2)
        
    visited=set()
    for i in range(1,n+1):
        if i not in visited:
            if dfs(i,set()):
                return True
    return False


    