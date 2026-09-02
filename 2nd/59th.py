n= int(input())
arr=[]
for i in range(n):
    j=int(input())
    a =list(map(int,input().split()))
    arr+=a
arr.sort()
print(*arr)