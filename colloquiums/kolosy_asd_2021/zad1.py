from math import ceil

def magiczne_piatki(T,p,r,k):
    #ilosc_grup=ceil((r-p+1)/5)
    #mediany=[0]*ilosc_grup
    mediany=[]
    for i in range(p,r,5):
        mediany.append(magiczne_piatki(T, i, i+5-1, (2*i+5)//2))
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


def flatten_array(T):
    n=len(T)
    A=[0 for _ in range(n*n)]

    for i in range(n):
        for j in range(n):
            A[i*n+j]=T[i][j]
    return A


def Median(T):
    #pozycja po posortowaniu
    n=len(T)
    m=n*n
    if n%2==0:
        pos=((m-n)//2,m-(m-n)//2)
    else:
        pos=((n//2)*n,((n//2)*n)+n)
    
    print(pos)
    splaszczona_T=flatten_array(T)
    print(splaszczona_T)
    
    # przekatna=[0]*n
    # j=0
    # for i in range(pos[0],pos[1]):
    #     przekatna[j]=magiczne_piatki(splaszczona_T,0,m-1,i)
    #     j+=1
    
    # pass

T= [ [ 2, 3, 5,6],
[ 7,11,13,14],
[17,19,23,22],
[24,26,27,28] ]

Median(T)