n,p = map(int,input().split())
M = 998244353
x = 100-p
y = pow(100, -1, M)

dp = [[0 for _ in range(n+1)]for __ in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(i,n):
        z = dp[i][j]*y*x
        v = dp[i][j]*y*p
        if j == n-1:
            dp[i+1][j+1] += (z + v)%M
        else:
            dp[i+1][j+1] += z%M
            dp[i+1][j+2] += v%M

x = 0
for i in range(n+1):
    x += (dp[i][-1]*(i+1))%M
print(x%M-1)