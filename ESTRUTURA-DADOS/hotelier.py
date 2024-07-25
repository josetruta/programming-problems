n = int(input())
e = input()
rooms = [0] * 10

def findL(arr):
    for i in range(len(arr)):
        if arr[i] == 0: return i

def findR(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0: return i

l, r = 0, 0
for event in e:
    if event == "L":
        rooms[findL(rooms)] = 1
    elif event == "R":
        rooms[findR(rooms)] = 1
    else:
        rooms[int(event)] = 0

print(*rooms, sep="")