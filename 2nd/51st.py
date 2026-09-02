n=int(input())
arr=list(map(int,input().split()))
ans=[]
for i in range(n):
    x=-1
    for j in range(i+1,n):
        if arr[j]>arr[i]:
            x=arr[j]
            break
    ans.append(x)
print(*ans)
            