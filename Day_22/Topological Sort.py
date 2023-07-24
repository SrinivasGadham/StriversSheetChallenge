from os import *
from sys import *
from collections import *
from math import *

def dfs(node, graph, visited, stack):
    
    visited[node] = True
    for adjNode in graph[node]:
        if not visited[adjNode]:
            dfs(adjNode, graph, visited, stack)
    stack.append(node)

def bfs(graph,in_degree,v):
    queue = deque()

    
    for i in range(v):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        
        
        for adjNode in graph[node]:
            in_degree[adjNode] -= 1
            if in_degree[adjNode] == 0:
                queue.append(adjNode)

    return result


def topologicalSort(adj, v, e):
    
    graph = [[] for _ in range(v)]
    in_degree = [0] * v  
    for i in range(e):
        u, v = adj[i]
        graph[u].append(v)
        in_degree[v] += 1
    
    
    v = len(graph)

    visited = [False] * v
    stack = []

    
    for i in range(v):
        if not visited[i]:
            dfs(i, graph, visited, stack)

    
    res = stack[::-1]

    
    res = bfs(graph,in_degree,v)

    return res