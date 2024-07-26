# EM ANDAMENTO

t = int(input())

for _ in range(t):
    n, q = [int(x) for x in input().split()]
    atl = [int(x) for x in input().split()]

    rodadas = {}
    rod = 0
    l, r = 0, 1
    maior = 0
    while r < len(atl):
        if (atl[l] > atl[r]):
            rodadas[rod] = l
            r += 1
            maior = max(maior, atl[l])
            if maior == atl[l]: idx_maior = l
        else:
            rodadas[rod] = r
            l = r
            maior = max(maior, atl[r])
            if maior == atl[r]: idx_maior = r
            r += 1
        rod += 1

    for _ in range(q):
        i, k = [int(x) for x in input().split()]
        i -= 1

        cont = 0
        for j in range(min(k, len(rodadas))):
            winner = rodadas[j]
            if atl[winner] == maior:
                if winner != i: break
                else:
                    cont += (k - j)
                    break
            if winner == i: cont += 1 
        print(cont)       
