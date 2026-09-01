n = int(input())
arr = list(map(int, input().split()))

if n <= 2:
    print(n)
else:
    length = 2
    ans = 2
    diff = arr[1] - arr[0]

    for i in range(2, n):
        if arr[i] - arr[i - 1] == diff:
            length += 1
        else:
            length = 2
            diff = arr[i] - arr[i - 1]

        ans = max(ans, length)

    print(ans)