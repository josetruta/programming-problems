class UnionFind:
    def __init__(self, n):
        self.Parent = list(range(n))
        self.Size = [1 for _ in range(n)]
    
    # Path compression
    def find_set(self, v):
        if (v != self.Parent[v]):
            self.Parent[v] = self.find_set(self.Parent[v])
        return self.Parent[v]

    # Union by size
    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if (a == b): return
        a_size = self.Size[a]
        b_size = self.Size[b]
        if (a_size < b_size):
            self.Parent[a] = b
            self.Size[b] += self.Size[a]
        else:
            self.Parent[b] = a
            self.Size[a] += self.Size[b]
    
    # Minimum spanning tree
    def kruskal_mst(self, graph):
        result = []
        minimum_cost = 0
        for e in graph:
            u, v, w = e
            a = self.find_set(u)
            b = self.find_set(v)
            if (a != b):
                result.append(e)
                minimum_cost += w
                self.union_sets(a, b)
        return result, minimum_cost



while True:
    m, n = [int(x) for x in input().split()]
    
    if (m == 0) and (n == 0): break

    adj = []
    total_weight = 0
    for _ in range(n):
        u, v, w = [int(x) for x in input().split()]
        total_weight += w
        adj.append((u, v, w))
    
    adj = sorted(adj, key=lambda item: item[2])
    
    unionFind = UnionFind(m)
    _, min_cost = unionFind.kruskal_mst(adj)

    print(total_weight - min_cost)
    