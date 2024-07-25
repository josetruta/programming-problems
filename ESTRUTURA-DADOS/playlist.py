n = int(input())
k = list(map(int, input().split()))

songs = {}
left, right = 0, 0
maximo = 0
while right < n:
    if (songs.get(k[right]) == None):
        songs[k[right]] = right
        right += 1
    else:
        if (songs[k[right]] >= left):
            left = songs[k[right]] + 1
        songs[k[right]] = right
        right += 1
        
    maximo = max(maximo, right - left)

print(maximo)