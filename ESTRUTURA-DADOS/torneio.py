t = int(input())

for _ in range(t):
    n, q = [int(x) for x in input().split()]
    atl = [int(x) for x in input().split()]

    vitorias = {}
    rod = 0
    l, r = 0, 1
    while r < len(atl):
        if (not vitorias.get(l)): vitorias[l] = [rod, None]
        if (not vitorias.get(r)): vitorias[r] = [rod, None]
        if (atl[l] > atl[r]):
            vitorias[r][1] = rod
            r += 1
        else:
            vitorias[l][1] = rod
            l = r
            r += 1
        rod += 1

    for _ in range(q):
        i, k = [int(x) for x in input().split()]
        i -= 1

        ini, fim = vitorias[i]
        if (k < ini): print(0)
        elif (fim == None) or (k < fim): print(k - ini)
        else: print(fim - ini)