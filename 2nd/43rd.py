n=int(input())
arr=list(map(int,input().split()))
s=int(input())
e=int(input())
freq={}
ans=[]
for i in range(s,e):
    if i not in arr:
       ans.append(i)
       if i+1 not in arr:
           ans.append("->"+(i+1))
           i+=1
print(ans)