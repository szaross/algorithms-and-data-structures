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

def partition(T,l,r):
    x=T[(l+r)//2]
    #print(x)
    i,j=l-1,r+1

    while(i<j):
        while(True):
            i+=1
            if(T[i]>=x):
                break
        while(True):
            j-=1
            if(T[j]<=x):
                break
        if (i >= j):
            return j

        T[i],T[j]=T[j],T[i]
        
    return j


    
def quicksort(T,l,r):
    if l<r:
        q=partition(T, l, r)
        quicksort(T, q+1, r)
        


def snow( S ):
    n=len(S)
    sum=0
    quicksort(S, 0, n-1)
    for i in range(n-1,-1,-1):
        a=S[i]-(n-i-1)
        if a>0:
            sum+=a
        else:
            return sum
    return sum

#print(snow([462, 2273, 7086, 1127, 8273, 1788, 7303, 2520, 9509, 9637, 6777, 2946, 9808, 5712, 3187, 782, 5679, 2785, 4637, 8441, 2674, 8028, 2516, 3080, 7401, 8738, 3627, 2088, 9958, 436, 2436, 7032, 8386, 3253, 4937, 4607, 6741, 7261, 8988, 8860, 9243, 7119, 3787, 7490, 2276, 8361, 173, 3926, 3267, 3264, 2627, 8917, 7355, 9563, 2259, 4784, 9738, 8989, 7193, 4506, 5799, 9788, 3847, 4681, 4516, 344, 2914, 2586, 8195, 7805, 4765, 4089, 5483, 3240, 8728, 8745, 1884, 5689, 1651, 5664, 6450, 7872, 4145, 9990, 1691, 9899, 8928, 84, 5496, 1841, 1166, 4386, 1177, 7194, 1309, 6964, 5162, 2244, 9370, 1690]))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )