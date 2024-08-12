n = int(input())
m = int(input())

def mod10(number):
    return number % (10**9 + 7)

def power(number, pow):
    res = 1
    while (pow > 0):
        if (pow & 1): res = res * number
        number = mod10(number * number)
        pow = pow >> 1
    return res

print(m % power(2, n))