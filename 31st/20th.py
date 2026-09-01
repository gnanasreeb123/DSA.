n = int(input())
prices = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        profit=prices[j]-prices[i]
        ans=max(ans, profit)
print(ans)