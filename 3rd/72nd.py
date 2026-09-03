from collections import deque
n=int(input())
a=list(map(int,input().split()))
if n==0 or a[0]==-1:
    exit()
q=deque([0])
l_to_r=True
while q:
    level=[]
    for _ in range(len(q)):
        i=q.popleft()
        if a[i]!=-1:
            level.append(a[i])
            l=2*i+1
            r=2*i+2
            if l<n and a[l]!=-1:
                q.append(l)
            if r<n and a[r]!=-1:
                q.append(r)
    if not l_to_r:
        level.reverse()
    print(*level)
    l_to_r=not l_to_r 