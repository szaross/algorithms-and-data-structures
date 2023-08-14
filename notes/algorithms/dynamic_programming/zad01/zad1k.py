from zad1ktesty import runtests


def roznica(S):
    # print(S)
    n = len(S)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = -1 if S[i] == "0" else 1

    maximum = -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            x = -1 if S[j] == "0" else 1
            dp[i][j] = dp[i][j - 1] + x
            if abs(dp[i][j]) > maximum and abs(dp[i][j]) < j - i + 1:
                maximum = abs(dp[i][j])
    # print(dp)
    return maximum if maximum != len(S) else -1


# runtests(roznica)
S = "10000011111001010101"
print(roznica(S))
