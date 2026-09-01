n=int(input())
arr=list(map(int,input().split()))
ans=[]
for i in range(n):
    product=1
    for j in range(n):
        if i!=j:
            product*=arr[j]
    ans.append(product)
print(*ans)