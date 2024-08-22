n, m = [int(x) for x in input().split()]
adj = [[] for _ in range(n + 1)]
degrees = [0] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    adj[a].append(b)
    degrees[b] += 1

def dfs(source):
    ans = []
    stack = []
    stack.append(source)
    while len(stack) > 0:
        v = stack.pop()
        if (degrees[v] == 0 and not visited[v]):
            ans.append(v)
        if (not visited[v]):
            visited[v] = True
            for neighbour in adj[v]:
                degrees[neighbour] -= 1
                if (degrees[neighbour] == 0):
                    stack.append(neighbour)
    return ans

ans = []
for i in range(1, n + 1):
    if (degrees[i] == 0):
        ans.extend(dfs(i))

if (len(ans) == n): print(*ans)
else: print("IMPOSSIBLE")