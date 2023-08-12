n = int(input())
ls = list(map(int,input().split()))
dp = [[0 for _ in range(21)] for _ in range(n-1)]
dp[0][ls[0]] = 1

for i in range(1,n-1):
    x = ls[i]
    for j in range(21):
        if dp[i-1][j]:
            if j - x >=0:
                dp[i][j-x] += dp[i-1][j]
            if j + x <= 20:
                dp[i][j+x] += dp[i-1][j]
print(dp[-1][ls[-1]])
# for i in range(n):
#     print(ls[i])
#     print(dp[i])