s=input()
p=input()

ans=[]
n=len(s)
m=len(p)

for i in range(n-m+1):
    j=0
    while j<m and s[i+j]==p[j]:
        j+=1
    if j==m:
        ans.append(i)

print(len(ans))
if ans:
    print(*ans)
else:
    print(-1)