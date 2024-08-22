import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
mat = []
visited = [[False] * m for _ in range(n)]

for i in range(n):
    mat.append(input())

def isValid(i, j):
    if (i < 0) or (i >= n): return False
    if (j < 0) or (j >= m): return False
    if (mat[i][j] == "#"): return False
    if (visited[i][j]): return False
    return True

def dfs(i, j):
    stack = []
    stack.append((i, j))
    while len(stack) > 0:
        v = stack.pop()
        i, j = v
        if (not visited[i][j]):
            visited[i][j] = True
        movs = [(-1,0), (0,1), (1,0), (0,-1)]
        for x, y in movs:
            new_i = i + x
            new_j = j + y
            if (isValid(new_i, new_j)):
                stack.append((new_i, new_j))

cont = 0
for i in range(n):
    for j in range(m):
        if (mat[i][j] == '.') and (not visited[i][j]):
            cont += 1
            dfs(i, j)

print(cont)