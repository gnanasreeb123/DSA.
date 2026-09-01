n=int(input())
k=int(input())
arr=list(map(int,input().split()))
ans=0
for i in range(n):
    xor=0
    for j in range(i,n):
        xor^=arr[j]
        if xor==k:
            ans+=1
print(ans)