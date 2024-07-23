t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    arr.sort()

    for _ in range(5):
        if (arr[0] < arr[1]): arr[0] += 1
        elif (arr[1] < arr[2]): arr[1] += 1
        else: arr[2] += 1
    
    mult = 1
    for num in arr:
        mult *= num
    
    print(mult)