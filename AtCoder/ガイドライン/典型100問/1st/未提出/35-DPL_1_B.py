n,W = map(int,input().split())

dp = [[-1 for _ in range(W+1)] for __ in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
    v,w = map(int,input().split())
    for j in range(W+1):
        if j-w>=0:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
        else:
            dp[i][j]=dp[i-1][j]

ans = 0
for i in range(W+1):
    ans = max(dp[n][i],ans)

print(ans)