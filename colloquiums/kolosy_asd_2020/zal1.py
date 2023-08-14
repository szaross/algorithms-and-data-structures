import heapq


# zad 1
def jak_dojade(G, P, d, a, b):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]

    distance[a] = 0
    queue = [(d, a)]

    while queue:
        tank, current = heapq.heappop(queue)
        visited[current] = True
        for v in range(n):
            if G[current][v] != -1:
                if (
                    tank >= G[current][v]
                    and distance[v] > distance[current] + G[current][v]
                ):
                    tank -= G[current][v]
                    distance[v] = distance[current] + G[current][v]
                    parent[v] = current
                    if v in P:  # binary search could be used if sorting P prior
                        tank = d
                    if not visited[v]:
                        heapq.heappush(queue, (tank, v))

    path = []
    x = b
    while parent[x] != None:
        path = [x] + path
        x = parent[x]
    if path:
        path = [a] + path

    return path if path else None


G = [
    [-1, 6, -1, 5, 2],
    [-1, -1, 1, 2, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, 4, -1, -1],
    [-1, -1, 8, -1, -1],
]
P = [0, 1, 3]
print(jak_dojade(G, P, 6, 0, 2))
