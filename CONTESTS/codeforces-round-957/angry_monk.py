t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))

    pieces = list(map(int, input().split()))
    pieces.sort()

    total = 0
    for i in range(len(pieces) - 1):
        total += (2 * pieces[i] - 1)
    
    print(total)