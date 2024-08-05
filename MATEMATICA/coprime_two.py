n, m = [int(x) for x in input().split()]
seq = [int(x) for x in input().split()]

fat = {}

for num in seq:
    if (num > 1) and (num <= m): fat[num] = 1
    i = 2
    while (i * i <= num) and (i <= m):
        if (num % i == 0):
            if (not fat.get(i)):
                for j in range(i, m+1, i):
                    fat[j] = True
            if (not fat.get(num//i)):
                k = num//i
                for j in range(k, m+1, k):
                    fat[j] = True
        i += 1


print(m - len(fat))
for i in range(1, m + 1):
    if (fat.get(i) == None): print(i)