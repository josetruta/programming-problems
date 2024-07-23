n = int(input())

conversas = []
for _ in range(n):
    conversas.append(input())

ordem = {}
cont = 0
for i in range(len(conversas) - 1, -1, -1):
    if ordem.get(conversas[i]) != None: continue
    else:
        ordem[conversas[i]] = cont
        cont += 1

listagem = [""] * len(ordem)
for nome in ordem:
    idx = ordem[nome]
    listagem[idx] = nome

for nome in listagem:
    print(nome)
