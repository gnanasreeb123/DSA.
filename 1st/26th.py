s=input()
p=input()

m=len(p)
target=sorted(p)
ans=[]

for i in range(len(s)-m+1):
    sub=s[i:i+m]
    if sorted(sub)==target:
        ans.append(i)

print(len(ans))
if ans:
    print(*ans)
else:
    print(-1)