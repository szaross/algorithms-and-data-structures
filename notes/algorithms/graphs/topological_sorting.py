# a topological sorting algorithm
from graph_module import generate_random_dag, visualize_graph
from networkx import topological_sort


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


G, A = generate_random_dag(5, 0.6)
print(ts(A))
print(list(topological_sort(G)))
visualize_graph(G)
