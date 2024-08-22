import sys
sys.setrecursionlimit(2*10**5)

n = int(input())

visited = [False for _ in range(n+1)]
chefes = [int(x) for x in input().split()]
adj = [[] for _ in range(n+1)]

# REVER A FORMA QUE ESTOU GUARDANDO AS ADJACENCIAS
for i in range(len(chefes)):
    adj[chefes[i]].append(i + 2)

acc = [0 for _ in range(n+1)]
acc[1] = n - 1
visited[1] = True
    
def dfs(source):
    visited[source] = True
    for neighbour in adj[source]:
        acc[source] += 1
        acc[source] += acc[neighbour]
        if (not visited[neighbour]):
            dfs(neighbour)

for i in range(n, 1, -1):
    if (not visited[i]):
        dfs(i, acc[i])

print(adj)
print(*acc[1:])
    