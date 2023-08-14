from egzP4atesty import runtests


def mosty(T):
    n = len(T)
    T.sort(key=lambda x: x[0])
    # print(T)
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        x, y = (T[i][0], T[i][1])
        for j in range(i):
            a, b = (T[j][0], T[j][1])
            if y >= b:
                dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)
    return max(dp)


runtests(mosty, all_tests=True)

# dp[i] - max ilosc mostow wiedzac ze bierzemy i-ty most
# T = [(1, 2), (2, 3), (3, 0)]
# print(mosty(T))
