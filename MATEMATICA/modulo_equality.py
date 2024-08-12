# EM ANDAMENTO

n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort()
b.sort()

flag = 0
for i in range(0, len(a) - 1):
    if (a[i] != b[i]):
        flag = (b[i] - a[i]) % m
        break

print(flag)