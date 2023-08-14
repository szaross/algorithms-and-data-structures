# Floyd-Warshall algorithm for directed graph
# time complexity: O(n^3)
from graph_module import generate_random_weighted_digraph, visualize_weighted_graph


# adjacency list
def fw(G):
    n = len(G)
    # adjacency list -> matrix representation
    M = [[0 for _ in range(n)] for _ in range(n)]
    W = [[float("inf") for _ in range(n)] for _ in range(n)]
    for v in range(n):
        for u, d in G[v]:
            M[v][u] = 1
            W[v][u] = d

    # F-W
    for t in range(n):
        for v in range(n):
            for u in range(n):
                W[v][u] = min(W[v][u], W[v][t] + W[t][u])

    return W


n = 6
G, A = generate_random_weighted_digraph(n, 0.3)
print(*fw(A))
visualize_weighted_graph(G)
