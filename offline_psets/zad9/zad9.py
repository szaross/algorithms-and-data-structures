from zad9testy import runtests
from functools import cache
import sys


def min_cost(O, C, T, L):
    n = len(O)
    parkings = []
    for i in range(n):
        parkings.append((O[i], C[i]))

    parkings.sort(key=lambda x: x[0])
    # print(parkings)

    # used: 2*T used
    @cache
    def rec(i, used):
        nonlocal parkings, T, L
        if i <= T:
            return 0
        res = float("inf")

        # zamienic na binary search
        j = len(parkings) - 1
        while parkings[j][0] >= i:
            j -= 1

        while parkings[j][0] >= i - T and j >= 0:
            res = min(res, rec(parkings[j][0], used) + parkings[j][1])
            j -= 1
        if not used:
            while parkings[j][0] >= i - 2 * T and j >= 0:
                res = min(res, rec(parkings[j][0], True) + parkings[j][1])
                j -= 1
        return res

    return rec(L - 1, False)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)

# O = [17, 20, 11, 5, 12]
# C = [9, 7, 7, 7, 3]
# T = 7
# L = 25
# print(min_cost(O, C, T, L))
