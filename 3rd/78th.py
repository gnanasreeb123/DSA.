import bisect

n=int(input())
a=list(map(int,input().split()))

arr=[]

for x in a:
    bisect.insort(arr,x)

    size=len(arr)

    if size%2==1:
        median=arr[size//2]
    else:
        median=(arr[size//2-1]+arr[size//2])/2

    print(f"{median:.1f}",end=" ")