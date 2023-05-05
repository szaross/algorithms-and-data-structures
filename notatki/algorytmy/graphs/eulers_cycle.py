from graph_module import generate_random_graph, visualize_graph
from collections import deque
from networkx import eulerian_circuit as ec
from networkx import is_eulerian


# adjacency list
def eulerian_circuit(G):
    n = len(G)

    # check if it has an eulerian circuit
    for v in range(n):
        if len(G[v]) % 2 == 1:
            return "G doesn't have an Eulerian circuit"

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    path = []
    res = deque()
    last_considered = [-1 for _ in range(n)]
    times = [-1 for _ in range(n)]
    time = 0
    stack = []

    def dfs_visit(G, v):
        nonlocal visited, parent, path, last_considered

        if not visited[v]:
            for i in range(last_considered[v] + 1, len(G[v])):
                neighbour = G[v][i]
                if (v, neighbour) not in path and (neighbour, v) not in path:
                    parent[neighbour] = v
                    path.append((v, neighbour))
                    last_considered[v] = i
                    dfs_visit(G, neighbour)
            res.append(v)
            visited[v] = True

    for v in range(n):
        dfs_visit(G, v)

    return res


n = 5
G, A = generate_random_graph(n, 0.6)
print(eulerian_circuit(A))
if is_eulerian(G):
    print(list(ec(G)))
else:
    print("G is not Eulerian")
visualize_graph(G)
