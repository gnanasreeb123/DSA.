class Solution(object):
    def longestPalindrome(self,S):
        n=len(S)
        best=0
        ans=""
        for i in range(n):
            l=r=i
            while l>=0 and r<n and S[l]==S[r]:
                if r-l+1>best:
                    best=r-l+1
                    ans=S[l:r+1]
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<n and S[l]==S[r]:
                if r-l+1>best:
                    best=r-l+1
                    ans=S[l:r+1]
                l-=1
                r+=1
        return ans
S=input().strip()
print(Solution().longestPalindrome(S))


s=input()
n=len(s)
ans=""

for i in range(n):
    for j in range(i,n):
        sub=s[i:j+1]
        if sub==sub[::-1]:
            if len(sub)>len(ans):
                ans=sub
print(ans)