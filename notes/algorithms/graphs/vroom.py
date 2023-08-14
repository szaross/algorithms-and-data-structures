# car goes cha cha cha
# max 15L
from graph_module import generate_random_weighted_digraph, visualize_weighted_graph
import heapq

# nie dziala - nalezy rozmnazac wierzcholki FIZYCZNIE


# adjacency list, P: list of prices
def truck(G, P, a, b):
    MAX_LITERS = 4  # <100
    n = len(G)
    # G1 = [[] for _ in range(n)]

    # rozmnazamy wierzcholki kazda po MAX_LITERS+1 (?) [0,15] (nie musimy fizycznie rozmnazac?)
    # for v in range(n):
    #     for u, d in G[v]:
    #         for i in range(MAX_LITERS + 1):
    #             G1[v][i].append((u, d, i))

    # dijkstra
    parent = [None for _ in range(n)]
    money = [[float("inf") for _ in range(MAX_LITERS + 1)] for _ in range(n)]
    print(money[0])
    visited = [[False for _ in range(MAX_LITERS + 1)] for _ in range(n)]
    liters = [-1 for _ in range(n)]
    liters[a] = MAX_LITERS
    money[a][liters[a]] = 0

    pq = []

    heapq.heappush(pq, (0, a, liters[a]))

    while pq:
        m, current, l = heapq.heappop(pq)
        visited[current][l] = True

        for neighbour, dist in G[current]:
            for tank in range(MAX_LITERS + 1):
                print(f"visiting {current}->{neighbour} tanking {tank}")
                print(f"1:{liters[current] >= dist}")
                print(f"2:{MAX_LITERS >= liters[current] - dist + tank >= 0}")
                print(
                    f"3:{money[neighbour][liters[neighbour] - dist + tank] > money[current][l] + (P[neighbour] * tank)}"
                )
                if (
                    liters[current] >= dist
                    and MAX_LITERS >= liters[current] - dist + tank >= 0
                    and money[neighbour][liters[neighbour] - dist + tank]
                    > money[current][l] + (P[neighbour] * tank)
                ):
                    print(f"able to tank")
                    money[neighbour][liters[neighbour] - dist + tank] = money[current][
                        l
                    ] + (P[neighbour] * tank)
                    liters[neighbour] = liters[current] - dist + tank
                    if not visited[neighbour][liters[neighbour]]:
                        heapq.heappush(
                            pq,
                            (
                                money[neighbour][liters[neighbour] - dist + tank],
                                neighbour,
                                tank,
                            ),
                        )

    return money


# nie dziala - nalezy rozmnazac wierzcholki FIZYCZNIE

n = 3
# G, A = generate_random_weighted_digraph(n, 0.5)
P = [1 for _ in range(n)]
# a, b = 0, 4
# money = truck(A, P, a, b)
# print(money)
# visualize_weighted_graph(G)

A = [[(1, 3)], [(2, 2)], []]
a, b = 0, 2
money = truck(A, P, a, b)
print(money)
