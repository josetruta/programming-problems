from collections import deque
 
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
    queue.append(source)
    while len(queue) > 0:
        v = queue.popleft()
        if (visited[v]):
            return v
        visited[v] = True
        for neighbour in adj[v]:
            if not visited[neighbour] and len(adj[neighbour]) > 1:
                queue.append(neighbour)
    
    return -1
 
def dfs(source, visited):
    stack = [(source, 0)]
    cycle = []
    while len(stack) > 0:
        v = stack[-1][0]
        if not visited[v]:
            visited[v] = True
            for neighbour in adj[v]:
                if not visited[neighbour] and (len(adj[neighbour]) > 1):
                    stack.append((neighbour, v))
        else:
            v = stack.pop()
            if (len(cycle) == 0):
                cycle.append(v)
            else:
                if (cycle[-1][1] == v[0]):
                    cycle.append(v)
    return cycle           
 
 
visited = [False for _ in range(n+1)]
vertice = has_cycle(token, visited)
 
if (vertice == -1): print("IMPOSSIBLE")
else:
    visited = [False for _ in range(n+1)]
    cycle = dfs(vertice, visited) 
    cycle.append((cycle[0][0], 0))
    print(len(cycle))
    for par in cycle:
        print(par[0], end=" ")


