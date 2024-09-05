import sys
from queue import PriorityQueue

n, m, t, k, p = [int(x) for x in input().split()]

pinheiros = set(map(int, input().split()))
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = [int(x) for x in input().split()]
    adj[a].append((w if b not in pinheiros else w + t, b))
    adj[b].append((w if a not in pinheiros else w + t, a))
    
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

distancias = dijkstra(1)
print(distancias)
curr = distancias[n][1]
if curr == 0:
    print(-1)
    sys.exit(0)
tempo = 0
path = []
path.append(n)
tempo += distancias[n][0]
path.append(curr)
tempo += distancias[curr][0]
while curr != 1:
    curr = distancias[curr][1]
    if curr == 0:
        print(-1)
        sys.exit(0)
    path.append(curr)
    tempo += distancias[curr][0]

for i in range(len(path) - 1, -1, -1):
    print(path[i], end=" ")

print()
print(tempo)