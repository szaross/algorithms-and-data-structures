from zad2ktesty import runtests


def palindrom(S):
    # print(S)
    n = len(S)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    def pal_r(i, j):
        nonlocal dp
        if dp[i][j] != -1:
            return dp[i][j]
        elif j == i + 1:
            dp[i][j] = S[i] == S[j]
            return dp[i][j]
        elif S[i] != S[j]:
            dp[i][j] = False
            return False
        else:
            return pal_r(i + 1, j - 1)

    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = pal_r(i, j)

    a, b = 0, 0
    for i in range(n):
        for j in range(1, n):
            if dp[i][j] and b - a < j - i:
                a, b = i, j

    return S[a : b + 1]


runtests(palindrom)
# S = "abaaabaaba"
# print(palindrom(S))
