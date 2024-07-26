from queue import PriorityQueue

t = int(input())

for _ in range(t):
    n = int(input())
    seq = [int(x) for x in input().split()]
    occ = {}

    for i in range(len(seq)):
        if (occ.get(seq[i])):
            occ[seq[i]] += 1
        else:
            occ[seq[i]] = 1
    
    q = PriorityQueue()
    for key in occ:
        q.put(- occ[key])
    
    while q.qsize() >= 2:
        i, j = q.get(), q.get()
        i += 1
        j += 1
        if (i < 0): q.put(i)
        if (j < 0): q.put(j)
    
    if q.qsize() == 0: print(0)
    else: print(- q.get())
