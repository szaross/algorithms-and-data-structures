from zad6testy import runtests
from queue import deque

# znajdywanie maksymalnego skojarzenia w grafie dwudzielnym


# czy jest sciezka w sieci residualnej / MOZNA POMINAC I PO PROSTU SPRAWDZAC SCIEZKE BFS-em
def min_weight(G, path):
    # print(path)
    m = G[path[0]][path[1]]
    for i in range(1, len(path) - 1):
        m = G[path[i]][path[i + 1]] if m > G[path[i]][path[i + 1]] else m
    return m


# DFS BEDZIE SZYBSZY
def BFS(G, s, t):
    # print(f"starting bfs from {s} to {t}")
    n = len(G)
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]

    d[s] = 0
    queue = deque()
    queue.append(s)

    flag = False

    while queue and not flag:
        current = queue.popleft()
        # print(f"visiting {current}")
        for v in range(n - 1, -1, -1):
            if G[current][v] == 1:
                neighbour = v
                if not visited[neighbour]:
                    d[neighbour] = d[current] + 1
                    parent[neighbour] = current
                    visited[neighbour] = True
                    queue.append(neighbour)
                    if neighbour == t:
                        flag = True
                        break
    path = []
    p = t
    while parent[p] != None:
        path = [p] + path
        p = parent[p]
    if path:
        path = [s] + path
    # print(path)
    return path


def DFS(G, s, t):
    n = len(G)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]

    stack = []
    stack.append(s)
    flag = False
    while stack and not flag:
        current = stack.pop()
        visited[current] = True
        # print(f"visiting {current}")
        for neighbour in range(len(G) - 1, -1, -1):
            if G[current][neighbour] == 1 and not visited[neighbour]:
                parent[neighbour] = current
                if neighbour == t:
                    flag = True
                stack.append(neighbour)

    path = []
    p = t
    while parent[p] != None:
        path = [p] + path
        p = parent[p]
    if path:
        path = [s] + path
    # print(parent)
    return path


def update_weight(G, path):
    # w = min_weight(G, path)
    w = 1
    for i in range(len(path) - 1):
        G[path[i]][path[i + 1]] += w
        # G[path[i + 1]][path[i]] -= w


def binworker(M):
    n = len(M)

    # postac macierzowa + 2 wierzcholki (dwudzielny)
    G = [[0 for _ in range(2 * n + 2)] for _ in range(2 * n + 2)]

    for v in range(n):
        for u in M[v]:
            G[v][u + n] = 1
            G[u + n][v] = 1

    for i in range(n):
        G[2 * n][i] = 1  # zrodlo
    for i in range(n, 2 * n):
        G[i][2 * n + 1] = 1  # ujscie

    # print(G)
    n = n * 2 + 2

    count = 0
    path = BFS(G, n - 2, n - 1)
    while path:
        count += 1  # min weight
        update_weight(G, path)
        path = BFS(G, n - 2, n - 1)

    return count


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=True)

# M = [[0, 1, 3], [2, 4], [0, 2], [3], [3, 2]]
# print(binworker(M))
