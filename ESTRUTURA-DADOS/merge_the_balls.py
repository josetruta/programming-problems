import sys
sys.setrecursionlimit(10**6)

n = int(input())
op = [int(x) for x in input().split()]

def operation(balls):
    if (len(balls) == 1): return True
    elif (balls[-1] != balls[-2]): return True
    elif (balls[-1] == balls[-2]): 
        new_value = balls[-1] + 1
        balls.pop()
        balls.pop()
        balls.append(new_value)
        return operation(balls)


balls = []
for i in range(n):
    balls.append(op[i])
    operation(balls)

print(len(balls))
