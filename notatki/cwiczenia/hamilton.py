import networkx as nx
import matplotlib.pyplot as plt


def generate_random_dag(n, p):
    random_graph = nx.fast_gnp_random_graph(n, p, directed=True)
    random_dag = nx.DiGraph([(u, v) for (u, v) in random_graph.edges() if u < v])
    A = [[] for _ in range(n)]
    for i, nbrdict in random_dag.adjacency():
        A[i] += list(nbrdict.keys())
    return random_dag, A


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

    for i in range(n):
        if not visited[i]:
            dfs_visit(G, i)

    return path


def hamilton(G):
    path = ts(G)
    print(path)
    for i in range(len(path) - 1):
        if path[i + 1] not in G[path[i]]:
            print(f"{path[i+1]} not in {G[path[i]]},{path[i]}")
            return False
    return True


G, A = generate_random_dag(5, 0.3)
print(hamilton(A))
print(list(nx.algorithms.tournament.hamiltonian_path(G)))

nx.draw_networkx(G, with_labels=True)
plt.show()
