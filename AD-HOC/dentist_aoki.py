entrada = list(map(int, input().split()))
n, q = entrada[0], entrada[1]

treatments = list(map(int, input().split()))
teeths = [1 for teeth in range(n)]

for t in treatments:
    idx = t - 1
    if (teeths[idx] == 1):
        teeths[idx] = 0
        n -= 1
    else:
        teeths[idx] = 1
        n += 1

print(n)