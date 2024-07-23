n = int(input())

aliases = {}
for _ in range(n):
    user_input = input().split()
    tam = int(user_input[0])

    nome = ""
    for i in range(1, tam + 1):
        nome += user_input[i][0]
    
    if aliases.get(nome): 
        aliases[nome] += 1
    else:
        aliases[nome] = 1

cont = 0
for nome in aliases:
    if aliases[nome] == 1: cont += 1

print(cont)
