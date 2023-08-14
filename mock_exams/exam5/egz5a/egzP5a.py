from egzP5atesty import runtests


# O(n^2)
def inwestor(T):
    n = len(T)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    maxx = 0
    for i in range(n):
        dp[i][i] = T[i]

    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = min(dp[i][j - 1], T[j])
            maxx = max(dp[i][j] * (j - i + 1), maxx)

    return maxx


runtests(inwestor, all_tests=True)

# T = [2, 1, 5, 6, 2, 3]
# print(inwestor(T))
