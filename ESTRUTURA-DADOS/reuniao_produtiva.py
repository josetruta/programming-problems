from queue import PriorityQueue

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    pq = PriorityQueue()
    for i in range(len(arr)):
        if arr[i] != 0:
            pq.put([- arr[i], i + 1])
    
    ans = []
    while pq.qsize() >= 2:
        i, j = pq.get(), pq.get()
        ans.append([i[1], j[1]])
        i[0] += 1
        j[0] += 1
        if (i[0] < 0): pq.put(i)
        if (j[0] < 0): pq.put(j)

    print(len(ans))
    for a in ans:
        print(a[0], a[1])