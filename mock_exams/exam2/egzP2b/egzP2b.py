from egzP2btesty import runtests
from math import log10


def kryptograf(D, Q):
    n = len(D)
    q = len(Q)

    res = 1

    for part in Q:
        if len(part) == 0:
            res *= len(D)
            continue
        s = 0
        for code in D:
            if part == code[-len(part) :]:
                s += 1
        res *= s if s != 0 else res
    return log10(res)


# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests=1)
# D = ["1100", "100", "0", "1111", "1101"]
# Q = ["", "1", "11", "0", "1101"]
# print(kryptograf(D, Q))
