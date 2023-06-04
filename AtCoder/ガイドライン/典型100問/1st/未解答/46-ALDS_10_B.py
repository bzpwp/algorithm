n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)]

dp = [[10**18 for _ in range(n)]for __ in range(n)]

for i in range(n):
    dp[0][i]=0

for i in range(1,n):
    for j in range(n-i):
        dp[i][j] = min(dp[i-1][j]+ls[j][0]*ls[j+i][0]*ls[j+i][1],dp[i-1][j+1]+ls[j][0]*ls[j][1]*ls[j+i][1])

print(dp[5])