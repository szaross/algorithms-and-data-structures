from egzP6atesty import runtests


# O(k)
def cmp(s1, s2):
    if len(s1) == len(s2):
        c1 = 0
        for letter in s1:
            if letter.isdigit():
                c1 += 1
        c2 = 0
        for letter in s2:
            if letter.isdigit():
                c2 += 1
        return c2 - c1
    else:
        return len(s1) - len(s2)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        # if A[j] <= x:
        if cmp(A[j], x) <= 0:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


# O(nk)
def quickselect(A, p, r, k):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    if k == q:
        return A[q]
    elif k < q:
        return quickselect(A, p, q - 1, k)
    else:
        return quickselect(A, q + 1, r, k)


def google(H, s):
    return quickselect(H, 0, len(H) - 1, len(H) - s)


runtests(google, all_tests=True)
