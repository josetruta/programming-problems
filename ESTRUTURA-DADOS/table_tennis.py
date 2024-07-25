n, k = [int(x) for x in input().split()]
players = [int(x) for x in input().split()]

if k > len(players): print(max(players))
else:
    for i in range(len(players)):
        wins = True
        m = k
        if (i > 0) and (players[i] > players[i - 1]): m -= 1
        for j in range(i, i + m + 1):
            if j == len(players): break
            if (players[i] < players[j]): 
                wins = False
                break
        if wins: 
            print(players[i])
            break
    