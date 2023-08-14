# Szymon Szarek
# Zlozonosc obliczeniowa: O(EV))
# Przeszktałcam graf z postaci list sąsiedztwa na listy krawędzi. Sortuję listę krawędzi rosnąco.
# Przechodzępo posortowanej liscie i sprawdzam czy z n-1 krawędzi ( od i do i+n-1) da się skonstruować spójny graf (drzewo)
# Pierwszy napotkany spójny graf jest szukanym drzewem. Ponieważ posortowałem krawędzię wiem, że krawędzie z G nie wchodzące w skład
# drzewa są albo mniejsze od m albo większe od M.

from kol2testy import runtests


# lista krawedzi
def connected(E, n):
    s = E[0][0]
    G = [[] for _ in range(n)]
    for u, v, w in E:
        G[v].append((u, w))
        G[u].append((v, w))

    # jezeli ktorys wierzcholek nie ma krawedzi zwroc false
    for u in G:
        if not u:
            return False

    visited = [False for _ in range(n)]
    queue = [s]

    while queue:
        current = queue.pop()
        for neighbour, w in G[current]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

    for i in range(n):
        if not visited[i]:
            return False
    return True


def beautree(G):
    n = len(G)
    E = []
    T = [[0 for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v, w in G[u]:
            if not T[u][v] and not T[v][u]:
                E.append((u, v, w))
                T[u][v] = 1
                T[v][u] = 1
    E.sort(key=lambda x: x[2])
    # print(E)
    sum = 0
    i = 0
    flag = False

    while i + n - 1 <= len(E) and not flag:
        # print(E[i : i + n - 1])
        if connected(E[i : i + n - 1], n):
            for j in range(i, i + n - 1):
                sum += E[j][2]
            flag = True

        i += 1

    return sum if sum != 0 else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=True)
