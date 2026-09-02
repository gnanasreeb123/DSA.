n,amount=map(int,input().split())
coins=list(map(int,input().split()))

INF=amount+1
dp=[INF]*(amount+1)
dp[0]=0

for x in range(1,amount+1):
    for c in coins:
        if c<=x:
            dp[x]=min(dp[x],dp[x-c]+1)

print(-1 if dp[amount]==INF else dp[amount])