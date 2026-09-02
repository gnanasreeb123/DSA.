s=input()
open=0
ans=0

for c in s:
    if c=='(':
        open+=1
    else:
        if open>0:
            open-=1
        else:
            ans+=1

print(ans+open)