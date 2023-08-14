from zad4ktesty import runtests
from functools import cache


def falisz(T):
    n = len(T)

    # REKURENCJA
    # @cache
    # def falisz_r(i, j):
    #     if i == 0 and j == 0:
    #         return T[0][0]
    #     left = falisz_r(i, j - 1) if j - 1 >= 0 else float("inf")
    #     up = falisz_r(i - 1, j) if i - 1 >= 0 else float("inf")
    #     return min(left, up) + T[i][j]
    #
    # return falisz_r(n - 1, n - 1)

    # DP ITERACYJNIE
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            if j + 1 < n:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + T[i][j])
            if i + 1 < n:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + T[i][j])

    return dp[n - 1][n - 1]


runtests(falisz)
