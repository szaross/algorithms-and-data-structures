# Szymon Szarek
# Złożoność obliczeniowa: O(S^2+(E+(S choose 2))logV)
# Implementacja algorytmu Dijkstry. Zagięcia czasoprzestrzeni implementuje jako krawędzie
# (pomiędzy wszystkimi planetami jej obejmującymi) o wadze 0.
# Dane wejściowe przekształcam z listy wierzchołków na listę sąsiedztwa.

from zad5testy import runtests
from queue import PriorityQueue


def dijkstra(n, E, S, a, b):
    times = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    times[a] = 0

    # create an adjacency list
    A = [[] for _ in range(n)]
    for element in E:
        A[element[0]].append((element[1], element[2]))
        A[element[1]].append((element[0], element[2]))
    for i in range(len(S)):
        for j in range(len(S)):
            if i != j:
                A[S[i]].append((S[j], 0))

    queue = PriorityQueue()
    queue.put((0, a))

    while not queue.empty():
        current = queue.get()[1]
        visited[current] = True
        for neighbour, distance in A[current]:
            if times[neighbour] > times[current] + distance:
                times[neighbour] = times[current] + distance
                if not visited[neighbour]:
                    queue.put((times[neighbour], neighbour))

    return times


def spacetravel(n, E, S, a, b):
    times = dijkstra(n, E, S, a, b)
    time = times[b]
    if time == float("inf"):
        return None
    return time


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
