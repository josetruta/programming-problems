from math import sqrt

t = int(input())

for _ in range(t):
    n = int(input())
    a = 1
    b = n - 1
    for num in range(2, int(sqrt(n)) + 1):
        if (n % num == 0):
            a = max(a, n // num)
            b = n - a
    print(a, b)
    