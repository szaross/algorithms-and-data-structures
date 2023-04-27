import networkx as nx
import matplotlib.pyplot as plt


def generate_random_dag(n, p):
    random_graph = nx.fast_gnp_random_graph(n, p, directed=True)
    random_dag = nx.DiGraph([(u, v) for (u, v) in random_graph.edges() if u < v])
    A = [[] for _ in range(n)]
    for i, nbrdict in random_dag.adjacency():
        A[i] += list(nbrdict.keys())
    return random_dag, A


# G, A = generate_random_dag(5, 0.6)
# nx.draw_networkx(G, with_labels=True)
# plt.show()
