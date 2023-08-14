from egzP1atesty import runtests

# O(nm)
# def titanic(W, M, D):
#     msg = ""
#     for letter in W:
#         msg += M[ord(letter) - 65][1]

#     D = [M[D[i]][1] for i in range(len(D))]

#     dp = dict()

#     def solve(s):
#         nonlocal msg, D
#         if s == msg:
#             return 0
#         if s in dp:
#             return dp[s]

#         res = float("inf")
#         for code in D:
#             tmp = s + code
#             if tmp == msg[: len(tmp)]:
#                 res = min(res, solve(tmp) + 1)
#         dp[s] = res
#         return res

#     return solve("")


# runtests(titanic, recursion=True)


def titanic(W, M, D):
    msg = ""
    for letter in W:
        msg += M[ord(letter) - 65][1]

    D = [M[D[i]][1] for i in range(len(D))]

    D.sort(reverse=True, key=lambda x: len(x))
    # print(D)
    i = 0
    n = len(msg)
    res = 0
    s = ""
    while s != msg:
        # print(s)
        for code in D:
            # print(s + code + "==" + msg[: len(s + code)])
            if s + code == msg[: len(s + code)]:
                res += 1
                s = s + code
                break

    return res


runtests(titanic, recursion=False)

W = "SOS"
# Czyli w zapisie Morse’a: . . . - - - . . .
D = [0, 4, 13, 19, 25]
# Czyli litery: A (.-), E (.), N (-.), T (-) oraz Z (--..)
M = [
    ("A", ".-"),
    ("B", "-..."),
    ("C", "-.-."),
    ("D", "-.."),
    ("E", "."),
    ("F", "..-."),
    ("G", "--."),
    ("H", "...."),
    ("I", ".."),
    ("J", ".---"),
    ("K", "-.-"),
    ("L", ".-.."),
    ("M", "--"),
    ("N", "-."),
    ("O", "---"),
    ("P", ".--."),
    ("Q", "--.-"),
    ("R", ".-."),
    ("S", "..."),
    ("T", "-"),
    ("U", "..-"),
    ("V", "...-"),
    ("W", ".--"),
    ("X", "-..-"),
    ("Y", "-.--"),
    ("Z", "--.."),
]

print(titanic(W, M, D))
