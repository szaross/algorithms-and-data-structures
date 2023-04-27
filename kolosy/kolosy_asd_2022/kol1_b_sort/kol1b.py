# Zlozonosc czasowa: O(N*logN)
# Zlozonosc pamieciowa: O(N)

from kol1btesty import runtests

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


def counting_sort(A):
    n=len(A)
    A=[ord(x)-97 for x in A]
    C=[0]*26
    B=[0]*n

    for i in range(n):
        C[A[i]]+=1
    
    for i in range(1,26):
        C[i]=C[i-1]+C[i]

    for i in range(n-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1

    for i in range(n):
        A[i]=B[i]+97
    
    s=""
    for el in A:
        s+=chr(el)

    return s
    
def f(T):
    n=len(T)
    for i in range(n):
        T[i]=counting_sort(T[i])

    T=merge_sort(T)
    #print(T)
    max_c=1
    last=T[0]
    count=1
    for i in range(1,n):
        if T[i]==last:
            count+=1
        else:
            max_c=count if count>max_c else max_c
            count=1
            last=T[i]
    max_c=count if count>max_c else max_c
    
    return max_c

# T="dsafgs"
# T=counting_sort(T)
# print(T)

# T=['tygrys', 'kot', 'wilk', 'trysyg', 'wlik', 'sygryt', 'likw', 'tygrys']
# print(f(T))
# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )


# A=['aaaaaaaaaaabbbbbbbbcccccccccccccccccccccccddddddddddddddddddeeeeeeeeeeeeeeefffffffffffffffgggggggggggggghhhhhhhhhhhhiiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjkkkkkkkkkkkkkllllllllllllllllllmmmmmmmmmmmmnnnnnnnnnnnnnooooooooooooooooppppppppppppqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrssssssssssssttttttttttttuuuuuuuuuuuuvvvvvvvvvvvvvvwwwwwwwxxxxxxxxxxxxxxyyyyyyyzzzzzzzzzzzzz', 'aaaaabbbccccccccddddddeeeeeeffffffhhiiiiiijjjjjjjjkkkkkkklllmnnnnnnnnnnooooooopppppqqqqqqqqrrrrsstttttuuvvvvvwwwwxxxxxyyyyyyyyzzz', 'aaaaaaaaaaabbbbbbbbcccccccccccccccccccccccddddddddddddddddddeeeeeeeeeeeeeeefffffffffffffffgggggggggggggghhhhhhhhhhhhiiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjkkkkkkkkkkkkkllllllllllllllllllmmmmmmmmmmmmnnnnnnnnnnnnnooooooooooooooooppppppppppppqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrssssssssssssttttttttttttuuuuuuuuuuuuvvvvvvvvvvvvvvwwwwwwwxxxxxxxxxxxxxxyyyyyyyzzzzzzzzzzzzz', 'aaaaabbbccccccccddddddeeeeeeffffffhhiiiiiijjjjjjjjkkkkkkklllmnnnnnnnnnnooooooopppppqqqqqqqqrrrrsstttttuuvvvvvwwwwxxxxxyyyyyyyyzzz', 'aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbcccccccccccccccccddddddddddddddddddeeeeeeeeefffffffffffffggggggggggggggggggggggggggggghhhhhhhhhhhiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkklllllllllllllllmmmmmmmmmmmnnnnnnnnnnnnnnnoooooooooooooppppppppppppppppppppppqqqqqqqqqqqqqqqrrrrrrrrrrrrsssssssssssssssssssssstttttttttttttttttttuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvwwwwwwwwwwwxxxxxxxxxyyyyyyyyyyyyzzzzzzzzzzzzzzzzz', 'aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbcccccccccccccccccddddddddddddddddddeeeeeeeeefffffffffffffggggggggggggggggggggggggggggghhhhhhhhhhhiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkklllllllllllllllmmmmmmmmmmmnnnnnnnnnnnnnnnoooooooooooooppppppppppppppppppppppqqqqqqqqqqqqqqqrrrrrrrrrrrrsssssssssssssssssssssstttttttttttttttttttuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvwwwwwwwwwwwxxxxxxxxxyyyyyyyyyyyyzzzzzzzzzzzzzzzzz', 
# 'aaaaabbbccccccccddddddeeeeeeffffffhhiiiiiijjjjjjjjkkkkkkklllmnnnnnnnnnnooooooopppppqqqqqqqqrrrrsstttttuuvvvvvwwwwxxxxxyyyyyyyyzzz', 'aabbbbbbbcccccccccdddddeeffffffggggggghhhhhhhiiiiiijjkkkkkkkllmmmmmmmnnnnnnnoooooppppppppqqqqqrrrsssssttttuvvvvvwwwxxyyyyyyyyzzzzzzzz', 'aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbcccccccccccccccccddddddddddddddddddeeeeeeeeefffffffffffffggggggggggggggggggggggggggggghhhhhhhhhhhiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkklllllllllllllllmmmmmmmmmmmnnnnnnnnnnnnnnnoooooooooooooppppppppppppppppppppppqqqqqqqqqqqqqqqrrrrrrrrrrrrsssssssssssssssssssssstttttttttttttttttttuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvwwwwwwwwwwwxxxxxxxxxyyyyyyyyyyyyzzzzzzzzzzzzzzzzz', 'aaaaabbbccccccccddddddeeeeeeffffffhhiiiiiijjjjjjjjkkkkkkklllmnnnnnnnnnnooooooopppppqqqqqqqqrrrrsstttttuuvvvvvwwwwxxxxxyyyyyyyyzzz']
# for el in A:
#     print(el)