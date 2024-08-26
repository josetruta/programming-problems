from collections import deque
import sys
sys.setrecursionlimit(10**5 + 1)

n, m = [int(x) for x in input().split()]
 
adj = [[] for _ in range(n + 1)]
token = 0
for i in range(m):
    u, v = [int(x) for x in input().split()]
    if (i == 0): token = u
    adj[u].append(v)
    adj[v].append(u)
 
def has_cycle(source, visited):
    queue = deque()
    queue.append((source,0))
    while len(queue) > 0:
        v = queue.popleft()
        if (visited[v[0]]):
            return v
        visited[v[0]] = True
        for neighbour in adj[v[0]]:
            if not visited[neighbour] and len(adj[neighbour]) > 1:
                queue.append((neighbour, v[0]))
    
    return -1

def dfs(curr, prev, visited, familia):
    visited[curr] = True
    for child in adj[curr]:
        if (child == prev): continue
        if not visited[child]:
            familia[child] = curr  
            return dfs(child, curr, visited, familia)
        return curr, child
 
 
visited = [False for _ in range(n+1)]
vertice = has_cycle(token, visited)

if (vertice == -1): print("IMPOSSIBLE")
else:
    familia = {}
    visited = [False for _ in range(n+1)]
    fim, inicio = dfs(vertice[0], vertice[1], visited, familia)
    ciclo = []
    ciclo.append(inicio)
    ciclo.append(fim)
    curr = fim
    while curr != inicio:
        ciclo.append(familia[curr])
        curr = familia[curr]
    
    print(len(ciclo))
    print(*ciclo)
