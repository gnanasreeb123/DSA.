s=input()
ans=0
left=0
str=set()
for right in range(len(s)):
    while s[right] in str:
        str.remove(s[right])
        left+=1
    str.add(s[right])
    ans=max(ans,right-left+1) 
print(ans)