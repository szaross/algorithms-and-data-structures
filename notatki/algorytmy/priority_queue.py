def parent(i): return (i-1)//2
def left(i): return 2*i+1
def right(i): return 2*i+2



def min_heapify(A,i):
    n=len(A)
    l=left(i)
    r=right(i)
    minimum=i

    if l<n and A[l]<A[minimum]: minimum=l
    if r<n and A[r]<A[minimum]: minimum=r

    if minimum!=i:
        A[i],A[minimum]=A[minimum],A[i]
        min_heapify(A, minimum)

def extract_min(A):
    n=len(A)
    minimum=A[0]
    A[0],A[n-1]=A[n-1],A[0]
    A.pop()
    min_heapify(A, 0)
    return minimum

def heap_decrease_key(A,i,key):
    A[i]=key
    while i>0 and A[parent(i)]>A[i]:
        A[i],A[parent(i)]=A[parent(i)],A[i]
        i=parent(i)

def build_heap(T):
    n=len(T)
    for i in range(n-1,-1,-1):
        min_heapify(T, i)

A=[1,2,10,9,7,3]
build_heap(A)
print(f'build heap:{A}')
m=extract_min(A)
print(f'extract min ({m}): {A}')
heap_decrease_key(A, 3, 1)
print(f'change key:{A}')

