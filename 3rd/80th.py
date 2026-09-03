n=int(input())

words=[]

for _ in range(n):
    words.append(input().strip())

s=set(words)

best=""

for word in words:

    valid=True

    for i in range(1,len(word)+1):
        if word[:i] not in s:
            valid=False
            break

    if valid:
        if len(word)>len(best):
            best=word
        elif len(word)==len(best) and word<best:
            best=word

if best=="":
    print(-1)
else:
    print(best)