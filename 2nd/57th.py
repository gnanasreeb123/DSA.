n=int(input())
arr=list(map(int,input().split()))
t=int(input())
l=0
r=n-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==t:
        print(mid)
        break
    if arr[l]<=arr[mid]:
        if arr[l]<=t<arr[mid]:
            r=mid-1
        else:
            l=mid+1
    else:
        if arr[mid]<t<=arr[r]:
            l=mid+1
        else:
            r=mid-1
else:
    print(-1)

    