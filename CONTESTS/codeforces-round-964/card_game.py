# ERRADO

t = int(input())

for _ in range(t):
    a1, a2, b1, b2 = [int(x) for x in input().split()]
    suneet = 0
    
    if (a1 >= b1) and (a2 > b2): 
        suneet += 1
    if (a1 >= b2) and (a2 > b1):
        suneet += 1
    if (a2 >= b1) and (a1 > b2):
        suneet += 1
    if (a2 >= b2) and (a1 > b1):
        suneet += 1
    
    print(suneet)
    