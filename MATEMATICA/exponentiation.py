n = int(input())

def mod10(number):
    return number % (10**9 + 7)

def power(number, pow):
    res = 1
    while (mod10(pow) > 0):
        if (mod10(pow) & 1): res = mod10(mod10(res) * mod10(number))
        number = mod10(mod10(number) * mod10(number))
        pow = mod10(pow) >> 1
    return mod10(res)

for _ in range(n):
    a, b = [int(x) for x in input().split()]
    a = mod10(a)
    b = mod10(b)
    print(mod10(power(a, b)))