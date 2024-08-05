t = int(input())

for _ in range(t):
    n = int(input())
    fat = []
    interval = []
    long_interval = 0

    for i in range(1, 10000):
        if (n % i == 0):
            if (len(interval) == 0): interval.append(i)
            elif (interval[-1] == i-1): interval.append(i)
            else:
                long_interval = max(long_interval, len(interval))
                interval = []
            fat.append(i)
            fat.append(n//i)
    
    long_interval = max(long_interval, len(interval))
    print(long_interval)