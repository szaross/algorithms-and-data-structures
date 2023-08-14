# Szymon Szarek
# Zlozonosc obliczeniowa: O(n^3)
# Algorytm polega na zwyklej rekurencji metoda top-down.
# Funkcja rekurencyjna oblicza maksymalna sciezke do (n-1,n-1) z punktu (i,j) biorąc pod uwagę skąd do niej przyszlismy
from zad7testy import runtests

# 0 z gory
# 1 z dolu
# 2 z lewej


def maze(L):
    n = len(L)
    dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(3)]
    dp[0][n - 1][n - 1] = 0
    dp[1][n - 1][n - 1] = 0
    dp[2][n - 1][n - 1] = 0

    def maze_r(i, j, prev):
        nonlocal L, n
        if i < 0 or i > n - 1 or j < 0 or j > n - 1 or L[i][j] == "#":
            return float("-inf")
        if dp[prev][i][j] != -1:
            return dp[prev][i][j]

        up = maze_r(i - 1, j, 1) if prev != 0 else float("-inf")
        down = maze_r(i + 1, j, 0) if prev != 1 else float("-inf")
        right = maze_r(i, j + 1, 2)

        dp[prev][i][j] = max(up, down, right) + 1

        return dp[prev][i][j]

    res = maze_r(0, 0, 0)
    return res if res != float("-inf") else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
