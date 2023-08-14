from egzP8atesty import runtests


# O(n^2)
# def reklamy(T, S, o):
#     n = len(S)
#     R = [(a, b, c) for (a, b), c in zip(T, S)]
#     R.sort(key=lambda x: x[1])

#     # bierzemy i-ty element
#     max_zysk = 0
#     for i in range(n):
#         res = 0
#         for j in range(i - 1, -1, -1):
#             x, y, zysk = R[j]
#             if R[i][0] > y:
#                 res = max(res, R[j][2])
#         max_zysk = max(max_zysk, res + R[i][2])

#     return max_zysk


def reklamy(T, S, o):
    n = len(S)
    R = [(a, b, c) for (a, b), c in zip(T, S)]
    R.sort(key=lambda x: x[2])
    # print(R)
    max_zysk = 0
    for i in range(n - 1, -1, -1):
        if i > 1 and max_zysk > R[i][2] + R[i - 1][2]:
            break
        max_zysk = max(max_zysk, R[i][2])
        for j in range(i - 1, -1, -1):
            if R[i][0] > R[j][1]:
                max_zysk = max(max_zysk, R[i][2] + R[j][2])
                break

    return max_zysk


runtests(reklamy, all_tests=True)
# T = [(0, 3), (4, 5), (1, 4)]
# S = [5000, 3000, 15000]
# print(reklamy(T, S, 6))

