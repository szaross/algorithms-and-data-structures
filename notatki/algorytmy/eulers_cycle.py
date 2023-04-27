from collections import deque


# adjacency list
def dfs(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    path = []
    res = deque()
    last_considered = [-1 for _ in range(n)]
    times = [-1 for _ in range(n)]
    time = 0
    stack = []

    def dfs_visit(G, v):
        nonlocal visited, parent, path, last_considered

        if not visited[v]:
            for i in range(last_considered[v] + 1, len(G[v])):
                neighbour = G[v][i]
                if (v, neighbour) not in path and (neighbour, v) not in path:
                    parent[neighbour] = v
                    path.append((v, neighbour))
                    last_considered[v] = i
                    dfs_visit(G, neighbour)
            res.append(v)
            visited[v] = True

    for v in range(n):
        dfs_visit(G, v)

    return res


# G = [[1, 2], [0, 3], [0, 3], [1, 2, 4, 5], [3, 5], [3, 4]]
G = [
    [1, 2],
    [0, 3, 2, 4, 5, 6],
    [0, 3, 6, 1, 4, 5],
    [1, 2, 4, 5],
    [3, 5, 1, 2],
    [3, 4, 1, 2],
    [1, 2],
]
print(dfs(G))

