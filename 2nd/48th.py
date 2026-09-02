s=input()
freq={}
for i in range(len(s)):
    if s[i] not in freq:
        freq[s[i]]=1
    else:
        freq[s[i]]+=1
for value,count in freq.items():
    print(value,count,sep="",end="")