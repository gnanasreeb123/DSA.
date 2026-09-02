n,k=map(int,input().split())
a=list(map(int,input().split()))

d=[]

for i in range(n):
    for j in range(i+1,n):
        d.append(abs(a[i]-a[j]))

d.sort()

print(d[k-1])