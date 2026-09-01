n=int(input())
arr=list(map(int,input().split()))
ans=arr[0]
for i in range(n):
    total=0
    for j in range(n):
        index=(i+j)%n
        total+=arr[index]
        ans=max(ans,total)
print(ans)