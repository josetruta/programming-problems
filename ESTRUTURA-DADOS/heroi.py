from queue import PriorityQueue

t = int(input())

for _ in range(t):
    n = int(input())
    cards = [int(x) for x in input().split()]

    powers = PriorityQueue()
    acc = 0
    for card in cards:
        if (card != 0):
            powers.put(- card)
        else:
            if not powers.empty():
                acc += (- powers.get())
    
    print(acc)
        