t = int(input())

for _ in range(t):
    n = int(input())
    
    cont = 0
    cont += (n // 4)
    cont += ((n % 4) // 2)
    
    print(cont)