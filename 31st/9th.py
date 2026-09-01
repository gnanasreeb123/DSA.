n = int(input())
arr = list(map(int, input().split()))
repeated = -1
missing = -1
for x in range(1, n + 1):
    count = 0
    for y in arr:
        if x == y:
            count += 1
    if count == 2:
        repeated = x
    if count == 0:
        missing = x
print(repeated, missing)