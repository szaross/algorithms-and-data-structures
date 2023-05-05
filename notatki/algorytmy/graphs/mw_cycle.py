# find a minimal weight cycle in a diracted graph
# time complexity: O(n^3)

from graph_module import generate_random_weighted_digraph, visualize_weighted_graph


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


def mwc(G):
    n = len(G)
    W = fw(G)

    mc = float("inf")
    cycle = []
    for v in range(n):
        for u in range(n):
            if W[v][u] + W[u][v] < mc:
                cycle = [u, v]
                mc = W[v][u] + W[u][v]
    return mc, cycle


n = 4
G, A = generate_random_weighted_digraph(n, 0.4)
print(mwc(A))
visualize_weighted_graph(G)
