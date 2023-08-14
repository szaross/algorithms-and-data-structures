from egzP7atesty import runtests


# brute force
# poprawne rozwiazanie: graf dwudzielny + max skojarzenie (algorytmy przeplywu)
def akademik(T):
    n = len(T)

    def solve(i, memo):
        nonlocal T, n
        if i == n:
            return 0
        if T[i] == (None, None, None):
            return solve(i + 1, memo)
        res = float("inf")
        for dorm in T[i]:
            if dorm not in memo:
                memo.add(dorm)
                res = min(res, solve(i + 1, memo))
                memo.remove(dorm)
        if res == float("inf"):
            return solve(i + 1, memo) + 1
        return res

    return solve(0, set([None]))


runtests(akademik)
# T = [
#     (1, None, None),
#     (1, 3, 8),
#     (2, 4, 8),
#     (3, 5, 8),
#     (1, 4, 9),
#     (0, 6, None),
#     (1, 4, None),
#     (3, None, None),
#     (3, 4, None),
#     (2, 3, 4),
# ]
# print(akademik(T))

# [
#     [5],
#     [0, 1, 4, 6],
#     [2, 9],
#     [1, 3, 7, 8, 9],
#     [2, 4, 6, 8, 9],
#     [3],
#     [5],
#     [],
#     [1, 2, 3],
#     [4],
# ]
