n, x = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]

mod = 10**9 + 7
dp = [0 for _ in range(x+1)]
dp[0] = 1

for i in range(1, x+1):
    for c in coins:
        if c <= i:
            dp[i] += dp[i-c] % mod

print(dp[x] % mod)