n = int(input())
arr = list(map(int, input().split()))
ans = []
for x in arr:
    if x not in ans:
        count=0
        for y in arr:
            if x==y:
                count+=1
        if count>n//3:
            ans.append(x)
ans.sort()
if len(ans)==0:
    print(-1)
else:
    print(*ans)