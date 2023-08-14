# Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, ba], [a2, b2],.. ., [an, bn]. Klocki spadają na oś
# liczbową w kolejności podanej w ciągu. Proszę zaproponować algorytm, który oblicza, ile klocków należy usunąć z listy tak, żeby każdy kolejny
# spadający klocek mieścił się w całości w tym, który spadł tuż przed nim.

# f(i) = ile klockow trzeba usunac rozwarzajac pierwsze i klockow
# f(i) = {
#   szukamy najblizszego klocka w ktorym sie miesci (j): =f(j)+i-j
# }


def contains(a, b):
    # a miesci sie na b
    xa, ya = a
    xb, yb = b
    return xa >= xb and ya <= yb


# O(n^2)
def blocks(T):
    n = len(T)

    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for i in range(1, n):
        j = i - 1
        while j >= 0 and not contains(T[i], T[j]):
            j -= 1
        if j == -1:
            dp[i] = i
        else:
            dp[i] = dp[j] + i - j - 1

    print(dp)
    return dp[n - 1]
