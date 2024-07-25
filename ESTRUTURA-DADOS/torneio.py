# EM ANDAMENTO
# LÓGICA FALHA, REPENSAR NO ALGORITMO

t = int(input())

for _ in range(t):
    n, q = [int(x) for x in input().split()]
    atl = [int(x) for x in input().split()]

    for _ in range(q):
        i, k = [int(x) for x in input().split()]
        i -= 1
        str = max(atl)

        if (k > n) and (atl[i] != str): print(0)

        else:
            wins, off = 0, 0
            if (i != 0): off = i - 1
            if (i > 0) and (k > off) and (atl[i - 1] < atl[i]): 
                wins += 1
                off += 1
            if (atl[i] == str): wins += (k - off)
            else:
                for j in range(i + 1, i + 1 + k - off):
                    if (j == len(atl)): break
                    elif (atl[i] > atl[j]): wins += 1
                    else: break
            
            if (wins < 0): wins = 0
            print(wins)
        
