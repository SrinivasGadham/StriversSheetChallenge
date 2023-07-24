def floydWarshall(n, m, src, dest, edges):
    
    adj = [[0] * n for _ in range(n)]
    for x in edges:
        u, v, w = x
        adj[u - 1][v - 1] = w

    
    for i in range(n):
        for j in range(n):
            if adj[i][j] == 0 and i != j:
                adj[i][j] = float('inf')

    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj[i][k] == float('inf') or adj[k][j] == float('inf'):
                    continue
                adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

    
    return int(1e9) if adj[src - 1][dest - 1] == float('inf') else adj[src - 1][dest - 1]