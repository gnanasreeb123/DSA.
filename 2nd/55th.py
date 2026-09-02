s=input()
stack=[]
for ch in s:
    if stack and stack[-1]==ch:
        stack.pop()
    else:
        stack.append(ch)
if stack:
    print(''.join(stack))
else:
    print("EMPTY")