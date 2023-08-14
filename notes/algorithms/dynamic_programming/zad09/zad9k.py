from zad9ktesty import runtests


# def prom(P, g, d):
#     n = len(P)
#     res = [[-1, None] for _ in range(n)]
#     dp = [[[-1 for _ in range(d + 1)] for _ in range(g + 1)] for _ in range(n)]

#     def f(i, g, d):
#         nonlocal P, n, res, dp
#         if g <= 0 or d <= 0 or i >= n:
#             return 0
#         if dp[i][g][d] != -1:
#             return dp[i][g][d]
#         up = f(i + 1, g - P[i], d)
#         down = f(i + 1, g, d - P[i])

#         dp[i][g][d] = max(up, down) + 1
#         return dp[i][g][d]

#     r = f(0, g, d)
#     # print(dp)

#     sol1 = []
#     sol2 = []
#     g1, d1 = g, d
#     i = 0
#     while i < r and (g1 >= P[i] or d1 >= P[i]):
#         up = dp[i + 1][g1 - P[i]][d1] if g1 - P[i] >= 0 else -1
#         down = dp[i + 1][g1][d1 - P[i]] if d1 - P[i] >= 0 else -1
#         if up > down:
#             g1 -= P[i]
#             sol1.append(i)
#         else:
#             d1 -= P[i]
#             sol2.append(i)
#         i += 1

#     # print(sol1)
#     # print(sol2)

#     if len(sol1) > 0 and sol1[-1] == r - 1:
#         return sol1
#     else:
#         return sol2


def prom(P, g, d):
    dp = [[None for i in range(d + 1)] for _ in range(g + 1)]

    def rek(l1, l2, i: int, counter: int, z1, z2):
        size = P[i]

        if l1 + size > g and l2 + size > d:
            return
        if l1 + size > g:  # gora zajeta
            dp[l1][l2 + size] = (
                counter + 1,
                z1,
                z2 + [i],
                i,
                0,
            )  # liczba zmieszczonych, gorny poklad, dolny poklad, ostatni index, ostatni poklad
            return rek(l1, l2 + size, i + 1, counter + 1, z1, z2 + [i])
        if l2 + size > d:  # dol zajety
            dp[l1 + size][l2] = (counter + 1, z1 + [i], z2, i, 1)
            return rek(l1 + size, l2, i + 1, counter + 1, z1 + [i], z2)

        rek(l1, l2 + size, i + 1, counter + 1, z1, z2 + [i])
        rek(l1 + size, l2, i + 1, counter + 1, z1 + [i], z2)

    M = 0
    indices = []
    rek(0, 0, 0, 0, [], [])
    for i in range(g + 1):
        for j in range(d + 1):
            if dp[i][j] is not None:
                cars_number, up, down, last_index, last_floor = dp[i][j]
                if cars_number >= M:
                    if last_floor == 0:
                        indices = down
                    else:
                        indices = up
                    M = cars_number

    return indices


runtests(prom)
