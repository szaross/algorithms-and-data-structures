# Szymon Szarek
# Z podanych danych tworze graf dwudzielny. Jedna grupa to pracownicy, a druga to maszyny.
# Krawędź pomiędzy nimi oznacza, że pracownik x wybrał pracę y. Aby znaleźć największą liczbę
# pracowników mogących pracować jednocześnie należy znaleźć maksymalne skojarzenie w tym grafie
# Do grafu dwudzielnego dodaję źródło i ujście i znajduje maksymalny przepływ dla tego grafu metodą Forda-Fulkersona.
# Jest on równoznaczny w maksymalnym skojarzeniem
from zad6testy import runtests
from queue import deque


def BFS(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    queue = deque()
    queue.append(s)
    visited[s] = True
    flag = False

    while queue and not flag:
        current = queue.pop()
        # print(f"visiting {current}")
        for neighbour in G[current]:
            if not visited[neighbour]:
                parent[neighbour] = current
                visited[neighbour] = True
                queue.append(neighbour)
                if neighbour == t:
                    flag = True
                    break
    path = []
    p = t
    # print(parent)
    while parent[p] != None:
        path = [p] + path
        p = parent[p]
    if path:
        path = [s] + path
    # print(path)
    return path


def update_weight(G, path):
    for i in range(len(path) - 1):
        G[path[i]].remove(path[i + 1])
        # G[path[i + 1]].append(path[i])


def binworker(M):
    n = len(M)

    # postac listowa
    G = [[] for _ in range(2 * n + 2)]

    # tworzenie grafu dwudzielnego
    for v in range(n):
        for u in M[v]:
            G[v + n].append(u)
            G[u].append(v + n)

    for i in range(n):
        G[2 * n].append(i)  # zrodlo
    for i in range(n, 2 * n):
        G[i].append(2 * n + 1)  # ujscie

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
