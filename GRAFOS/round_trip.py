import sys
sys.setrecursionlimit(10**6 + 1)
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
 
adj = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)

def dfs(source, prev, visited, parent):
    global inicio, fim
    visited[source] = 1
    for child in adj[source]:
        if (child == prev): continue
        if (visited[child] == 0):
            parent[child] = source 
            dfs(child, source, visited, parent)
            if (inicio): return
        elif (visited[child] == 1):
            fim = source
            inicio = child
            return
    visited[source] = 2
 
visited = [0 for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
inicio = False
fim = False

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i, 0, visited, parent)
    if (inicio): break

if (not inicio): print("IMPOSSIBLE")
else:
    ciclo = []
    u = fim
    ciclo.append(inicio)
    while u != inicio:
        ciclo.append(u)
        u = parent[u]
    ciclo.append(inicio)

    print(len(ciclo))
    print(*ciclo)
