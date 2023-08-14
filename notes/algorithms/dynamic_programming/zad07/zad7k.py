from zad7ktesty import runtests


def ogrodnik(T, D, Z, l):
    m = len(T)
    n = len(T[0])
    visited = [[False for _ in range(n)] for _ in range(m)]

    def sum_up(i, j):
        nonlocal visited, n, m, T
        if i > m - 1 or i < 0 or j > n - 1 or j < 0 or visited[i][j] or T[i][j] == 0:
            return 0
        visited[i][j] = True

        top = sum_up(i - 1, j)
        bottom = sum_up(i + 1, j)
        right = sum_up(i, j + 1)
        left = sum_up(i, j - 1)

        return top + bottom + left + right + T[i][j]

    for index in D:
        T[0][index] = sum_up(0, index)

    # knapsack problem
    n = len(D)
    for i in range(n):
        D[i] = T[0][D[i]]

    dp = [[0 for _ in range(l + 1)] for _ in range(n)]

    for b in range(D[0], l + 1):
        dp[0][b] = Z[0]

    for b in range(l + 1):
        for i in range(1, n):
            dp[i][b] = dp[i - 1][b]
            if b - D[i] >= 0:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - D[i]] + Z[i])

    return dp[n - 1][l]


runtests(ogrodnik, all_tests=True)
