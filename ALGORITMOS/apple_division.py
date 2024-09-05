n = int(input())
weights = [int(x) for x in input().split()]
total_sum = sum(weights)

out = float("-inf")

def solve(idx, sum_1, total_sum):
    global out
    global n
    if (idx == n): 
        out = min(out, abs(sum_1 - (total_sum - sum_1)))
        return
    solve(idx + 1, sum_1 + weights[idx], total_sum)
    solve(idx + 1, sum_1, total_sum)

solve(0, 0, total_sum)
print(out)