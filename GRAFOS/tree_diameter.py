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
    queue = deque()
    queue.append((source, 0))
    while len(queue) > 0:
        v = queue.pop()
        if not visited[v[0]]:
            visited[v[0]] = True
            while len(path) <= v[1]: path.append([])
            path[v[1]].append(v[0])
            for w in adj[v[0]]:
                if not visited[w]:
                    queue.append((w, v[1] + 1))
    return path

path = dfs(1)

if (len(path) == 0): print(0)
else:
    distante_1 = path[-1][0]
    path = dfs(distante_1)
    print(len(path) - 1)


