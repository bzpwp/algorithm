"""
コイン問題(各種無限個)
各値段に要する最小のコイン枚数
"""
n,m = map(int,input().split())
ls = list(map(int,input().split()))

dp = [[float("inf") for _ in range(n+1)] for __ in range(m+1)]
dp[0][0]=0

for i in range(m):
    c = ls[i]
    for j in range(n+1):
        if j-c>=0:
            dp[i+1][j] = min(dp[i][j],dp[i+1][j-c]+1)
        else:
            dp[i+1][j] = dp[i][j]

ans = float("inf")
for i in range(m+1):
    ans = min(ans,dp[i][n])

print(ans)