# find a path from a to b with the smallest sum of weights having walked through only decreasing weights
# time complexity: O(E*log(E) + E)
from graph_module import generate_random_weighted_digraph, visualize_weighted_graph


# adjacency list
def decreasing_path(G, a, b):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    distance[a] = 0
    parent = [None for _ in range(n)]

    # convert adjacency list into a list of edges
    G1 = []
    for v in range(n):
        for u, d in G[v]:
            G1.append((v, u, d))

    # sort the list of edges in decreasing order
    G1.sort(key=lambda x: x[2], reverse=True)

    # relax edges in that order
    for v, u, d in G1:
        if distance[u] > distance[v] + d:
            distance[u] = distance[v] + d
            parent[u] = v

    # get the path
    path = [b]
    s = b
    while parent[s] != None:
        path = [parent[s]] + path
        s = parent[s]

    res = (distance[b], path) if distance[b] != float("inf") else None, None

    return res


n = 6
a = 1
b = 4
G, A = generate_random_weighted_digraph(n, 0.5)
print(decreasing_path(A, a, b))
visualize_weighted_graph(G)
