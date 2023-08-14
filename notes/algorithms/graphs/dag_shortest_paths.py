# find shortest paths from vertex v (in a DAG)
# time complexity: O(V+E)
from graph_module import generate_random_weighted_digraph, visualize_weighted_graph


def ts_weighted(G):
    n = len(G)
    visited = [False for _ in range(n)]
    path = []

    def dfs_visit(G, v):
        nonlocal visited, path
        visited[v] = True

        for neighbour, d in G[v]:
            if not visited[neighbour]:
                dfs_visit(G, neighbour)
        path = [v] + path

    for v in range(n):
        if not visited[v]:
            dfs_visit(G, v)

    return path


# adjacency list
def spd(G, a):
    n = len(G)
    # ts sorting
    G_sorted = ts_weighted(G)
    distances = [float("inf") for _ in range(n)]
    distances[a] = 0

    # relax every vertex in topological order
    for v in G_sorted:
        for u, d in G[v]:
            if distances[u] > distances[v] + d:
                distances[u] = distances[v] + d

    return distances


n = 5
G, A = generate_random_weighted_digraph(n, 0.6)
print(spd(A, 1))
visualize_weighted_graph(G)
