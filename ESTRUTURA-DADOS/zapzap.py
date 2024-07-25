from queue import Queue

n, k = [int(x) for x in input().split()]
cvs = [int(x) for x in input().split()]

q = Queue(k)
current_ids = {}
for cv in cvs:
    if (not q.full()) and (current_ids.get(cv) == None):
        q.put(cv)
        current_ids[cv] = True
    elif (not current_ids.get(cv)):
        current_ids.pop(q.get())
        q.put(cv)
        current_ids[cv] = True

out = []
for _ in range(q.qsize()):
    out.append(q.get())

print(len(out))

for i in range(len(out) - 1, 0, -1):
    print(out[i], end=" ")

print(out[0])
