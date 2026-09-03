n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
rows=set()
cols=set()
for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            rows.add(i)
            cols.add(j)
for i in range(n):
    for j in range(m):
        if i in rows or j in cols:
            a[i][j]=0
for row in a:
    print(*row)