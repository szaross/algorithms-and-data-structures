import networkx as nx
import matplotlib.pyplot as plt
from random import randint


def generate_random_graph(n, p):
    """Generate a random graph
    n = number of vertices
    p = propability of an edge between two vertices

    returns:(G,A), where G is a networkx Graph object and A is an adjacency list
    """
    random_graph = nx.fast_gnp_random_graph(n, p, directed=False)
    # random_dag = nx.DiGraph([(u, v) for (u, v) in random_graph.edges() if u < v])
    A = [[] for _ in range(n)]
    for i, nbrdict in random_graph.adjacency():
        A[i] += list(nbrdict.keys())
    return random_graph, A


def generate_random_digraph(n, p):
    """Generate a random digraph
    n = number of vertices
    p = propability of an edge between two vertices

    returns:(G,A), where G is a networkx Graph object and A is an adjacency list
    """
    random_graph = nx.fast_gnp_random_graph(n, p, directed=True)
    # random_dag = nx.DiGraph([(u, v) for (u, v) in random_graph.edges() if u < v])
    A = [[] for _ in range(n)]
    for i, nbrdict in random_graph.adjacency():
        A[i] += list(nbrdict.keys())
    return random_graph, A


def generate_random_dag(n, p):
    """Generate a random dag
    n = number of vertices
    p = propability of an edge between two vertices

    returns:(G,A), where G is a networkx Graph object and A is an adjacency list
    """
    random_graph = nx.fast_gnp_random_graph(n, p, directed=True)
    random_dag = nx.DiGraph([(u, v) for (u, v) in random_graph.edges() if u < v])
    A = [[] for _ in range(n)]
    for i, nbrdict in random_dag.adjacency():
        A[i] += list(nbrdict.keys())
    return random_dag, A


def generate_random_weighted_digraph(n, p):
    """Generate a random weighted digraph
    n = number of vertices
    p = propability of an edge between two vertices

    returns:(G,A), where G is a networkx Graph object and A is an adjacency list
    """
    random_graph = nx.fast_gnp_random_graph(n, p, directed=True)
    # random_dag = nx.DiGraph([(u, v) for (u, v) in random_graph.edges() if u < v])
    A = [[] for _ in range(n)]
    for i, nbrdict in random_graph.adjacency():
        for v in nbrdict.keys():
            w = randint(1, 7)
            A[i].append((v, w))
            random_graph[i][v]["weight"] = w
    return (
        random_graph,
        A,
    )


def generate_random_weighted_dag(n, p):
    """Generate a random weighted dag
    n = number of vertices
    p = propability of an edge between two vertices

    returns:(G,A), where G is a networkx Graph object and A is an adjacency list
    """
    random_graph1 = nx.fast_gnp_random_graph(n, p, directed=True)
    random_graph = nx.DiGraph([(u, v) for (u, v) in random_graph1.edges() if u < v])
    A = [[] for _ in range(n)]
    for i, nbrdict in random_graph.adjacency():
        for v in nbrdict.keys():
            w = randint(1, 7)
            A[i].append((v, w))
            random_graph[i][v]["weight"] = w
    return (
        random_graph,
        A,
    )


def visualize_weighted_graph(G):
    """Visualize a weighted graph
    G = a networkx Graph object
    """
    labels = nx.get_edge_attributes(G, "weight")
    pos = nx.shell_layout(G)
    nx.draw_networkx_edge_labels(
        G,
        pos,
        labels,
        font_color="red",
        font_size=13,
        label_pos=0.8,
    )
    nx.draw_networkx(G, pos, with_labels=True)
    plt.show()


def visualize_graph(G):
    """Visualize a graph
    G = a networkx Graph object
    """
    pos = nx.shell_layout(G)
    nx.draw_networkx(G, pos, with_labels=True)
    plt.show()
