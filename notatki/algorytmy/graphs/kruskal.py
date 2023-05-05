# implementation of Kruskal's algorithm
# time complexity: O(E*logV)


# adjacency list
def kruskal(G):
    n = len(G)
    # find/union structure
    parent = [x for x in range(n)]
    rank = [0 for _ in range(n)]

    def find_set(x):
        nonlocal parent
        if x != parent[x]:
            parent[x] = find_set(parent[x])
        return parent[x]

    def union(x, y):
        x = find_set(x)
        y = find_set(y)

        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    # adjacency list -> list of edges
    E = []
    for v in range(n):
        for u, d in G[v]:
            E.append((v, u, d))

    E.sort(key=lambda x: x[2])

    A = []
    for v, u, d in E:
        if find_set(v) != find_set(u):
            union(v, u)
            A.append((v, u, d))
    return A
