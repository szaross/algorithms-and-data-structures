# Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las składa się z n drzew rosnących
# na pozycjach O, ..., n-1. Dla każdego i e{0,...,n-1} znany jest zysk c, jaki można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce
# uzyskać maksymalny zysk ze ścinanych drzew, ale prawo zabrania ścinania dwóch drzew z rzędu. Proszę zaproponować algorytm, dzięki
# któremu John znajdzie optymalny plan wycinki.


# f(i) - maksymalny zysk mozliwy do zdobycia rozwazając pierwsze i drzew
# f(i) = max(f(i-2)+C[i],f(i-1))
# f(0)=C[0]
# f(1)=C[1]


def black_forest(C):
    n = len(C)
    f = [0 for _ in range(n)]
    f[0] = C[0]
    if n > 1:
        f[1] = C[1]

    for i in range(2, n):
        f[i] = max(f[i - 2] + C[i], f[i - 1])

    return f[n - 1]
