from zad8testy import runtests
from functools import cache

# jezeli zero- nic nie robimy
# jezeli plamy maja te same id - nie dodajemy/relaksujemy

# 0 z gory
# 1 z dolu
# 2 z lewej
# 3 z prawej

# index=-T[i][j]-1


def plan(T):
    n = len(T)
    m = len(T[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    def sum_up(i, j, prev, upper):
        nonlocal T, n, visited, m
        if i > n - 1 or i < 0 or j > m - 1 or j < 0 or T[i][j] == 0 or visited[i][j]:
            return 0
        # print(f"sumup: {i} {j}")
        visited[i][j] = True
        if i == 0:
            upper.append(j)
        left = sum_up(i, j - 1, 3, upper) if prev != 2 else 0
        right = sum_up(i, j + 1, 2, upper) if prev != 3 else 0
        up = sum_up(i - 1, j, 1, upper) if prev != 0 else 0
        down = sum_up(i + 1, j, 0, upper) if prev != 1 else 0

        return left + right + up + down + T[i][j]

    # ALGORYTM REKURENCYJNY DP
    # create oils list
    oils = []
    for i in range(m):
        if T[0][i] > 0:
            upper = []
            sums = sum_up(0, i, 0, upper)
            # print(f"i:{i} upper:{upper} sums:{sums}")
            for j in upper:
                T[0][j] = -(len(oils) + 1)
            oils.append(sums)

    # dp = [float("inf") for _ in range(m)]
    # dp[0] = 1
    # energy = [0 for _ in range(m)]
    # energy[0] = oils[0]
    # for i in range(n):
    #     for j in range(1, energy[i] + 1):
    #         if i + j < m:
    #             if dp[i + j] > dp[i]:
    #                 dp[i + j] = dp[i]
    #                 energy[i + j] = energy[i] - j
    #     if T[0][i] != 0:
    #         for j in range(energy[i]+1, energy[i] + oils[-(T[0][i] + 1)] + 1):
    #             if i + j < m and T[0][i] != T[0][j]:
    #                 if dp[i + j] > dp[i] + 1:
    #                     dp[i + j] = dp[i] + 1
    #                     energy[i + j] = energy[i] + oils[-(T[0][i] + 1)] - j
    # # print(dp)
    # # print(energy)
    # # print(oils)
    # return dp[m - 1]

    # print(oils)
    # print(T)

    @cache
    def maks(i, energy, can_fuel):
        nonlocal m, oils, T
        if i + energy >= m - 1:
            return 0
        res = float("inf")
        for j in range(1, energy + 1):
            res = min(res, maks(i + j, energy - j, True))
            if T[0][i] != 0 and can_fuel and i + j < m:
                res = min(
                    res,
                    maks(
                        i + j, energy - j + oils[-(T[0][i] + 1)], T[0][i] != T[0][i + j]
                    )
                    + 1,
                )
        return res

    return maks(0, oils[0], True) + 1

    # # dp
    # dp = [float("inf") for _ in range(m)]
    # dp[0] = 0
    # # print(dp)
    # for i in range(m):
    #     for j in range(i):
    #         if T[0][i] != T[0][j] and dp[j] != float("inf"):
    #             if oils[-(T[0][j] + 1)] + j >= i:
    #                 # print(f"i:{i}")
    #                 dp[i] = min(dp[i], dp[j] + 1)
    # return dp[m - 1]

    # ALGORYTM ZACHLANNY
    # create oils list
    # oils = []
    # for i in range(0, m):
    #     if T[0][i] > 0:
    #         # print(f"{i}")
    #         upper = []
    #         sums = sum_up(0, i, 0, upper)
    #         # print(f"i:{i} upper:{upper} sums:{sums}")
    #         for j in upper:
    #             T[0][j] = -(len(oils) + 1)
    #         oils.append((i, sums))
    # sums = oils.pop(0)[1]
    # oils.sort(key=lambda x: x[1], reverse=True)
    # # print(oils)
    # # print(sums)
    # for i in range(len(oils)):
    #     if sums >= i:
    #         sums += oils[i][1]
    #     # print(sums)
    #     if sums >= m - 1:
    #         return i + 2
    # return 1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
