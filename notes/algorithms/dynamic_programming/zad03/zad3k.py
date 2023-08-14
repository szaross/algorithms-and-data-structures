from zad3ktesty import runtests


def ksuma(T, k):
    n = len(T)

    dp = [float("inf") for _ in range(n)]
    for i in range(k):
        dp[i] = T[i]

    for i in range(k, n):
        for j in range(i - k, i):
            dp[i] = min(dp[j] + T[i], dp[i])

    res = float("inf")
    for i in range(n - k, n, 1):
        res = min(res, dp[i])

    return res


runtests(ksuma)
