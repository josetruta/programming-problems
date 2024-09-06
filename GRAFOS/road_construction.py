import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.Parent = list(range(n+1))
        self.Size = [1 for _ in range(n+1)]
        self.Largest = 0
        self.NumberOfSets = n
    
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
            self.Largest = max(self.Largest, self.Size[b])
            self.NumberOfSets -= 1
        else:
            self.Parent[b] = a
            self.Size[a] += self.Size[b]
            self.Largest = max(self.Largest, self.Size[a])
            self.NumberOfSets -= 1

n, m = [int(x) for x in input().split()]
unionFind = UnionFind(n)

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    unionFind.union_sets(a, b)
    print(unionFind.NumberOfSets, unionFind.Largest, sep = " ")
    

            

