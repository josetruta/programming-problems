# EM ANDAMENTO

t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    
    out = [[0] * (n//k)] * (n//k)
    icol = 0
    for i in range(n):
        row = list(input())
        if (i % k == 0):
            irow = 0
            for j in range(len(row)):
                if (j % k == 0):
                    out[irow][icol] = row[j]
                    irow += 1
            icol += 1
    
    for row in out:
        print(*row)
                