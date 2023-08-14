# Szymon Szarek
# zlozonosc czasowa: O(N+nlogn)
# Iterujemy po tablicy i porownujemy pierwszą i ostatnią literę
# w każdym słowie. Odwracamy słowo, jeżeli ostatnia litera jest wcześniej
# w alfabecie niż pierwsza. W ten sposób nie musimy martwić się kolejnością znaków podczas porównywania.
# Sortujemy tablicę string-ów tak jak liczb, ponieważ python pozwala porównywać ciągi znaków.
# Po posortowaniu znajdujemy napis, który najwięcej razy się powtarza.

from zad3testy import runtests

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
    heap_sort(T)
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


#print(strong_string(['pies', 'mysz', 'kot', 'kogut', 'tok', 'seip', 'kot']))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
