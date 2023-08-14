# elementy T[i] sa z przedzialu [0,1)
from math import floor
from insertion_sort import insertion_sort


def bucket_sort(T):
    n = len(T)
    B = [[] for _ in range(n)]
    for i in range(n):
        B[floor(n * T[i])].append(T[i])

    for i in range(n):
        insertion_sort(B[i])

    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            T[k] = B[i][j]
            k += 1


def bucket_sort_no_uniform(T):
    max_el = max(T) + 1
    for el in T:
        print(f"{el/max_el} ")


A = [883838, 277036, 376302, 429966, 986472, 337584, 261407, 657265, 392006, 747676]

bucket_sort_no_uniform(A)
# print(A)
