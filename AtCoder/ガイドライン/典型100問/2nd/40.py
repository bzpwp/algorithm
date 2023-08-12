n,k = map(int,input().split())
from collections import defaultdict
dd= defaultdict(int)
for i in range(k):
    a,b = map(int,input().split())
    dd[a] = b
dp = [[0 for _ in range(3)] for _ in range(n)]
if dd[1]:
    dp[0][dd[1]-1] = 1
else:
    for i in range(3):
        dp[0][i] = 1
if dd[2]:
    dp[1][dd[2]-1] = sum(dp[0])
else:
    for i in range(3):
        dp[1][i] = sum(dp[0])
print(dp)
for i in range(2,n):
    if dd[i+1]:
        if dp[i-1][dd[i+1]-1] == 0:
            dp[i][dd[i+1]-1] = sum(dp[i-1])
        else:
            dp[i][dd[i+1]-1] = sum(dp[i-1]) - dp[i-2][dd[i+1]-1]
        dp[i][dd[i+1]-1] %= 10000
    else:
        for j in range(3):
            if dp[i-1][j] == 0:
                 dp[i][j] = sum(dp[i-1]) 
            else:
                dp[i][j] = sum(dp[i-1]) - dp[i-2][j]
            dp[i][j] %= 10000
    print(dp)
print(sum(dp[-1])%10000)
