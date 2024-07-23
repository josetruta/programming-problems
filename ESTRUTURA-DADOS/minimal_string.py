s = list(input())
copia = [(s[i], i) for i in range(len(s))]
copia.sort()
t, u = [], []

i, idx_menor = 0, 0
while len(u) < len(s):
    if (len(t) == 0):
        t.append(s[i])
        i += 1
    elif (ord(t[-1]) <= ord(copia[idx_menor][0])):
        u.append(t[-1])
        t.pop()
        idx_menor += 1
    elif (copia[idx_menor][1] <= i):
      idx_menor += 1
    elif (i < len(s)):
        t.append(s[i])
        i += 1
    else:
        u.append(t[-1])
        t.pop()
    
    print(u)

print(*u, sep = "")
    