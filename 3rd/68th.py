n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
i=n-1
j=m-1
carry=0
ans=[]
while i>=0 or j>=0 or carry:
    x=a[i] if i>=0 else 0
    y=b[j] if j>=0 else 0
    total=x+y+carry
    ans.append(total%10)
    carry=total//10
    i-=1
    j-=1
ans.reverse()
print(*ans)