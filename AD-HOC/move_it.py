n = int(input())

boxes = [0 for i in range(n)]

pos = list(map(int, input().split()))
itens = list(map(int, input().split()))

custo = 0
for i in range(len(itens)):
    item = itens[i]
    caixa = boxes[pos[i] - 1]
    if (item >= caixa):
        boxes[pos[i] - 1] = item
        custo += caixa
    else:
        custo += item

print(custo)