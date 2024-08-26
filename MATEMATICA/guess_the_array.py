n = int(input())

x = int(input("? 1 2\n"))
y = int(input("? 1 3\n"))
z = int(input("? 2 3\n"))

a = (x + y - z) // 2
b = x - a
c = y - a

res = [a, b, c]

for i in range(3, n):
    value = int(input("? 1 " + str(i + 1) + "\n"))
    res.append(value - a)

print("!", *res)