# Szymon Szarek
# Zlozonosc czasowa - O(nlogn)
# Żeby zebrać jak najwięcej śniegu, musimy brać największe sterty śniegu
# Sortuję tablicę rosnąco i wybieram elementy, które będą częścią trasy
# Elementy wybieram od tyłu do momentu, w którym wiem, że reszta śniegu zdążyłaby już stopnieć po zebraniu wcześniejszych
# Wiemy, że nie ważne jest położenie stert śniegu w oryginalnej tablicy, ponieważ zawsze istnieje droga
# przechodząca przez wybrane sterty, tak aby żadna ze stert nie została rozjechana przez maszyne; 
# Sumowanie śniegu zaimplementowalem podczas sortowania metodą przez kopcowanie; jeżeli wiemy, że
# posortowana sterta śniegu zdążyła już stopniec, to znaczy ze kazda kolejna tez już stopniała i nie ma sensu dalej sortować tablicy

from zad2testy import runtests

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

def heap_sort_and_sum(T):
    n=len(T)
    sum=0
    build_heap(T)
    for i in range(n-1,0,-1):
        T[0],T[i]=T[i],T[0]
        heapify(T, 0, i)
        a=T[i]-(n-i-1)
        if a>0:
            sum+=a
        else:
            break
    return sum

def snow( S ):
    return heap_sort_and_sum(S)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )