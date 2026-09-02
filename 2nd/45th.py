n=int(input())
arr=list(map(int,input().split()))
ans=[]
s=0
e=n-1
while s<=e :
    ans.append(arr[e])
    if e!=s:
        ans.append(arr[s])
    s+=1
    e-=1
print(ans)