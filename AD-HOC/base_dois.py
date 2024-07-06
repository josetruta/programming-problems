sequencia = list(map(int, input().split()))

soma = 0
for i in range(len(sequencia)):
    soma += (sequencia[i] * (2 ** i))

print(soma)