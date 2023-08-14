# Szymon Szarek
# Złożoność obliczeniowa: O(S+(E+S)logV))
# Implementacja algorytmu Dijkstry. Zagięcia czasoprzestrzeni implementuję jako
# cykl stworzony z jego wierzchołków z krawędziami o wadze 0.
# Dane wejściowe przekształcam z listy wierzchołków na listę sąsiedztwa.

from zad5testy import runtests
import heapq


def dijkstra(n, E, S, a, b):
    times = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    times[a] = 0

    # create an adjacency list
    A = [[] for _ in range(n)]
    for element in E:
        A[element[0]].append((element[1], element[2]))
        A[element[1]].append((element[0], element[2]))
    for i in range(len(S) - 1):
        A[S[i]].append((S[i + 1], 0))
    A[S[-1]].append((S[0], 0))

    heap = []
    heapq.heappush(heap, (0, a))

    while heap:
        current = heapq.heappop(heap)[1]
        visited[current] = True
        for neighbour, distance in A[current]:
            if times[neighbour] > times[current] + distance:
                times[neighbour] = times[current] + distance
                if not visited[neighbour]:
                    heapq.heappush(heap, (times[neighbour], neighbour))

    return times


def spacetravel(n, E, S, a, b):
    times = dijkstra(n, E, S, a, b)
    time = times[b]
    if time == float("inf"):
        return None
    return time


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
