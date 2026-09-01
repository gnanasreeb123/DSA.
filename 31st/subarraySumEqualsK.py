n=int(input())
k=int(input())
arr=list(map(int,input().split()))
ans=0
for i in range (n):
    sum=0
    for j in range(i,n):
        sum+=arr[j]
        if sum==k:
            ans+=1
print(ans)