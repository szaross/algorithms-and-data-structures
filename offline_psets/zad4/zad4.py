# Szymon Szarek
# Złożoność obliczeniowa: O((d+1)*(E+V)), gdzie d to długość najkrótszej ścieżki od s do t
# Wyznaczamy najktórszą ścieżkę z s do t za pomocą BFS-a. Zapisujemy ją do zmiennej shortest przy pomocy tablicy parent.
# Przechodzimy po shortest iteracyjnie od tyłu "usuwając" daną krawędź i jeszcze raz puszczając BFS-a.
# Usuwanie krawędzi polega na przekazaniu do BFS-a tej krawędzi jako argumentu. BFS jeżeli napotka tą krawędź nie przejdzie przez nią.


from zad4testy import runtests
from collections import deque

def BFS(G,s,t,p=(None,None)):
    n=len(G)
    times=[-1 for _ in range(n)]
    parent=[None for _ in range(n)]
    visited=[False for _ in range(n)]
    
    times[s]=0
    visited[s]=True
    queue=deque()
    queue.append(s)

    while queue:
        current=queue.popleft()
        for neighbour in G[current]:
            if not visited[neighbour] and (current,neighbour)!=p and (neighbour,current)!=p:
                times[neighbour]=times[current]+1
                queue.append(neighbour)
                visited[neighbour]=True
                parent[neighbour]=current
                if neighbour==t:
                    return times,parent
                
    return times,parent

def longer( G, s, t ):
    n=len(G)
    times,parent=BFS(G, s, t)
    time = times[t]
    if time == -1:
        return None

    shortest=[t]
    x=t
    while(parent[x]!=s):
        shortest.append(parent[x])
        x=parent[x]
    shortest.append(s)

    
    for i in range(1,len(shortest)):
        p=(shortest[i],shortest[i-1])
        res,par=BFS(G, s, t,p)
        
        if res[t]>time or res[t]==-1:
            return(shortest[i],shortest[i-1])

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )