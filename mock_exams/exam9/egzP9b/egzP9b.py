from egzP9btesty import runtests


# implementacja macierzowa
def dyrektor(G, R):
    n = len(G)
    M = [[0 for _ in range(n)] for _ in range(n)]
    R = [set(R[i]) for i in range(n)]
    R2 = dict()
    for v in range(n):
        for u in R[v]:
            if (v, u) in R2:
                R2[(v, u)] += 1
            else:
                R2[(v, u)] = 1

    for v in range(n):
        for u in G[v]:
            if (v, u) not in R2:
                M[v][u] += 1
            elif R2[(v, u)] == 0:
                M[v][u] += 1
            elif R2[(v, u)] > 0:
                R2[(v, u)] -= 1

    path = []

    def DFS_visit(v):
        nonlocal M, path
        for node in range(n):
            if M[v][node]:
                M[v][node] -= 1
                DFS_visit(node)
        path.append(v)

    DFS_visit(0)
    return path[::-1]


runtests(dyrektor, all_tests=False)
