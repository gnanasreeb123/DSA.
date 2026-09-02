n=int(input())
arr=list(map(int,input().split()))
ans=[]
for i in range(n):
    count=1
    j=i-1
    while j>=0 and arr[j]<=arr[i]:
        count+=1
        j-=1
    ans.append(count)
print(*ans)





n=int(input())
arr=list(map(int,input().split()))
stack=[]
ans=[0]*n
for i in range(n):
    while stack and arr[stack[-1]]<=arr[i]:
        stack.pop()
    if stack:
        ans[i]=i-stack[-1]
    else:
        ans[i]=i+1
    stack.append(i)
print(*ans)