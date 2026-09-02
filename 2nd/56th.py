n=int(input())
arr=list(map(int,input().split()))
x=int(input())
l=0
r=n-1
while arr[l]!=x and l<n:
    l+=1
while arr[r]!=x and r>=0:
    r-=1
print(l,r)