n = int(input())
mat = []

for _ in range(n):
    mat.append(list(input()))

dp = [[0] * n for _ in range(n)]
mod = 10**9 + 7

for i in range(n):
    if mat[i][0] == "*": break
    dp[i][0] = 1

for j in range(n):
    if mat[0][j] == "*": break
    dp[0][j] = 1

for i in range(1, n):
    for j in range(1, n):
        if mat[i][j] == "*": dp[i][j] = 0
        else: dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod

print(dp[n-1][n-1])