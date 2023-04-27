# "a good start" is a vertex, which we can reach every other vertex from
# adjacency list


def strongly_connected(G):
    res = []
    comp = []
    n = len(G)

    # dfs
    visited = [False for _ in range(n)]
    times = [None for _ in range(n)]
    time = 0

    def dfs_visit(G, v):
        nonlocal visited, times, time, comp

        visited[v] = True
        comp.append(v)

        for neighbour in G[v]:
            if not visited[neighbour]:
                dfs_visit(G, neighbour)
        times[v] = time
        time += 1

    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u)

    G_reversed = [[] for _ in range(n)]
    for i in range(n):
        for node in G[i]:
            G_reversed[node].append(i)

    times2 = [None for _ in range(n)]
    for i in range(n):
        times2[i] = (i, times[i])
    times2.sort(key=lambda x: x[1], reverse=True)

    # dfs on reversed digraph
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[times2[i][0]]:
            comp = []
            dfs_visit(G_reversed, times2[i][0])
            res.append(comp)

    return res


def gs(G):
    n = len(G)
    G_reversed = [[] for _ in range(n)]
    for i in range(n):
        for node in G[i]:
            G_reversed[node].append(i)
    scc = strongly_connected(G_reversed)
    return scc[-1]


G = [[6], [0, 2, 4], [3], [], [3], [1, 2], [5, 7], [6]]
print(gs(G))
