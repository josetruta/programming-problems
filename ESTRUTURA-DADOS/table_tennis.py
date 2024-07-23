# EM ANDAMENTO

n, k = [int(x) for x in input().split()]
players = [int(x) for x in input().split()]

if k > len(players): print(max(players))
else:
    for i in range(len(players)):
        wins = True
        for j in range(i - 1, i + k + 1):
            if j < 0: continue
            if j == len(players): break
            if (players[i] < players[j]): 
                wins = False
                break
        if wins: 
            print(players[i])
            break
    