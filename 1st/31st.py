n,k=map(int,input().split())
a=list(map(int,input().split()))

ans=[]

for i in range(n-k+1):
    mx=a[i]
    for j in range(i,i+k):
        mx=max(mx,a[j])
    ans.append(mx)

print(*ans)