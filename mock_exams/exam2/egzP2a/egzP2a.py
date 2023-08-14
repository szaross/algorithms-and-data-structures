from egzP2atesty import runtests


# pomysl 1 - sortowanie + rozstawienie uczniow
# pomysl 2 - funkcja partition dla osob siedzących na "skrajach" rzędów


# 1
def zdjecie(T, m, k):
    S = sorted(T, key=lambda x: x[1])
    l = 0
    print(f"len T: {len(T)}")
    for i in range(m - 1, 0, -1):
        # print("i")
        for j in range(i, i + k * m, m):
            print(j)
            T[j] = S[l]
            # print(l)
            l += 1
        k += 1
    i = 0
    while i < len(T):
        T[i] = S[l]
        l += 1
        i += m

    T[-1] = S[-1]

    return None


runtests(zdjecie, all_tests=True)

# m = 2  # Ilość rzędów
# k = 2  # Ilość osób w najniższym rzędzie
# T = [(1001, 154), (1002, 176), (1003, 189), (1004, 165), (1005, 162)]
# # I rząd     #II rząd    #I rząd     #II rząd    #I rząd
# print(zdjecie(T, m, k))
