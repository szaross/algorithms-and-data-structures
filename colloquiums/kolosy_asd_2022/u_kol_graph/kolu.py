from kolutesty import runtests


def ts(G, disk):
    n = len(G)
    visited = [False for _ in range(n)]
    path = []

    def dfs_visit(G, v):
        nonlocal visited, path, disk
        visited[v] = True

        if disk[v] == "B":
            for neighbour in G[v]:
                if not visited[neighbour]:
                    dfs_visit(G, neighbour)
            path = [v] + path

        if disk[v] == "A":
            for i in range(len(G[v]) - 1, -1, -1):
                neighbour = G[v][i]
                if not visited[neighbour]:
                    dfs_visit(G, neighbour)
            path = [v] + path

    for v in range(n):
        if not visited[v]:
            dfs_visit(G, v)

    return path


def swaps(disk, depends):
    n = len(depends)
    G = [[] for _ in range(n)]
    for v in range(n):
        for u in depends[v]:
            G[u].append(v)

    for i in range(n):
        G[i].sort(key=lambda x: disk[x])

    path = ts(G, disk)
    count = 0
    prev = disk[path[0]]

    for i in range(1, len(path)):
        if disk[path[i]] != prev:
            count += 1
            prev = disk[path[i]]
    return count


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(swaps, all_tests=True)

# disk = ["A", "A", "B", "B"]
# depends = [[2, 3], [], [1, 3], [1]]
# print(swaps(disk, depends))
