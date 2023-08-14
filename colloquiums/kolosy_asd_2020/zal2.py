import heapq


def dijkstra(G, W, L, s):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [float("inf") for _ in range(n)]
    t = s
    distance[s] = 0
    # counter = 0
    queue = [(0, 1, s)]
    flag = False
    while queue and not flag:
        d, counter, current = heapq.heappop(queue)
        if counter == len(W):
            flag = True
            t = current
            break
        visited[current] = True
        for neighbour, w in G[current]:
            if W[counter] == L[neighbour]:
                if distance[neighbour] > distance[current] + w:
                    distance[neighbour] = distance[current] + w
                    parent[neighbour] = current
                    if not visited[neighbour]:
                        heapq.heappush(
                            queue, (distance[neighbour], counter + 1, neighbour)
                        )

    path = []
    x = t
    while parent[x] != None:
        path = [x] + path
        x = parent[x]
    if path:
        path = [s] + path

    return distance[t], path


def letters(G, W):
    E = G[1]
    L = G[0]
    n = len(L)
    # list of edges->adjacency list
    AL = [[] for _ in range(n)]

    for u, v, w in E:
        AL[u].append((v, w))
        AL[v].append((u, w))

    L2 = [(L[i], i) for i in range(n)]
    L2.sort(key=lambda x: x[1])

    s = [y[0] for y in L2].index(W[0])

    res, path = dijkstra(AL, W, L, s)

    for i in range(s + 1, n):
        if L2[i][0] != W[0]:
            break

        tmp = dijkstra(AL, W, L, i)

        if tmp[0] < res:
            res, path = tmp

    return res, path


L = ["k", "k", "o", "o", "t", "t"]
E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
G = (L, E)
W = "kot"
print(letters(G, W))
