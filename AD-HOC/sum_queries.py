n, q = list(map(int, input().split()))

seq = [int(x) for x in input().split()]

sum = [0]
for i in range(0, len(seq)):
    sum.append(seq[i] + sum[i])

for i in range(q):
    a, b = list(map(int, input().split()))
    print(sum[b] - sum[a-1])