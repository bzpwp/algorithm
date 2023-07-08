n = int(input())

dp = [[-10**16 for _ in range(n+1)] for _ in range(2)] 
# print(dp)
for i in range(n):
    x,y = map(int,input().split())
    if x == 1:
        dp[0][i+1] = dp[0][i]
        dp[1][i+1] = max(dp[0][i]+y, dp[1][i])
    else:
        dp[1][i+1] = dp[1][i]
        dp[0][i+1] = max(dp[0][i], dp[0][i]+y, dp[1][i]+y)

print(max(dp[0][-1], dp[1][-1]) + 10**16)