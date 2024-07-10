n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

c = [a[i] - b[i] for i in range(len(a))]

c.sort()

cont = 0
for i in range(len(c)):
    if (c[i] > 0):
        cont += (n - 1 - i)
    else:
        res = 0
        l, r = i, n - 1
        while (l <= r):
            mid = (l + r) // 2
            if (c[i] + c[mid] > 0):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        if (res != 0) : cont += (n - res)

print(cont)


