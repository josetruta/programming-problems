# EM ANDAMENTO

n = int(input())
k = list(map(int, input().split()))

songs = {}
maximo, cont = 0, 0
for i in range(n):
    if (songs.get(k[i]) != None):
        cont -= 1
        if cont < 0: cont = 1
        songs[k[i]] = i
    else:
        songs[k[i]] = i
        cont += 1
    maximo = max(maximo, cont)

print(maximo)