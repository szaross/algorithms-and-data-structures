import networkx as nx
import matplotlib.pyplot as plt


def generate_random_digraph(n, p):
    random_graph = nx.fast_gnp_random_graph(n, p, directed=True)
    # random_dag = nx.DiGraph([(u, v) for (u, v) in random_graph.edges() if u < v])
    A = [[] for _ in range(n)]
    for i, nbrdict in random_graph.adjacency():
        A[i] += list(nbrdict.keys())
    return random_graph, A


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


# [[0, 2, 1], [3, 4, 5, 6], [7, 10, 8, 9]] for G1:
# G1 = [[1], [2], [0, 6], [6], [3, 10], [4, 8], [5], [8], [10], [8], [7, 9]]

G, A = generate_random_digraph(5, 0.4)

print(strongly_connected(G))
print(list(nx.strongly_connected_components(G)))

nx.draw_networkx(G, with_labels=True)
plt.show()
