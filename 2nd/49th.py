s=input()
t=input()
freq1={}
freq2={}
ans="YES"
for i in range(len(s)):
    if s[i] in freq1 and freq1[s[i]]!=t[i]:
        ans="NO"
        break
    if t[i] in freq2 and freq2[t[i]]!=s[i]:
        ans="NO"
        break
    freq1[s[i]]=t[i]
    freq2[t[i]]=s[i]
print(ans)