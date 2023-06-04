n,w = map(int,input().split())
ls = []
for i in range(n):
    ls.append(list(map(int,input().split())))

dp = [[-1]*(n+1) for _ in range(w+1)]

dp[0][0]=0

for i in range(1,n+1):
    w1 = ls[i-1][0]
    v = ls[i-1][1]
    for j in range(w+1):
        if j-w1 >=0:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w1]+v)
        elif dp[i-1][j]>=0:
            dp[i][j] = dp[i-1][j]

z = 0
for k in range(w+1):
    z = max(z, dp[n+1][k])

print(z)