n, k = map(int, input().split())
arr = list(map(int, input().split()))
c =set()
for i in range(n):
    for j in range(i+1,n):
        if abs(arr[i]-arr[j]) == k :
            pair=tuple(sorted((arr[i],arr[j])))
            c.add(pair)
print(len(c))