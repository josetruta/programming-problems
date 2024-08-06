t = int(input())

for _ in range(t):
    n, s, m = [int(x) for x in input().split()]
    ini = 0
    diff = 0
    for _ in range(n):
        l, r = [int(x) for x in input().split()]
        diff = max(diff, l - ini)
        ini = r
    diff = max(diff, m - ini)
    if diff >= s: print("YES")
    else: print("NO")