n = int(input())
dp = [[-10**18]*5 for i in range(n+1)]

dp[0][0]=0

for i in range(n):
    t,x,a = map(int,input().split())
    if t <= 4:
        for j in range(t):
            dp[0][j+1]=max(0,dp[0][t])
    else:
        for j in range():
            dp[0][j+1]=max(0,dp[0][t])