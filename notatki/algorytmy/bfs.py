from collections import deque

# wierzcholki sa ponumerowane od 0..n-1
# implementacja macierzowa E
# def BFS(E):
#     n=len(E)
#     visited=[False for _ in range(n)]
#     d=[-1 for _ in range(n)]
#     parent=[0 for _ in range(n)]

#     queue=deque()
#     visited[0]=True
#     parent[0]=None
#     d[0]=0
#     queue.append(0)
#     while queue: # is not empty
#         current=queue.pop()
#         for neighbour in range(len(E[current])):
#             if E[current][neighbour] and not visited[neighbour]:
#                 print(f'visiting {neighbour} from {current}')
#                 visited[neighbour]=True
#                 d[neighbour]=d[current]+1
#                 parent[neighbour]=current
#                 queue.append(neighbour)
#     return d,visited,parent


# E=[
#     [None,1,1,None],
#     [None,None,None,1],
#     [None,None,None,1],
#     [None,None,None,None]
# ]


# ----------------------------------------------------------------#
# implementacja listowa
class Node:
    def __init__(self, x, nex=None):
        self.val = x
        self.next = None


def push_back(head, val):
    while head.next != None:
        head = head.next
    head.next = Node(val)


def display(f: Node):
    p = f
    while p != None:
        arrow = "->" if p.next != None else ""
        print(f"{p.val}{arrow}", end="")
        p = p.next
    print()


def BFS(E):
    n = len(E)
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    parent = [0 for _ in range(n)]

    queue = deque()
    visited[0] = True
    parent[0] = None
    d[0] = 0
    queue.append(0)
    while queue:  # is not empty
        current = queue.popleft()
        p = E[current]
        while p is not None:
            if not visited[p.val]:
                neighbour = p.val
                print(f"visiting {neighbour} from {current}")
                visited[neighbour] = True
                d[neighbour] = d[current] + 1
                parent[neighbour] = current
                queue.append(neighbour)
            p = p.next

    return d, visited, parent


E = [None for _ in range(4)]
E[0] = Node(1)
push_back(E[0], 2)
E[1] = Node(3)
E[2] = Node(3)
for el in E:
    if el:
        display(el)


# ----------------------------------------------------------------#


d, v, p = BFS(E)
print("odl:")
print(*d)
print("visited:")
print(*v)
print("parent:")
print(*p)
