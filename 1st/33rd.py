q=int(input())
st=[]

for _ in range(q):
    x=input().split()

    if x[0]=="PUSH":
        st.append(int(x[1]))
    elif x[0]=="POP":
        st.pop()
    elif x[0]=="TOP":
        print(st[-1])
    else:
        print(min(st))