n,W = map(int,input().split())

dp = [[-1 for _ in range(W+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 0

for i in range(n):
    v,w = map(int,input().split())
    for j in range(W+1):
        if i == 2:
            print("--", i, j)
        if dp[i][j] >= 0:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j + w <= W:
                dp[i+1][j + w] = max(dp[i][j] + v, dp[i+1][j + w])
print(max(dp[-1]))

for i in dp:
    print(i)