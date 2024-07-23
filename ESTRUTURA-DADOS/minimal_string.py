s = list(input())
t, u = [], ""
abc = [0] * 26

for i in range(len(s)):
    abc[ord(s[i]) - 97] += 1

for i in range(len(s)):
    t.append(s[i])
    abc[ord(s[i]) - 97] -= 1
    while t and sum(abc[:(ord(t[-1]) - 97)]) == 0:
        u += t.pop()
        
print(u)