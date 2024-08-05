n, k = [int(x) for x in input().split()]
ans = set()

for i in range(1, int(n**(1/2)) + 1):
    if (n % i == 0):
        ans.add(i)
        ans.add(n//i)

ans = sorted(ans)
if len(ans) >= k: print(ans[k - 1])
else: print(-1) 
