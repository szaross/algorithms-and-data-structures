# find the shortest path calculated as a product of weight
# time complexity: O(E + V*E)
from math import log, exp
from graph_module import generate_random_weighted_digraph, visualize_weighted_graph


# adjacency list
def bf(G, a, b):
    n = len(G)
    distances = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    distances[a] = 0

    # recalculate weight as log(weight)
    for v in range(n):
        for i in range(len(G[v])):
            G[v][i] = (G[v][i][0], log(G[v][i][1]))

    # relax
    for v in range(n):
        for u, d in G[v]:
            if distances[u] > distances[v] + d:
                distances[u] = distances[v] + d
                parent[u] = v

    # find negative cycles
    for v in range(n):
        for u, d in G[v]:
            if distances[u] != float("inf") and distances[u] > distances[v] + d:
                return "A negative cycle has been found"

    path = [b]
    s = b
    while parent[s] != None:
        path = [parent[s]] + path
        s = parent[s]

    res = round(exp(distances[b])), path if distances[b] != float("inf") else float(
        "inf"
    )

    return res


G, A = generate_random_weighted_digraph(5, 0.6)
a = 0
b = 3
print(bf(A, a, b))
visualize_weighted_graph(G)
