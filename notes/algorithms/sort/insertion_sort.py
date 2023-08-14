def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        tmp = T[i]
        j = i - 1

        while j >= 0 and tmp < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = tmp
