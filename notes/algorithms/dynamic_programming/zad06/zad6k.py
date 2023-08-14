from zad6ktesty import runtests


def haslo(S):
    n = len(S)
    dp = [-1 for _ in range(n)]
    dp[0] = 1 if S[0] != "0" else 0
    dp[1] = 2 if 0 < int(S[:2]) <= 26 else 1

    for i in range(2, n):
        res = 0
        if S[i - 1] != "0" or S[i - 1] == "2" and int(S[i]) < 7:
            res = dp[i - 1] + dp[i - 2]
        if int(S[i - 1]) > 2:
            res = dp[i - 1]
        if S[i - 1] == "0":
            if S[i] == "0":
                return 0
            res = dp[i - 1]
        if S[i] == "0":
            if int(S[i - 1]) > 2:
                return 0
            res = dp[i - 2]
        dp[i] = res
    # print(dp)
    return dp[n - 1]


runtests(haslo)
