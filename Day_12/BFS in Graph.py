from os import *
from sys import *
from collections import *
from math import *

from collections import defaultdict
from queue import Queue
def BFS(vertex, edges):
    # print(vertex,edges)
    def bfs(root,l):
        q=Queue()
        visited.add(root)
        q.put(root)
        while q.qsize():
            node=q.get()
            for adj in graph[node]:
                if adj not in visited:
                    q.put(adj)
                    visited.add(adj)
            l.append(node)
        return sorted(l)
    graph=defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    visited=set()
    res=[]
    for i in range(vertex):
        if i not in visited:
            res.append(bfs(i,[]))
    res.sort(key=lambda x:x[0])
    return res