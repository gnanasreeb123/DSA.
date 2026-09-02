n,k=map(int,input().split())
a=list(map(int,input().split()))

total=sum(a)

if total%k!=0:
    print("NO")
else:
    target=total//k
    s=0
    parts=0

    for x in a:
        s+=x

        if s==target:
            parts+=1
            s=0

    if parts==k:
        print("YES")
    else:
        print("NO")