input_n = list(map(int, input().split()))
a, b = input_n[0], input_n[1]

cont = 0
for i in range(a, b+1):
    dez_milhar = i // 10000
    i = i % 10000
    uni_milhar = i // 1000
    i = i % 1000
    centena = i // 100
    i = i % 100
    dezena = i // 10
    i = i % 10
    unidade = i

    if (unidade == dez_milhar) and (dezena == uni_milhar): cont += 1

print(cont)