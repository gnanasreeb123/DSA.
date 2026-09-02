n=int(input())
arr=list(map(int,input().split()))
freq={}
for i in arr:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
res=[]
for value,count in freq.items():
    res.extend([value]*count)
print(res)
