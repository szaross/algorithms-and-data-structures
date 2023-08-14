# Szymon Szarek
# Złożoność obliczeniowa: O(np)
# Złożoność pamięciowa: O(p)
# Tworzymy dodatkową tablicę S, w której będziemy przechowywać aktualnie rozważany kawałek tablicy wejściowej T.
# Na początku dodaję ręcznie elementy od 0 do p do tablicy S, sortuję ją rosnąco i dodaję do sumy k-ty element od końca, który jest k-tym największym elementem w tej tablicy.
# Następnie iteruje po tablicy T od elementów p do n-p. Za każdym razem odejmuje najstarszy element w tej tablicy i dodaje kolejny element z T. Tym sposobem "przesuwamy" się
# po tablicy T bez potrzeby tworzenia tablicy dodatkowej za każdym razem na nowo.
# Po dodaniu elementu sortuję tablice zmodyfikowanym insertion sortem, gdyż jedynie jeden element jest nie na swoim miejscu (nowo dodany). Identycznie jak wcześniej dodaję do sumy k-ty element od końca.

from kol1testy import runtests


# insertion sort
def insertion_sort2(T):
    n = len(T)
    tmp = T[n - 1]
    j = n - 2
    while j >= 0 and tmp < T[j]:
        T[j + 1] = T[j]
        j -= 1
    T[j + 1] = tmp


# merge sort
def merge_sort(T):
    if len(T) == 1:
        return T

    T1 = merge_sort(T[len(T) // 2 :])
    T2 = merge_sort(T[: len(T) // 2])

    S = []
    n, m = len(T1), len(T2)
    i, j = 0, 0

    while i < n and j < m:
        if T1[i] < T2[j]:
            S.append(T1[i])
            i += 1
        else:
            S.append(T2[j])
            j += 1

    if i < n:
        for k in range(i, n):
            S.append(T1[k])
    elif j < m:
        for k in range(j, m):
            S.append(T2[k])

    return S


def ksum(T, k, p):
    n = len(T)
    sum = 0
    S = T[:p]
    S = merge_sort(S)
    sum += S[-k]
    for i in range(p, n):
        del S[S.index(T[i - p])]
        S.append(T[i])
        insertion_sort2(S)
        sum += S[-k]

    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
