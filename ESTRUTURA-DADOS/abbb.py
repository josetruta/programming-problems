t = int(input())

for _ in range(t):
    s = input()
    keeper = [s[0]]
    for i in range(1, len(s)):
        keeper.append(s[i])
        if (s[i] == 'B') and (len(keeper) >= 2): 
            keeper.pop()
            keeper.pop()
    print(len(keeper))
