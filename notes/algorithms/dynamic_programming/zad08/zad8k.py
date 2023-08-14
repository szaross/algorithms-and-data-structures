from zad8ktesty import runtests


def napraw(s, t):
    n = len(s)
    m = len(t)
    dp = [[float("inf") for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][n] = m - i
    for i in range(n + 1):
        dp[m][i] = n - i

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if t[i] == s[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1

    return dp[0][0]


runtests(napraw)


# s = "swidry"
# t = "kawiory"
# print(napraw(s, t))
