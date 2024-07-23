t = int(input())

for _ in range(t):
    n, m, k = list(map(int, input().split()))

    res = []
    for n in range(n, k - 1, -1):
        res.append(n)
    
    for n in range(m + 1, k):
        res.append(n)
    
    for n in range(1, m + 1):
        res.append(n)
    
    print(*res)