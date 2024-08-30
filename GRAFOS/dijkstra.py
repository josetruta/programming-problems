from queue import PriorityQueue

n, m = [int(x) for x in input().split()]
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = [int(x) for x in input().split()]
    adj[a].append((w, b))
    adj[b].append((w, a))

def dijkstra(no):
    q = PriorityQueue()
    dist = [[10**11 + 1, 0] for _ in range(n+1)]

    dist[no] = (0, 0)
    q.put((dist[no][0], no))

    while not q.empty():
        top = q.get()
        for w_vizinho, vizinho in adj[top[1]]:
            if dist[vizinho][0] > dist[top[1]][0] + w_vizinho:
                dist[vizinho] = (dist[top[1]][0] + w_vizinho, top[1])
                q.put((dist[vizinho][0], vizinho))
    
    return dist

# O ERRO ESTÁ NA LÓGICA DO PATH

distancias = dijkstra(1)
print(distancias)
path = []
curr = distancias[n][1]
path.append(n)
path.append(curr)
while curr != 1:
    curr = distancias[curr][1]
    path.append(curr)

for i in range(len(path) - 1, -1, -1):
    print(path[i], end=" ")
