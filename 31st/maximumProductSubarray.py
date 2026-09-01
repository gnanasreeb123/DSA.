n=int(input())
arr=list(map(int,input().split()))
ans=arr[0]
for i in range(n):
    prod=1
    for j in range(i,n):
        prod*=arr[j]
        ans=max(ans,prod)
print(ans)
    