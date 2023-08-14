from kol3btesty import runtests
import heapq


def dijkstra(G, A, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    dist = [float("inf") for _ in range(n)]

    dist[s] = 0
    queue = [(0, s)]

    while queue:
        d_c, current = heapq.heappop(queue)
        # flag = False
        visited[current] = True
        for neighbour, d_n in G[current]:
            if not visited[neighbour]:
                if dist[neighbour] > dist[current] + d_n:
                    dist[neighbour] = dist[current] + d_n
                    if not visited[neighbour]:
                        heapq.heappush(queue, (dist[neighbour], neighbour))

                    # parent[neighbour] = current
                    # flag = True
                # if dist[neighbour] > dist[current] + A[current] + A[neighbour]:
                #     dist[neighbour] = dist[current] + A[current] + A[neighbour]
                #     flag = True
                # if flag:

    return dist[t]


def airports(G, A, s, t):
    n = len(G)

    # add all edges between airports
    for v in range(n):
        for u in range(n):
            G[v].append((u, A[u] + A[v]))

    return dijkstra(G, A, s, t)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)
