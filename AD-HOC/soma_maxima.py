n = int(input())
seq = [int(x) for x in input().split()]

soma_maxima = float("-inf")
soma_atual = 0

for i in range(len(seq)):
    soma_atual = max(seq[i], soma_atual + seq[i])
    soma_maxima = max(soma_maxima, soma_atual)

print(soma_maxima)