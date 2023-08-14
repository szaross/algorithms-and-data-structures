from zad11ktesty import runtests
from functools import cache


def kontenerowiec(T):
    n = len(T)
    dp = dict()

    def solve(i, l, r):
        nonlocal n, T
        if i == n:
            dp[(i, l, r)] = abs(l - r)
            return dp[(i, l, r)]

        if (i, l, r) in dp:
            return dp[(i, l, r)]

        dp[(i, l, r)] = min(solve(i + 1, l + T[i], r), solve(i + 1, l, r + T[i]))
        return dp[(i, l, r)]

    return solve(0, 0, 0)


runtests(kontenerowiec)
