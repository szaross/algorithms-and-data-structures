# count the total number of paths from a to b in a dag
# time complexity: O(V + E)
from graph_module import generate_random_dag, visualize_graph


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


def nop(G, a, b):
    n = len(G)
    G_sorted = ts(G)
    # store the number of paths to b from i-th vertex
    number = [0 for _ in range(n)]
    number[b] = 1

    for v in range(n - 1, -1, -1):
        tmp = 0
        for u in G[v]:
            tmp += number[u]
        number[v] += tmp
    return number[a]


n = 6
G, A = generate_random_dag(n, 0.6)
print(nop(A, 0, 4))
visualize_graph(G)
