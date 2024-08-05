t = int(input())

for _ in range(t):
    a, b, c = [int(x) for x in input().split()]
    x = 10 ** (a - 1)
    y = 10 ** (b - 1)
    mdc = 10 ** (c - 1)
    if (min(x, y) == x): x = min(x, y) + mdc
    else: y = min(x, y) + mdc
    print(x, y)