n = int(input())

intervals = []

for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

intervals.sort()

ans = []

for start, end in intervals:

    if not ans or start > ans[-1][1]:
        ans.append([start, end])
    else:
        ans[-1][1] = max(ans[-1][1], end)

for start, end in ans:
    print(start, end)