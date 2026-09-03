n=int(input())
a=list(map(int,input().split()))

def height(i):
    if i>=n or a[i]==-1:
        return 0

    left=height(2*i+1)
    right=height(2*i+2)

    if abs(left-right)>1:
        return -1000000

    return max(left,right)+1

if height(0)<0:
    print("NO")
else:
    print("YES")