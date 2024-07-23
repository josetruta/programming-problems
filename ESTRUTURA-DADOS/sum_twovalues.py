n, target = list(map(int, input().split()))
seq = list(map(int, input().split()))

seq_dict = {}
out = (None, None)
for i in range(len(seq)):
    diff = target - seq[i]
    if diff < 0:
        continue
    diff_idx = seq_dict.get(diff)
    if diff_idx:
        out = (diff_idx, i + 1)
        break
    if not seq_dict.get(seq[i]): 
        seq_dict[seq[i]] = i + 1

if out[0] == None: print("IMPOSSIBLE")
else: print(*out)
