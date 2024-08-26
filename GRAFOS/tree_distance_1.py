from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(1, n):
    u, v = [int(x) for x in input().split()]
    adj[u].append(v)
    adj[v].append(u)

def dfs(source):
    visited = [False for _ in range(n+1)]
    path = [[]]
    distancias = [0 for _ in range(n+1)]
    queue = deque()
    queue.append((source, 0))
    while len(queue) > 0:
        v = queue.pop()
        if not visited[v[0]]:
            visited[v[0]] = True
            while len(path) <= v[1]: path.append([])
            path[v[1]].append(v[0])
            distancias[v[0]] = v[1]
            for w in adj[v[0]]:
                if not visited[w]:
                    queue.append((w, v[1] + 1))
    return path, distancias

def dfs_distancia(source):
    visited = [False for _ in range(n+1)]
    distancias = [0 for _ in range(n+1)]
    queue = deque()
    queue.append((source, 0))
    while len(queue) > 0:
        v = queue.pop()
        if not visited[v[0]]:
            visited[v[0]] = True
            distancias[v[0]] = v[1]
            for w in adj[v[0]]:
                if not visited[w]:
                    queue.append((w, v[1] + 1))
    return distancias

path, distancias_1 = dfs(1)

a = path[-1][0]
path, distancias_a = dfs(a)
b = path[-1][0]

distancias_b = dfs_distancia(b)

distancias_max = [max(distancias_a[i], distancias_b[i]) for i in range(1, n+1)]

if (len(distancias_max) == 0): print(0)
else: print(*distancias_max)