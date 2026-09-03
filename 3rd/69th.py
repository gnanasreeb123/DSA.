n=int(input())
a=list(map(int,input().split()))
ans=[]
left=0
right=n-1
while left<=right:
    if left==right:
        ans.append(a[left])
    else:
        ans.append(a[left])
        ans.append(a[right])
    left+=1
    right+=1
print(*ans)