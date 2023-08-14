from zad6testy import runtests
from queue import deque

# znajdywanie maksymalnego skojarzenia w grafie dwudzielnym


def BFS(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    d[s] = 0
    visited[s] = True
    queue = deque()
    queue.append(s)

    flag = False
    while queue and not flag:
        current = queue.popleft()
        for neighbour in G[current]:
            if not visited[neighbour]:
                # print(f"{current}->{neighbour}")
                d[neighbour] = d[current] + 1
                parent[neighbour] = current
                visited[neighbour] = True
                queue.append(neighbour)
                if neighbour == t:
                    flag = True
                    break

    # print(parent)
    path = []
    p = t
    while parent[p] != None:
        # print(path)
        path = [p] + path
        p = parent[p]
    if path:
        path = [s] + path
    # print(path)
    return path


def binworker(M):
    n = len(M)
    G = [[] for _ in range(2 * n + 1)]

    # tworzenie grafu dwudzielnego
    for v in range(n):
        for u in M[v]:
            G[v + n].append(u)
            G[u].append(v + n)
        G[v].append(2 * n)

    visited = [False for _ in range(2 * n + 1)]
    queue = [
        x for x in range(n, 2 * n)
    ]  # sprawdzamy tylko jedna czesc grafu dwudzielnego

    while queue:
        # print("1")
        current = queue.pop()
        flag = False
        for neighbour in G[current]:
            if not visited[neighbour]:
                # print(f"{current} matched with {neighbour}")
                visited[neighbour] = True
                visited[current] = True
                G[neighbour].remove(2 * n)
                flag = True
                break

        if not flag:
            # print(f"no path for {current}")
            path = BFS(G, current, 2 * n)
            if path:
                G[path[-2]].remove(2 * n)
                visited[path[-2]] = True
                visited[current] = True

    count = 0
    for v in range(n):
        if visited[v]:
            count += 1

    # print(visited)
    return count


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=False)
