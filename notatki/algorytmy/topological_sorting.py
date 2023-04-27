import networkx as nx
import matplotlib.pyplot as plt


# adjacency list
def ts(G):
    n = len(G)
    visited = [False for _ in range(n)]
    path = []

    def dfs_visit(G, v):
        nonlocal visited, path
        visited[v] = True

        for neighbour in G[v]:
            if not visited[neighbour]:
                dfs_visit(G, neighbour)
        path = [v] + path

    for v in range(n):
        if not visited[v]:
            dfs_visit(G, v)

    return path


# print(dfs(A))
# generate random dag in adjacency list
def generate_random_dag(n, p):
    random_graph = nx.fast_gnp_random_graph(n, p, directed=True)
    random_dag = nx.DiGraph([(u, v) for (u, v) in random_graph.edges() if u < v])
    A = [[] for _ in range(n)]
    for i, nbrdict in random_dag.adjacency():
        A[i] += list(nbrdict.keys())
    return random_dag, A


G, A = generate_random_dag(5, 0.6)
print(ts(A))
print(list(nx.topological_sort(G)))

nx.draw_networkx(G, with_labels=True)
plt.show()