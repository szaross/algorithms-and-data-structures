from zad3testy import runtests
from random import randint

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
    x=A[r]
    i=p-1

    for j in range(p,r):
        if A[j][1]<=x[1]:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1


def strong_string(T):
    n=len(T)
    for i in range(n):
        suma=0
        for j in range(len(T[i])):
            suma+=ord(T[i][j])
        T[i]=(T[i],suma)
    
    quicksort(T, 0, n-1)

    max_s=1
    val=T[0][1]
    S=[]
    S.append((T[0][0],1))
    i=1
    while i<n:
        #print(f'{i} {n} {T[i][1]}=={val}')
        while i<n and T[i][1]==val:
            #print(f'{S}')
            trafil=False
            for j in range(len(S)):
               #print(el)
                if (len(S[j][0])==len(T[i][0])) and (T[i][0]==S[j][0] or T[i][0][::-1]==S[j][0]):
                    #print(f'{T[i][0]} pasuje do {S[j]}')
                    trafil=True
                    S[j]=(S[j][0],S[j][1]+1)
            if not trafil:
                S.append((T[i][0],1))
            i+=1
        else:
            for p in S:
                if p[1]>max_s: max_s=p[1]
            if i>=n-1:
                break
            S=[]
            S.append((T[i][0],1))
            val=T[i+1][1]
            i+=1
                
            

    return max_s



# S=["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
# print(strong_string(S))
# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
