def getCusto(inicio, fim, s, letra):
    cont = 0
    for i in range(inicio, fim + 1):
        if (s[i] != letra): cont += 1
    return cont

def ehABoa(inicio, fim, s, letra):
    if (inicio == fim):
        if (s[fim] == letra): return 0
        else: return 1
    meio = int((inicio + fim) / 2)
    return min(getCusto(inicio, meio, s, letra) + ehABoa(meio + 1, fim, s, chr(ord(letra) + 1)),
               getCusto(meio + 1, fim, s, letra) + ehABoa(inicio, meio, s, chr(ord(letra) + 1)))

t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    inicio = 0
    fim = n - 1
    letra = 'a'
    print(ehABoa(inicio, fim, s, letra))
