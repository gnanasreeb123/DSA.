n=int(input())
arr=list(map(int,input().split()))
ans=0
l=[]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        ans=max((arr[j]-arr[i]),ans)
        
    
print(ans)
    
        