n=int(input())
a=input().split()
st=[]
for x in a:
    if x not in '+-*/':
        st.append(int(x))
    else:
        b=st.pop()
        c=st.pop()
        if x=='+':
            st.append(c+b)
        elif x=='-':
            st.append(c-b)
        elif x=='*':
            st.append(c*b)
        else:
            st.append(int(c/b))
print(st[-1])