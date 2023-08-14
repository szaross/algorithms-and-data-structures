from egzP3btesty import runtests
from queue import PriorityQueue


def lufthansa(G):
    n = len(G)

    # find/union implementation
    rank = [0 for _ in range(n)]
    parent = [x for x in range(n)]

    def findset(x):
        nonlocal parent
        if parent[x] != x:
            parent[x] = findset(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal rank, parent
        x = findset(x)
        y = findset(y)

        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y

            if rank[x] == rank[y]:
                rank[y] += 1

    # create edge list
    E = []
    for v in range(n):
        for u, d in G[v]:
            if u < v:
                E.append((v, u, d))
    E.sort(reverse=True, key=lambda x: x[2])

    A = set()
    found = False
    for v, u, d in E:
        if findset(v) != findset(u):
            union(v, u)
            A.add((v, u, d))
        elif not found:
            A.add((v, u, d))
            found = True

    res = 0
    for v, u, d in E:
        if (v, u, d) not in A:
            res += d

    return res


runtests(lufthansa, all_tests=True)


# G = [
#     [(1, 15), (2, 5), (3, 10)],
#     [(0, 15), (2, 8), (4, 5), (5, 12)],
#     [(0, 5), (1, 8), (3, 5), (4, 6)],
#     [(0, 10), (2, 5), (4, 2), (5, 11)],
#     [(1, 5), (2, 6), (3, 2), (5, 2)],
#     [(1, 12), (4, 2), (3, 11)],
# ]
# print(lufthansa(G))
