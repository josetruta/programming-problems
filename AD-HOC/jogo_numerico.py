t = int(input())

def thaisWins(lista, k):
    d, t = 0, len(lista) - 1
    for i in range(1, k + 1):
        while (t >= 0) and (lista[t] > (k - i + 1)):
            t -= 1
        t -= 1
        d += 1
    t += 1
    d -= 1
    return t >= d

for _ in range(t):
    n = int(input())
    lista = list(map(int, input().split()))

    lista.sort()

    ans = 0
    for k in range(n, 0, -1):
        if (thaisWins(lista, k)): 
            ans = k
            break
    print(ans)
    

    
