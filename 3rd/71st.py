n=int(input())
a=list(map(int,input().split()))
tree=[None]*n
for i in range(n):
    if a[i]!=-1:
        tree[i]=a[i]
stack=[]
ans=[]
i=0
while stack or i<n:
    while i<n and tree[i] is not None:
        stack.append(i)
        i=2*i+1
    if not stack:
        break
    node=stack.pop()
    ans.append(tree[node])
    i=2*node+2
print(*ans)