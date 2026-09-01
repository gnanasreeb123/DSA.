n=int(input())
arr=list(map(int,input().split()))
s=set(arr)
len=0
ans=0
for x in s:
    if x-1 not in s:
        len=1
    while x+len in s:
        len=len+1
    ans=max(ans,len)
print(ans)