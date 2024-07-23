t = int(input())

for _ in range(t):
    n = int(input())
    seq = [int(x) for x in input().split()]
    q = []
    
    for i in range(len(seq)):
        if len(q) == 0:
            q.append(seq[i])
        elif seq[i] != q[-1]:
            q.pop()
        else:
            q.append(seq[i])
    
    print(len(q))
