from zad3testy import runtests
from math import ceil
from statistics import median

def quicksort(A,p,r):
    while p<r:
        q=partition(A, p, r)
        if q-p>r-q:
            quicksort(A, q+1, r)
            r=q-1
        else:
            quicksort(A, p, q-1)
            p=q+1

def partition(A,p,r):
    x=magic_fives(A, p, r)
    #print(x)
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def magic_fives(A,p,r):
    mediany=[]
    ilosc_grup=ceil((r-p+1)/5)
    for i in range(p,r+1-ilosc_grup,ilosc_grup):
        S=A[i:i+ilosc_grup]
        heap_sort(S)
        mediany.append(S[len(S)//2])
    heap_sort(mediany)
    return mediany[len(mediany)//2]


def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1)//2

def heapify(T,i,n):
    l=left(i)
    r=right(i)
    max_ind=i

    if l<n and T[l]>T[max_ind]: max_ind=l
    if r<n and T[r]>T[max_ind]: max_ind=r

    if max_ind!=i:
        T[i],T[max_ind]=T[max_ind],T[i]
        heapify(T,max_ind,n)

def build_heap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T, i, n)

def heap_sort(T):
    n=len(T)
    sum=0
    build_heap(T)
    for i in range(n-1,0,-1):
        T[0],T[i]=T[i],T[0]
        heapify(T, 0, i)



def strong_string(T):
    n=len(T)
    for i in range(n):
        if T[i][-1]<T[i][0]: T[i]=T[i][::-1]
    quicksort(T, 0, n-1)
    #print(T)
    
    last_val=T[0]
    max_sum=1
    sum=1
    for i in range(1,n):
        if T[i]==last_val:
            sum+=1
        else:
            max_sum=sum if sum>max_sum else max_sum
            last_val=T[i]
            sum=1

    max_sum=sum if sum>max_sum else max_sum
    return max_sum


# def strong_string(T):
#     n=len(T)
#     for i in range(n):
#         suma=0
#         for j in range(len(T[i])):
#             suma+=ord(T[i][j])
#         T[i]=(T[i],suma)
    
#     quicksort(T, 0, n-1)

#     max_s=1
#     val=T[0][1]
#     S=[]
#     S.append((T[0][0],1))
#     i=1
#     while i<n:
#         #print(f'{i} {n} {T[i][1]}=={val}')
#         while i<n and T[i][1]==val:
#             #print(f'{S}')
#             trafil=False
#             for j in range(len(S)):
#                #print(el)
#                 if (len(S[j][0])==len(T[i][0])) and (T[i][0]==S[j][0] or T[i][0][::-1]==S[j][0]):
#                     #print(f'{T[i][0]} pasuje do {S[j]}')
#                     trafil=True
#                     S[j]=(S[j][0],S[j][1]+1)
#             if not trafil:
#                 S.append((T[i][0],1))
#             i+=1
#         else:
#             for p in S:
#                 if p[1]>max_s: max_s=p[1]
#             if i>=n-1:
#                 break
#             S=[]
#             S.append((T[i][0],1))
#             val=T[i+1][1]
#             i+=1 

#     return max_s



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
