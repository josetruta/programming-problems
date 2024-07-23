while True:
    user_input = [int(x) for x in input().split()]
    n = user_input[0]

    if n == 0: break

    seq = user_input[1:]

    max_area = 0
    stack = []
    for i in range(len(seq)):
        if (len(stack) == 0) or (stack[-1][1] <= seq[i]):
            stack.append((i, seq[i]))
        else:
            prev_idx = 0
            while (len(stack) != 0) and (stack[-1][1] > seq[i]):
                max_area = max(max_area, stack[-1][1] * (i - stack[-1][0]))
                prev_idx = stack[-1][0]
                stack.pop()
            stack.append((prev_idx, seq[i]))
    
    for item in stack:
        max_area = max(max_area, item[1] * (len(seq) - item[0]))
    
    print(max_area)
