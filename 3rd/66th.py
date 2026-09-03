l=int(input())
a=list(map(int,input().split()))
n=int(input())
index=l-n
a.pop(index)
print(*a)