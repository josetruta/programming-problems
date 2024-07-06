first_input = list(map(int, input().split()))
n, q = first_input[0], first_input[1]

matriz = list(map(int, input().split()))

zeros, uns = 0, 0
for num in matriz:
    if num == 0: zeros += 1
    else: uns += 1

for i in range(q):
    second_input = list(map(int, input().split()))
    t = second_input[0]

    if (t == 1):
        x = second_input[1] - 1
        matriz[x] = 1 - matriz[x]
        if (matriz[x] == 0): 
            uns -= 1
            zeros += 1
        else:
            uns += 1
            zeros -= 1
    else:
        k = second_input[1] - 1
        if (k < uns): print(1)
        else: print(0)
