n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = {}

for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

values = list(freq.keys())

values.sort(key=lambda x: (-freq[x], x))

print(*values[:k])