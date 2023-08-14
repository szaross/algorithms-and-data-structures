# Szymon Szarek
# Złożoność obliczeniowa:

from zad5testy import runtests


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def min_heapify(A, i, times):
    n = len(A)
    l = left(i)
    r = right(i)
    minimum = i

    if r < n and times[A[r]] < times[A[minimum]]:
        minimum = r
    if l < n and times[A[l]] < times[A[minimum]]:
        minimum = l

    if minimum != i:
        A[i], A[minimum] = A[minimum], A[i]
        min_heapify(A, minimum, times)


def extract_min(A, times):
    n = len(A)
    minimum = A[0]
    A[0] = A[n - 1]
    A.pop()
    min_heapify(A, 0, times)
    return minimum


def heap_decrease_key(A, i, key, times, neighbour):
    while i > 0 and times[A[parent(i)]] > times[A[i]]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


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

    queue = []
    queue.append(a)

    while queue:
        current = extract_min(queue, times)
        visited[current] = True
        for neighbour, distance in A[current]:
            if times[neighbour] > times[current] + distance:
                times[neighbour] = times[current] + distance
                if not visited[neighbour]:
                    queue.append(neighbour)
                    heap_decrease_key(
                        queue, len(queue) - 1, times[neighbour], times, neighbour
                    )

    return times


def spacetravel(n, E, S, a, b):
    times = dijkstra(n, E, S, a, b)
    time = times[b]
    # print(times)
    if time == float("inf"):
        return None
    return time


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)

# E = [(0,1, 5),
# (1,2,21),
# (1,3, 1),
# (2,4, 7),
# (3,4,13),
# (3,5,16),
# (4,6, 4),
# (5,6, 1)]
# S = [ 0, 2, 3 ]
# a = 1
# b = 5
# n = 7
# print(spacetravel(n, E, S, a, b))
# E=[(0, 1, 5), (1, 2, 21), (1, 3, 1), (2, 4, 7), (3, 4, 13), (3, 5, 16), (4, 6, 4), (5, 6, 1)]
# S=[0, 2, 3]
# a=4
# b=5
# n=7
# print(spacetravel(n, E, S, a, b))
