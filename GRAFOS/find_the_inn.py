from queue import PriorityQueue

n, m, t, k, p = [int(x) for x in input().split()]

if p != 0: pinheiros = set(map(int, input().split()))
else: pinheiros = set()
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = [int(x) for x in input().split()]
    w = w * 60
    adj[a].append((w if b not in pinheiros else w + k, b))
    
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
if distancias[n][1] == 0:
    print(-1)
elif distancias[n][0] > t * 60:
    print(-1)
else: print(distancias[n][0])