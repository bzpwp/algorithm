n, m = map(int,input().split())
dis = []
for i in range(n):
    dis.append(int(input()))
cli = []
for i in range(m):
    cli.append(int(input()))

dp = [[float("inf") for _ in range(m)] for __ in range(n+1)]

dp[0][0]=0

for i in range(m):
    dp[0][i]=0


for i in range(n):
    for j in range(i+1,m):
        dp[i+1][j]=min(dp[i+1][j-1],dp[i][j-1]+cli[j]*dis[i])

print(min(dp[-1]))