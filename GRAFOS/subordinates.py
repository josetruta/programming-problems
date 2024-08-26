n = int(input())

visited = [False for _ in range(n+1)]
chefes = [int(x) for x in input().split()]
adj = [[] for _ in range(n+1)]

for i in range(len(chefes)):
    adj[chefes[i]].append(i + 2)

acc = [0 for _ in range(n+1)]
    
def dfs(source):
    stack = [source]
    while len(stack) > 0:
        daVez = stack[-1]
        if (not visited[daVez]):
            visited[daVez] = True
            acc[daVez] += len(adj[daVez])
            for neighbour in adj[daVez]:
                if (not visited[neighbour]) and (len(adj[neighbour]) > 0):
                    stack.append(neighbour)
                    
        else:
            daVez = stack.pop()
            for neighbour in adj[daVez]:
                acc[daVez] += acc[neighbour]

dfs(1)

print(*acc[1:])
    