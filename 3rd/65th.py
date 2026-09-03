n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
found=False
for i in range(n):
    mini=min(a[i])
    for j in range(m):
        if a[i][j]==mini:
            largest=True
            for k in range(n):
                if a[k][j]>a[i][j]:
                    largest=False
                    break
            if largest:
                print(a[i][j],i,j)
                found=True
if not found:
    print(-1)