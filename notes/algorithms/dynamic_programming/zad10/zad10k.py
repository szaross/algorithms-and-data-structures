from zad10ktesty import runtests
from math import floor, sqrt


def dywany(n):
    k = floor(sqrt(n))
    dp = [[-1 for _ in range(n + 1)] for _ in range(k + 1)]
    child = [None for _ in range(k + 1)]

    def solve(i, remaining_sum):
        nonlocal dp
        if remaining_sum == 0:
            return 0
        elif i == 0 or remaining_sum < 0:
            return float("inf")

        if dp[i][remaining_sum] != -1:
            return dp[i][remaining_sum]

        if i**2 <= remaining_sum:
            p = remaining_sum // (i**2)
            r1 = solve(i - 1, remaining_sum)
            r2 = solve(i - 1, remaining_sum - p * (i**2)) + p
            if r1 < r2:
                dp[i][remaining_sum] = r1
                child[i] = 0
            else:
                dp[i][remaining_sum] = r2
                child[i] = p
            return dp[i][remaining_sum]

        dp[i][remaining_sum] = solve(i - 1, remaining_sum)
        child[i] = 0
        return dp[i][remaining_sum]

    r = solve(k, n)
    # print(child)

    i = k
    counted = 0
    a = n
    res = []
    while i >= 0 and a != 0:
        if i**2 <= a:
            p = a // (i**2)
            # print(p)
            r1 = dp[i - 1][a] if dp[i - 1][a] != -1 else 0
            r2 = dp[i - 1][a - p * (i**2)] if dp[i - 1][a - p * (i**2)] != -1 else 0
            if r1 < r2:
                # print("r1")
                res += [i] * (dp[i][a] - r1)
            else:
                # print("r2")
                # print(r2)
                res += [i] * (dp[i][a] - r2)
                a -= p * (i**2)

        i -= 1
    # print(r)
    return res


runtests(dywany)
# print(dywany(791))
