from egzP3atesty import runtests
from math import inf


class Node:
    def __init__(self, wyborcy, koszt, fundusze):
        self.next = None
        self.wyborcy = wyborcy
        self.koszt = koszt
        self.fundusze = fundusze
        self.x = None


# rekurencyjnie
# def wybory(T):
#     res = 0
#     # O(mnp)
#     for wybory in T:
#         fundusze = wybory.fundusze
#         okregi = []
#         curr = wybory
#         while curr != None:
#             okregi.append(curr)
#             curr = curr.next

#         n = len(okregi)
#         dp = dict()

#         # O(np)
#         def solve(i, fundusz):
#             nonlocal dp, n
#             if fundusz < 0:
#                 return float("-inf")
#             if i == n:
#                 return 0
#             if (i, fundusz) in dp:
#                 return dp[(i, fundusz)]

#             dp[(i, fundusz)] = max(
#                 solve(i + 1, fundusz - okregi[i].koszt) + okregi[i].wyborcy,
#                 solve(i + 1, fundusz),
#             )
#             return dp[(i, fundusz)]

#         res += solve(0, fundusze)

#     return res


# runtests(wybory, all_tests=True)


# iteracyjnie
def wybory(T):
    res = 0
    for wybory in T:
        fundusze = wybory.fundusze
        okregi = []

        # linked list -> array
        curr = wybory
        while curr != None:
            okregi.append(curr)
            curr = curr.next

        # 
        n = len(okregi)
        dp = [[0 for _ in range(fundusze + 1)] for _ in range(n)]
        for i in range(okregi[0].koszt, fundusze + 1):
            dp[0][i] = okregi[0].wyborcy

        for f in range(fundusze + 1):
            for i in range(1, n):
                dp[i][f] = dp[i - 1][f]
                if f - okregi[i].koszt >= 0:
                    dp[i][f] = max(
                        dp[i][f], dp[i - 1][f - okregi[i].koszt] + okregi[i].wyborcy
                    )
        res += dp[n - 1][fundusze]
    return res


runtests(wybory, all_tests=True)
