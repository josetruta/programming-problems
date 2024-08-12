def mod10(number):
    return number % (10**7 + 7)

def power(number, pow):
    res = 1
    while (pow > 0):
        if (pow & 1): res = mod10(res * number)
        number = mod10(number * number)
        pow = pow >> 1
    return mod10(res)

while True:
    n, k = [int(x) for x in input().split()]

    if (n == 0) and (k == 0): break

    res = mod10((mod10(2 * power(n-1, k)) + power(n, k))) + mod10(mod10(2 * power(n-1, n-1)) + power(n, n))

    print(mod10(res))
