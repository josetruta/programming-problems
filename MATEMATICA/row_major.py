t = int(input())

for _ in range(t):
    n = int(input())
    out = ""
    max = 1
    while (max < n) and (n % max == 0): max += 1
    i_max = 0
    for i in range(n):
        i_max = i_max % max
        print(chr(i_max + 97), end="")
        i_max += 1
    print()