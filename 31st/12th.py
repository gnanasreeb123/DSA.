n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

for i in range(n):
    s = set()

    for j in range(i, n):
        s.add(arr[j])

        if len(s) <= k:
            ans = max(ans, j - i + 1)
        else:
            break

print(ans)