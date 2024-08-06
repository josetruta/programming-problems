t = int(input())

for _ in range(t):
    num = int(input())
    uni = (num % 10**1) // 10**0
    dez = (num % 10**2) // 10**1
    print(uni + dez)