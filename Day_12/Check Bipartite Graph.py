class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, col):
            if color[node] != -1:
                return color[node] == col
            color[node] = col
            for neighbor in graph[node]:
                if not dfs(neighbor, 1 - col):
                    return False
            return True

        vertices = len(graph)
        color = [-1] * vertices

        for i in range(vertices):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
        