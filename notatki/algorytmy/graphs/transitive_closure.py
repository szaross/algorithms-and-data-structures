# find the transitive closure of a directed graph G
# time complexity: O(n^3)

from graph_module import generate_random_weighted_digraph, visualize_weighted_graph


# adjacency list
def tc(G):
    n = len(G)
    W = [[float("inf") for _ in range(n)] for _ in range(n)]

    for v in range(n):
        for u, d in G[v]:
            W[v][u] = d

    # Floyd-Warshall
    for t in range(n):
        for x in range(n):
            for y in range(n):
                W[x][y] = min(W[x][y], W[x][t] + W[t][y])

    for i in range(n):
        for j in range(n):
            W[i][j] = 0 if W[i][j] == float("inf") else 1

    return W
    # W: returned graph in matrix representation


n = 4
G, A = generate_random_weighted_digraph(n, 0.5)
print(tc(A))
visualize_weighted_graph(G)
