n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = []

for i in range(n - k + 1):
    window = arr[i:i+k]
    s = set(window)
    ans.append(len(s))

print(*ans)