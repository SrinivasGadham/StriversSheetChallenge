

discoveryTime = 1

 

def dfs(graph, node, disc, low, inStack, nodeStack, ans):

    global discoveryTime

    disc[node] = discoveryTime

    low[node] = discoveryTime

 

    discoveryTime += 1

 

    nodeStack.append(node)

    inStack[node] = True

 

    

    for v in graph[node]:

        

        if disc[v] == -1:

            dfs(graph, v, disc, low, inStack, nodeStack, ans)

            low[node] = min(low[node], low[v])

        elif inStack[v]:

            low[node] = min(low[node], disc[v])

 

    

    if low[node] == disc[node]:

        component = []

        

        u = 0

        while nodeStack[-1] != node:

            u = nodeStack[-1]

            del nodeStack[-1]

            inStack[u] = False

 

            component.append(u)

 

        u = nodeStack[-1]

        del nodeStack[-1]

        inStack[u] = False

 

        component.append(u)

        ans.append(component)

 

def stronglyConnectedComponents(n, edges):

    

    graph = [[] for i in range(n)]

 

    for edge in edges:

        graph[edge[0]].append(edge[1])

 

    

    disc = [-1] * n

    low = [-1] * n

 

    nodeStack = []

    inStack = [False] * n

 

    ans = []

    for i in range(n):

        if disc[i] == -1:

            

            dfs(graph, i, disc, low, inStack, nodeStack, ans)

 

    return ans

 