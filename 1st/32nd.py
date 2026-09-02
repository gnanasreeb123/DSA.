s=input()
num=[]
st=[]
cur=""
k=0

for c in s:
    if c.isdigit():
        k=k*10+int(c)
    elif c=='[':
        num.append(k)
        st.append(cur)
        k=0
        cur=""
    elif c==']':
        cur=st.pop()+cur*num.pop()
    else:
        cur+=c

print(cur)