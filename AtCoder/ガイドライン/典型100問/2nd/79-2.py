n,m,q = map(int,input().split())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    dp[a][b] += 1

import itertools
dp = [list(itertools.accumulate(i)) for i in dp]
for i in range(n-1):
    for j in range(n):
        dp[i+2][j+1] += dp[i+1][j+1]

for _ in range(q):
    a,b = map(int,input().split())
    print(dp[b][b] + dp[a-1][a-1] - dp[b][a-1] - dp[a-1][b])