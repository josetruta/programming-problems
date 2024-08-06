t = int(input())

for _ in range(t):
    s = input()
    t = input()
    ans = []
    
    i, j = 0, 0
    flag = False
    while i < len(s):
        ans.append(s[i])
        if (s[i] == t[j]): 
            if (j < len(t) - 1):
                j += 1
            else: flag = True 
        elif (s[i] == "?"):
            ans[i] = t[j]
            if (j < len(t) - 1):
                j += 1
            else: flag = True 
        i += 1
    
    if (not flag): print("NO")
    else: 
        print("YES")
        print(''.join(ans))
            