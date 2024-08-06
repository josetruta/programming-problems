t = int(input())

def mod10(number):
    return number % 10

def power(number, pow):
    res = 1
    while (pow > 0):
        if (pow & 1): res = mod10(mod10(res) * mod10(number))
        number = mod10(mod10(number) * mod10(number))
        pow = pow >> 1
    return res

for _ in range(t):
    a, b = [int(x) for x in input().split()]
    res = power(mod10(a), b)
    print(str(res)[-1])
    
    