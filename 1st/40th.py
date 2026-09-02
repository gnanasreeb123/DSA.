n,W=map(int,input().split())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))

best=0
bestmask=0

for mask in range(1<<n):
    weight=0
    value=0

    for i in range(n):
        if mask&(1<<i):
            weight+=wt[i]
            value+=val[i]

    if weight<=W and value>best:
        best=value
        bestmask=mask

print(best)

for i in range(n):
    if bestmask&(1<<i):
        print(i,end=" ")