n=int(input())
strs=[]
group=[]
used=[]
for i in range(n):
    strs.append(input())
for i in range(n):
    if i in used:
        continue
    group=[strs[i]]
    
    for j in range(i+1,n):
        if sorted(strs[i])==sorted(strs[j]):
            group.append(strs[j])
            used.append(j)
    print(*group)           