s = input()
M = 998244353
n = len(s)
if n == 1:
    print(0)
    exit()
dp = [[0 for _ in range(n+1)] for __ in range(n)]

if s[0] == ")":
    print(0)
    exit()
else:
    dp[0][1] = 1


for i in range(1,n):
    if s[i] == "(":
        for j in range(n):
            if dp[i-1][j]:
                dp[i][j+1] = dp[i-1][j]
    elif s[i] == ")":
        for j in range(1,n):
            if dp[i-1][j]:
                dp[i][j-1] = dp[i-1][j]
    else:
        for j in range(n):
            if dp[i-1][j]:
                dp[i][j+1] += dp[i-1][j]%M
                if j >= 1:
                    dp[i][j-1] += dp[i-1][j]%M
# for i in dp:
    # print(i)
print(dp[-1][0]%M)