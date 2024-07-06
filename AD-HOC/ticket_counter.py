entrada = list(map(int, input().split()))
n, a = entrada[0], entrada[1]

fila = list(map(int, input().split()))

tempo_decorrido = []
tempo_decorrido.append(fila[0] + a)
print(tempo_decorrido[0])

for i in range(1, len(fila)):
    if (fila[i] < tempo_decorrido[i-1]):
        tempo = tempo_decorrido[i-1] + a
    else:
        tempo = fila[i] + a
    tempo_decorrido.append(tempo)
    print(tempo)
