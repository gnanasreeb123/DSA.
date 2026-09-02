path=input()
stack=[]
for x in path.split('/'):
    if x=='' or x=='.':
        continue
    elif x=='..':
        if stack:
            stack.pop()
    else:
        stack.append(x)
print('/'+'/'.join(stack))