from os import *
from sys import *
from collections import *
from math import *
import heapq
def dijkstra(vec, vertices, edges, source):
    # print(vec)
    # print(vertices)
    # print(edges)
    #print(source)
    graph=defaultdict(list)
    for a,b,w in vec:
        graph[a].append((b,w))
        graph[b].append((a,w))
    dist=[2147483647 for i in range(vertices)]
    # parent=[-1 for i in range(vertices)]
    dist[source]=0
    heap=[[0,source]]
    heapq.heapify(heap)
    while len(heap)!=0:
        weight,v=heapq.heappop(heap)
        for child,child_weight in graph[v]:
            if dist[child]>=dist[v]+child_weight:
                dist[child]=dist[v]+child_weight
                heapq.heappush(heap,[dist[child],child])
                # parent[child]=v
    


    # print(dist)
    # print(parent)
    return dist

    