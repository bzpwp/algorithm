n,m = map(int,input().split())
ls = list(map(int,input().split()))

dp = [[10**18 for _ in range(n+1)] for _ in range(m)]
dp[0][0] = 0 

for i in range(m):
    c = ls[i]
    for j in range(n+1):
        if dp[i][j] >= 0:
            if j+c <= n:
                dp[i][j+c] = min(dp[i][j] + 1, dp[i][j+c])
            if i <= m-2:
                dp[i+1][j] = dp[i][j]
print(dp[-1][-1])