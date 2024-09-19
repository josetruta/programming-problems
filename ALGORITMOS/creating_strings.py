from itertools import permutations

n = input()

unique_words = set()
n = sorted(n)

for p in permutations(n):
    unique_words.add(''.join(p))

print(len(unique_words))
unique_words = sorted(unique_words)
print(*unique_words)