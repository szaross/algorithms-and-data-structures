from zad4testy import runtests
def bfs_len(g, s, d, k):
    n = len(g)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    length = [0 for _ in range(n)]
    q = [g[s]]
    visited[s] = True
    parent[s] = -1
    while len(q) != 0:
        u = q[0]
        q.pop(0)
        for v in u:
            if not visited[v]:
                parent[v] = g.index(u)
                if v != k[0] or parent[v] != k[1]:
                    visited[v] = True
                    length[v] = length[parent[v]] + 1
                    q.append(g[v])
                    if v == d:
                        return length[v]
    return -1


def bfs_path(g, s, d):
    n = len(g)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    length = [0 for _ in range(n)]
    q = [g[s]]
    visited[s] = True
    parent[s] = -1
    l = 0
    while len(q) != 0:
        u = q[0]
        q.pop(0)
        for v in u:
            flag = False
            if not visited[v]:
                visited[v] = True
                parent[v] = g.index(u)
                length[v] = length[parent[v]] + 1
                q.append(g[v])
                if v == d:
                    l = length[v]
                    flag = True
                    break
        if flag:
            break
    if flag:
        w = d
        path = []
        for i in range(l + 1):
            path.append(w)
            w = parent[w]

        return path
    else:
        return None


def longer(G, s, t):
    starting_path = bfs_path(G, s, t)
    if starting_path == None:
        return None
    starting_len = len(starting_path) - 1
    for i in range(starting_len, 0, -1):
        k = (starting_path[i - 1], starting_path[i])
        new_path = bfs_len(G, s, t, k)
        if new_path > starting_len or new_path == -1:
            return k

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)