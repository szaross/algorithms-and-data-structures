from zad3testy import runtests

def counting_sort(A,j):
    n=len(A)
    C=[0] * 28
    B=[0] * n

    for i in range(n):
        if len(A[i])<=j: C[0]+=1
        else: C[ord(A[i][j])-96]+=1

    for i in range(1,27):
        C[i]+=C[i-1]

    for i in range(n-1,-1,-1):
        if len(A[i])>j:
            B[C[ord(A[i][j])-96]-1]=A[i]
            C[ord(A[i][j])-96]-=1
        else:
            B[C[0]-1]=A[i]
            C[0]-=1
        

    for i in range(n):
        A[i]=B[i]
    

def strong_string(T):
    n=len(T)
    for i in range(n):
        if T[i][-1]<T[i][0]: T[i]=T[i][::-1]
    #print(T)

    max_len=len(max(T,key=lambda x:len(x)))
    for i in range(max_len):
        counting_sort(T, i)
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

#print(strong_string(["pies", "mysz", "kot", "kogut", "tok", "seip", "kot","aga"]))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
