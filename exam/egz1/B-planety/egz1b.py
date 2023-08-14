# Szymon Szarek
# Zlozonosc obliczeniowa:O(nE^2)
# Rozwiazanie polega na funkcji rekurencyjnej solve(i,b) wraz z memoizacja. solve(i,b) oznacza, ze jestesmy na i-tej planecie majac aktualnie b paliwa.
# Na kazdej planecie rozwazamy przypadek, w ktorym tankujemy kazda dostepna ilosc paliwa ([0,E]) i przechodzimy na kolejna planete.
# Jezeli mamy 0 paliwa i na planecie istnieje teleport na inna planete, to rowniez rozpatrzamy ten przypadek. Odczytanie rozwiazania to solve(0,0) - wchodzimy na pierwsza planete bez zadnego paliwa

from egz1btesty import runtests


def planets(D, C, T, E):
    n = len(D)
    dp = [[-1 for _ in range(E + 1)] for _ in range(n)]

    # O(nE^2)
    def solve(i, b):
        nonlocal D, C, T, E, n
        if i == n - 1:
            return 0
        if dp[i][b] != -1:
            return dp[i][b]
        res = float("inf")
        # O(E)
        for fuel in range(E + 1):
            if E >= b + fuel >= D[i + 1] - D[i]:
                res = min(res, solve(i + 1, b + fuel - (D[i + 1] - D[i])) + fuel * C[i])
        if b == 0:
            planet, price = T[i]
            if planet != i:
                res = min(res, solve(planet, b) + price)
        dp[i][b] = res
        return res

    return solve(0, 0)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
