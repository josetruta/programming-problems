testes = int(input())

def soma_acumulada(lista):
    res = [0]
    for i in range(len(lista)):
        res.append(res[i] + lista[i])
    return res

def falso_sort(lista):
    for i in range(1, len(lista)):
        if (lista[i] < lista[i - 1]):
            lista[i] = lista[i - 1]

def busca_binaria(lista, chave):
    inicio, fim = 0, len(lista) - 1
    resposta = -1

    while (inicio <= fim):
        meio = (fim + inicio) // 2 

        if (lista[meio] <= chave):
            resposta = meio
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return resposta      


for i in range(testes):
    degraus, perguntas = list(map(int, input().split()))
    alturas_d = list(map(int, input().split()))
    num_perguntas = list(map(int, input().split()))

    alturas_total = soma_acumulada(alturas_d)
    falso_sort(alturas_d)

    out = []
    for i in range(len(num_perguntas)):
        idx = busca_binaria(alturas_d, num_perguntas[i])
        out.append(str(alturas_total[idx + 1]))
    
    print(' '.join(out))