n=int(input())
a=list(map(int,input().split()))

ans=0

for i in range(n):
    mn=a[i]

    for j in range(i,n):
        mn=min(mn,a[j])
        area=mn*(j-i+1)
        ans=max(ans,area)

print(ans)