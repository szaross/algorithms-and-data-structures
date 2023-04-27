from collections import deque


# czy graf jest dwudzielny?
# kolorujemy graf dwoma kolorami
# jezeli kolory obok siebie to nie jest dwudzielny
# reprezentacja macierzowa, kolory maja wartosci True/False
def bfs(E: list[list[bool]]):
    n=len(E)
    colouring = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]

    colour=True
    queue=deque()
    current=0
    colouring[current]=colour
    colour = not colour

    for i in range(n):
        if E[0][i] != False and not visited[i]:
            queue.append(i)
    
    while queue:
        current=queue.popleft()
        if not visited[current]:
            colouring[current]=colour
            visited[current]=True
        #print(colouring)
        for i in range(n):
            if E[current][i] != False:
                if not visited[i]:
                    queue.append(i)
                elif colouring[i] == colouring[current]:
                    print(f'{current} {i}')
                    return False

        colour = not colour
    
    return True

# E=[
#     [False,True,True,True],
#     [False,False,False,True],
#     [False,False,False,True],
#     [False,False,False,False]
# ]
# print(bfs(E))



# ile jest spójnych składowych w grafie

# dfs_visit wierzcholek 0; jezeli jakis wierzcholek nie zostal jeszcze odwiedzony to spojne skladowe+=1; dfs_visit ten wierzcholek...
# macierz jako listy sasiedztwa
def dfs_visit(E,visited,v):
        stack=deque()
        stack.append(v)
        while stack:
            current=stack.pop()
            visited[current]=True
            for u in E[current]:
                if visited[u]==False:
                    stack.append(u)

def dfs_components(E: list[list[int]], n):
    visited=[False for _ in range(n)]
    components=1
    queue=deque()
            
    queue.append(0)
    while queue:
        current = queue.popleft()
        dfs_visit(E,visited,current)

        for i in range(n):
            if visited[i]==False:
                components+=1
                queue.append(i)
                break

    return components

A=[
    [1,2],
    [0,3],
    [0,3],
    [1,2],
    [5],
    [4],
    []
]
print(dfs_components(A, 7))


E=[
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]

