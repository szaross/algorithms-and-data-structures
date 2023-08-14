from egz2btesty import runtests


def magic(C):
    n = len(C)
    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for i in range(n):
        chest = C[i][0]
        if dp[i] == -1:
            continue
        for j in range(1, 4):
            K, W = C[i][j]
            if W > i and chest - K <= 10:
                dp[W] = max(dp[W], dp[i] + chest - K)

    return dp[n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)
