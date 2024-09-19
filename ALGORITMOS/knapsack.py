from math import ceil

t = int(input())

for _ in range(t):
    n, w = [int(x) for x in input().split()]
    items = [int(x) for x in input().split()]

    sum = 0
    ans = []
    for i in range(n):
        if (items[i] >= ceil(w/2)) and (items[i] <= w):
            ans = [i + 1]
            sum = items[i]
            break
        else:
            sum += items[i]
            if sum > w:
                sum -= items[i]
            else:
                ans.append(i + 1)
                if sum >= ceil(w/2): break
    
    if (sum >= ceil(w/2)):
        print(len(ans))
        print(*ans)
    else:
        print(-1)