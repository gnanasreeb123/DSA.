n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

def possible(d):
    count=1
    last=a[0]

    for i in range(1,n):
        if a[i]-last>=d:
            count+=1
            last=a[i]
            if count>=k:
                return True
    return False

low=1
high=a[-1]-a[0]
ans=0

while low<=high:
    mid=(low+high)//2

    if possible(mid):
        ans=mid
        low=mid+1
    else:
        high=mid-1

print(ans)