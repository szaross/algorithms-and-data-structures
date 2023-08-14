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


T = [
    (1, 1),
    (22, 2),
    (3, 3),
    (1, 5),
    (2, 3),
    (5, 2),
    (1, 6),
    (3, 11),
]
print(merge_sort(T))
