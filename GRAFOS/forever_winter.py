t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().split()]
    nodes = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = [int(x) for x in input().split()]
        nodes[u].append(v)
        nodes[v].append(u)
    
    externo = []
    vizinhos = set()
    for i in range(1, len(nodes)):
        if (len(nodes[i]) == 1): 
            externo.append(i)
            vizinhos.add(nodes[i][0])

    x = len(vizinhos)
    y = len(externo) // x
    print(x, y)
