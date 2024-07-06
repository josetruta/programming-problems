def ehPrimo(num):
    if (num < 2): return False
    for i in range(2, num):
        if (num % i == 0): return False
    return True

n = int(input())

resto = n - 2

if ehPrimo(resto):
    print(2, resto)
else:
    print(-1)