'''

for i in range(n):
    max=arr[i]
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            max=arr[i]
    ans.append(max)
            
print(ans)'''
n=int(input())
arr=list(map(int,input().split()))
ans=[]

for i in range(n):
    flag=True
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            flag=False
            break
    if flag:
        ans.append(arr[i])
print(*ans)