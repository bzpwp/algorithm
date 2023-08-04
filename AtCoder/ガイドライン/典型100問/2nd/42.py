n,m = map(int,input().split())
D = [int(input()) for _ in range(n)]
C = [int(input()) for _ in range(m)]

dp = [[float("inf") for _ in range(n+1)] for _ in range(m+1)]
for i in range(m+1):
    dp[i][0] = 0
for i in range(m):
    c = C[i]
    for j in range(min(i+1,n)):
        d = D[j]
        dp[i+1][j+1] = min(dp[i][j+1], dp[i][j] + c*d)
print(dp[-1][-1])
for i in dp:
    print(i)