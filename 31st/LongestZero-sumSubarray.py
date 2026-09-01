n=int(input())
arr=list(map(int,input().split()))
ans=0
for i in range(n):
    total=0
    for j in range(i,n):
        total+=arr[j]
        if total==0:
            ans=max(ans,j-i+1)
print(ans)