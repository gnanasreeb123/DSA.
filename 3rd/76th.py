n=int(input())
a=list(map(int,input().split()))
k=int(input())

ans=[]

def inorder(i):
    if i>=n or a[i]==-1:
        return

    inorder(2*i+1)
    ans.append(a[i])
    inorder(2*i+2)

inorder(0)

print(ans[k-1])