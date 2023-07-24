import heapq

def calculatePrimsMST(n, m, g):
    adj = [[] for _ in range(n+1)]  
    for i, j, w in g:
        adj[i].append((j, w))
        adj[j].append((i, w))
    
    ans = []
    visited = [False] * (n+1)
    pq = []  

    heapq.heappush(pq, (0, -1, 1))  

    while pq:
        weight, source, destination = heapq.heappop(pq)

        if visited[destination]:
            continue

        visited[destination] = True
        if source != -1:
            ans.append([source, destination, weight])

        for adjNode, eW in adj[destination]:
            if not visited[adjNode]:
                heapq.heappush(pq, (eW, destination, adjNode))
    
    return ans