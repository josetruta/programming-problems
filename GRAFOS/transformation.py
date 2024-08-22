def dfs(source):
    global flag
    if (source > b): return
    if (source == b):
        res.append(source)
        flag = True
        return
    if flag: return
    dfs(source * 2)
    dfs((10 * source) + 1)
    if flag: res.append(source)

a, b = [int(x) for x in input().split()]

res = []
flag = False

dfs(a)

if (len(res) == 0): print("NO")
else:
    print("YES")
    res.sort(reverse=False)
    print(len(res))
    print(*res)