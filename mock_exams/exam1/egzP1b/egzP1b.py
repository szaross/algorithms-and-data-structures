from egzP1btesty import runtests
import heapq


def dijkstra(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [float("inf") for _ in range(n)]

    distance[s] = 0
    queue = [(0, 0, s)]

    while queue:
        w1, counter, current = heapq.heappop(queue)
        visited[current] = True
        if counter > 3:
            continue
        for neighbour, w2 in G[current]:
            if neighbour == t and counter == 3:
                distance[neighbour] = w1 + w2
                return distance[neighbour]
            if distance[neighbour] > w1 + w2 and neighbour != t:
                distance[neighbour] = w1 + w2
                if not visited[neighbour]:
                    heapq.heappush(queue, (w1 + w2, counter + 1, neighbour))

    return distance[t]


def turysta(G, D, L):
    E = set()
    for u, v, p in G:
        if u not in E:
            E.add(u)
        if v not in E:
            E.add(v)
    n = max(E)
    AL = [[] for _ in range(n + 1)]
    for u, v, p in G:
        AL[u].append((v, p))
        AL[v].append((u, p))

    res = dijkstra(AL, D, L)

    return res


runtests(turysta)


# G = [
#     (0, 1, 9),
#     (0, 2, 1),
#     (1, 2, 2),
#     (1, 3, 8),
#     (1, 4, 3),
#     (2, 4, 7),
#     (2, 5, 1),
#     (3, 4, 7),
#     (4, 5, 6),
#     (3, 6, 8),
#     (4, 6, 1),
#     (5, 6, 1),
# ]
# D = 0
# L = 6
# print(turysta(G, D, L))
