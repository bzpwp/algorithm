
n = 5

dp = [[0] for i in range(n)]
M = 998244353
def sousa(x):
    return pow(x, M-2, M)*(x+1)

dp[0][0]+=1

print(dp)