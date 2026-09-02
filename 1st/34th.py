n=int(input())
ans=[]

def valid(s):
    bal=0
    for c in s:
        if c=="(":
            bal+=1
        else:
            bal-=1
        if bal<0:
            return False
    return bal==0

def generate(s):
    if len(s)==2*n:
        if valid(s):
            ans.append(s)
        return
    generate(s+"(")
    generate(s+")")

generate("")

print(*ans,sep="\n")