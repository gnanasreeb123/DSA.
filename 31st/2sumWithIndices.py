n=int(input())
t=int(input())
lst=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if lst[i]+lst[j]==t:
            print(i,j)