from queue import PriorityQueue
import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
adj_1 = [[] for _ in range(n + 1)]
adj_2 = [[] for _ in range(n + 1)]
edges = []

for _ in range(m):
    a, b, w = [int(x) for x in input().split()]
    adj_1[a].append((w, b))
    adj_2[b].append((w, a))
    edges.append(((a, b), w))

def dijkstra(adj, no):
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

dist_origem1 = dijkstra(adj_1, 1)
dist_origemN = dijkstra(adj_2, n)

menor_custo = 10**18 + 1
for e in edges:
    u, v = e[0]
    w = e[1]
    menor_custo = min(menor_custo, dist_origem1[u][0] + dist_origemN[v][0] + w//2)

print(menor_custo)
