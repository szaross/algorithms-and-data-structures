from zad2testy import runtests


def depth(L):
    # L.sort(key=lambda x: x[1])
    # L.sort(key=lambda x: x[0])
    n=len(L)
    P=[]
    K=[]
    for i in range(n):
        P.append([L[i][0],i])
    
    for i in range(n-1,-1,-1):
        K.append([L[i][1],i])
   
    P.sort(key=lambda x:x[0])
    K.sort(key=lambda x:x[0])
    print(P)
    print(K)
    
    # i=0
    # max_c=0
    # counter=0
    # last_koniec=-1
    # ind=-1
    # while i<n:
    #     if P[i]<last_koniec:
    #         i+=1
        
        


    
    pass



A = [ [1, 6],
[5, 6],
[2, 5],
[8, 9],
[1, 6]]
depth(A)
#runtests( depth ) 
