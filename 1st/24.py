class Solution(object):
    def checkInclusion(self, P, S):
        m=len(P)
        n=len(S)
        if m>n:
            return "NO"
        a=[0]*26
        b=[0]*26
        for c in P:
            a[ord(c)-97]+=1
        for i in range(m):
            b[ord(S[i])-97]+=1
        if a==b:
            return "YES"
        for i in range(m,n):
            b[ord(S[i])-97]+=1
            b[ord(S[i-m])-97]-=1
            if a==b:
                return "YES"
        return "NO"
S=input().strip()
P=input().strip()
print(Solution().checkInclusion(P,S))