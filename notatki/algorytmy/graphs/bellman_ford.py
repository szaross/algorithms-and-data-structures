from graph_module import generate_random_weighted_digraph, visualize_weighted_graph


# adjacency list
def bf(G, a, b):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    distance[a] = 0

    # relax
    for v in range(n):
        for u, d in G[v]:
            if distance[u] > distance[v] + d:
                distance[u] = distance[v] + d
                parent[u] = v

    path = [b]
    s = b
    while parent[s] != None:
        path = [parent[s]] + path
        s = parent[s]

    # find negative cycles
    for v in range(n):
        for u, d in G[v]:
            if distance[u] != float("inf") and distance[u] > distance[v] + d:
                print(f"{v}->{u}: {distance[u]} > {distance[v]} + {d}")
                # negative cycle exists
                return None
    return distance[b], path


G, A = generate_random_weighted_digraph(5, 0.4)
a = 0
b = 3
print(bf(A, a, b))
visualize_weighted_graph(G)
