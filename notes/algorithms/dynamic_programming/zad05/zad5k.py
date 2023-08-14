from zad5ktesty import runtests
from functools import cache


def garek(T):
    n = len(T)

    # 0 - twoj
    # 1 - garek
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    def g(i, j, ruch):
        nonlocal T, n
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if ruch == 0:
            dp[i][j] = max(g(i, j - 1, 1) + T[j], g(i + 1, j, 1) + T[i])
            return dp[i][j]
        if ruch == 1:
            if i + 1 < n:
                dp[i + 1][j] = g(i + 1, j, 0)
            if j - 1 > 0:
                dp[i][j - 1] = g(i, j - 1, 0)
            left = 0 if i + 1 >= n - 1 else dp[i + 1][j]
            right = 0 if j - 1 <= 0 else dp[i][j - 1]
            if left > right:
                return right
            else:
                return left

    return g(0, n - 1, 0)


runtests(garek)
