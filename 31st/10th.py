n = int(input())
arr = list(map(int, input().split()))

ans = arr[0]

for i in range(n):
    total = 0

    for j in range(i, n):
        total += arr[j]

        # Don't delete anything
        ans = max(ans, total)

        # Delete one element
        for k in range(i, j + 1):
            value = total - arr[k]
            ans = max(ans, value)

print(ans)