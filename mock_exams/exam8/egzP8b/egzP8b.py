from egzP8btesty import runtests
import heapq


def dijkstra(G, s, P):
    n = len(G)
    # print(len(P), P[-1])
    visited = [False for _ in range(n)]
    # distance = [0 for _ in range(n)]
    queue = [(0, 1, s)]
    i = 0

    while queue:
        distance, next_index, current = heapq.heappop(queue)
        # print(next_index, current)
        # visited[current] = True
        if next_index == len(P) and current == P[-1]:
            return distance
        for neighbour, d in G[current]:
            addable = True
            found = False
            for j in range(len(P)):
                if P[j] == neighbour:
                    if j < next_index:
                        addable = False
                    found = j == next_index
                    break
            # if found:
            #     visited[current] = True
            if addable and not visited[neighbour]:
                # print(f"{current}->{neighbour}")
                # print((distance + d, next_index + int(found), neighbour))
                heapq.heappush(
                    queue, (distance + d, next_index + int(found), neighbour)
                )


def robot(G, P):
    # print(G)
    # print(P)
    return dijkstra(G, P[0], P)


runtests(robot, all_tests=False)
