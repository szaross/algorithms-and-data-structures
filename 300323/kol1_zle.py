# Szymon Szarek
# Złożoność obliczeniowa: O(np)
# Przechodzimy iteracyjnie po elementach tablicy od 0 do n-p 
# włącznie i za każdym razem tworzymy nową tablicę S p-elementową.
# Sortujemy tablicę p i do sumy dodajemy k-ty element od końca. 
# Jest to więc k-ty największy element w tej tablicy.
# tym sposobem rozważamy wszystkie możliwe "podtablice" tablict wejściowej.

from kol1testy import runtests

def merge_sort(T):
    if len(T)==1: return T

    T1=merge_sort(T[len(T)//2:])
    T2=merge_sort(T[:len(T)//2])
    
    S=[]
    n,m=len(T1),len(T2)
    i,j=0,0

    while i<n and j<m:
        if T1[i]<T2[j]: 
            S.append(T1[i])
            i+=1
        else:
            S.append(T2[j])
            j+=1
    
    if i<n:
        for k in range(i,n):
            S.append(T1[k])
    elif j<m:
        for k in range(j,m):
            S.append(T2[k])

    return S

def ksum(T, k, p):
    #brut
    n=len(T)
    sum=0
    for i in range(n-p+1):
        S=T[i:i+p]
        S=merge_sort(S)
        sum+=S[-k]
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
