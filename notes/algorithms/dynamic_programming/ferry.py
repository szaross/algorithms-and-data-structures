# Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce, żeby wjechać na prom. Prom ma dwa
# pasy (lewy i prawy), oba długości L. Proszę napisać program, który wyznacza, które samochody powinny pojechać na który pas, żeby na promie
# zmieściło się jak najwięcej aut. Auta muszą wjeżdżać w takiej kolejności, w jakiej są podane w tablicy A.


# f(g,d,i) - czy da sie rozdzielic pierwsze i aut, tak, zeby na gornym pokladzie zajmowaly dlugosc g, a na dolnym d

# f(g,d,i) =  f(g-A[i],d,i-1) or f(g,d-A[i],i-1)
# f(A[0],0,0) = True
# f(0,A[0],0) = True


def ferry(A, L):
    n = len(A)
    F = [[[False for _ in range(n)] for _ in range(L + 1)] for _ in range(L + 1)]

    F[A[0]][0][0] = True
    F[0][A[0]][0] = True

    for i in range(1, n):
        for g in range(L + 1):
            for d in range(L + 1):
                if g - A[i] >= 0:
                    F[g][d][i] = F[g - A[i]][d][i - 1]
                if d - A[i] >= 0:
                    F[g][d][i] = F[g][d][i] or F[g][d - A[i]][i - 1]

    found = False
    for i in range(n - 1, -1, -1):
        for g in range(L, -1, -1):
            for d in range(L, -1, -1):
                if F[g][d][i]:
                    best = (g, d, i)
                    found = True
                    break
            if found:
                break
        if found:
            break

    res = []
    g, d, i = best
    while i >= 0:
        if F[g - A[i]][d][i - 1]:
            res.append("g")
            g -= A[i]
            i -= 1
        else:
            res.append("d")
            d -= A[i]
            i -= 1
    if g > 0:
        res.append("g")
    else:
        res.append("d")

    return res[::-1]


T = [5, 6, 1, 3, 2, 4, 3, 5]
L = 10

print(ferry(T, L))
