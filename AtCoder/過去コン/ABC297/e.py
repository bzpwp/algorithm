n,k = map(int, input().split())
ls = list(map(int,input().split()))

ls.sort()

dp = [[float("inf") for _ in range(k+1)] for __ in range(n)]

for i in range(k+1):
    dp[0][i] = ls[0]*i
for i in range(n-1):
    dp[i+1][0] = 0


for i in range(n-1):
    x = ls[i+1]
    c = 1
    d = 0
    for j in range(k):
        if dp[i][c] < dp[i+1][d] + x:
            dp[i+1][j+1] = dp[i][c]
            c += 1
        elif dp[i][c] > dp[i+1][d] + x:
            dp[i+1][j+1] = dp[i+1][d] + x
            d += 1
        elif dp[i][c] == dp[i+1][d] + x:
            dp[i+1][j+1] = dp[i+1][d] + x
            c += 1
            d += 1

print(dp[-1][-1])
