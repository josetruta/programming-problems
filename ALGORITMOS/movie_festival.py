n = int(input())

filmes = []
for _ in range(n):
    start, end = [int(x) for x in input().split()]
    filmes.append((end, start))

filmes.sort()

cont = 1
prev_end = filmes[0][0]
for i in range(1, len(filmes)):
    if (filmes[i][1] >= prev_end):
        prev_end = filmes[i][0]
        cont += 1

print(cont)