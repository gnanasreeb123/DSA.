n=int(input())
a=list(map(int,input().split()))

m=int(input())
b=list(map(int,input().split()))

i=0
j=0

while i<n and j<m:

    if a[i]==b[j]:
        print(a[i])
        break

    if a[i]<b[j]:
        i+=1
    else:
        j+=1

else:
    print(-1)