from math import ceil

# def magic_fives(A,p,r,k):
#     if p==r:
#         return A[p]
#     mediany=[]
#     ilosc_grup=ceil((r-p+1)/5)

#     for i in range(p,r+1-ilosc_grup,ilosc_grup):
#         mediany.append(A[i:i+ilosc_grup][(ilosc_grup)//2])
    
#     x=magic_fives(mediany, 0, len(mediany)-1, len(mediany)//2)

#     pos=partition(A, p, r, x)
#     if pos==k:
#         return x
#     elif pos>k:
#         return magic_fives(A, p, pos-1, k)
#     else:
#         return magic_fives(A, pos+1, r, k)

def bubblesort(T):
    for i in range(len(T)):
        a=0
        b=1
        while b < len(T):
            if T[a] > T[b]:
                T[a],T[b] = T[b],T[a]
            a+=1
            b+=1
    return

def magiczne_piatki(T,p,r,k):
    if p==r:
        return T[p]
    #ilosc_grup=ceil((r-p+1)/5)
    #mediany=[0]*ilosc_grup
    chunks = [T[i : i+5] for i in range(p, r+1, 5)]
    mediany=[]
    for el in chunks:
        bubblesort(el)
        mediany.append(el[len(el)//2])
    print(chunks)
    x=magiczne_piatki(mediany, 0, len(mediany)-1, len(mediany)//2)

    pos=partition(T,p,r,x)

    if pos==k:
        return T[k]
    elif pos>k:
        return magiczne_piatki(T, p, pos-1, k)
    else:
        return magiczne_piatki(T, pos+1, r, k)

def partition(A,p,r,pivot):
    x=pivot
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

A=[1,7,3,4,1,2,1,1,4,5,32,1,2,56,563,34,5]
k=10
print(f'WYNIK: {magiczne_piatki(A, 0, len(A)-1, k)}')
print(sorted(A))