from math import gcd

n = int(input())
mat = [int(x) for x in input().split()]
out = []
out.append(mat[0])

for i in range(1, n):
    if (gcd(mat[i], out[-1]) > 1):
        out.append(1)
    out.append(mat[i])

print(len(out) - n)
print(*out)