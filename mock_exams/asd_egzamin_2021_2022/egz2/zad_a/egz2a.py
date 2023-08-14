from egz2atesty import runtests


# O(n^2)
def coal(A, T):
    magazyny = [0]
    last = 0
    for dostawa in A:
        zapakowane = False
        for i in range(len(magazyny)):
            if magazyny[i] + dostawa <= T:
                magazyny[i] = magazyny[i] + dostawa
                zapakowane = True
                last = i
                break
        if not zapakowane:
            magazyny.append(dostawa)
            last = len(magazyny) - 1
        print(magazyny)

    return last


# def bisearch(A, key, T):
#     i, j = 0, len(A)

#     while i <= j:
#         mid = (i + j) // 2
#         if A[mid] + key <= T:
#             j = mid - 1
#         else:
#             i = mid + 1
#     return i


# def coal(A, T):
#     magazyny = [0]
#     last = 0
#     for dostawa in A:
#         zapakowane = False
#         magazyn=bisearch(magazyny,dostawa,T)

#     return last


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(coal, all_tests=False)

# A = [1, 6, 2, 10, 8, 7, 1]
# T = 10
# print(coal(A, T))
