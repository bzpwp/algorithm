n,k = map(int,input().split())
from collections import defaultdict
dd = defaultdict(int)
for i in range(k):
    a,b = map(int,input().split())
    dd[a]=b

M = 10000

dp = [[0 for _ in range(3)]for __ in range(n+2)]
if dd[1]:
    dp[2][dd[1]-1]=1
else:
    for i in range(3):
        dp[2][i]=1

for i in range(n-1):
    s = dp[i+2][0]+dp[i+2][1]+dp[i+2][2]
    if dd[i+2]:
        dp[i+3][dd[i+2]-1] = s
        if dp[i+1][dd[i+2]-1] and dp[i+2][dd[i+2]-1]:
            dp[i+3][dd[i+2]-1]-=dp[i+1][dd[i+2]-1]
            dp[i+3][dd[i+2]-1]+=dp[i][dd[i+2]-1]
        dp[i+3][dd[i+2]-1] %= M
    else:
        for j in range(3):
            dp[i+3][j] = s
            if dp[i+1][j] and dp[i+2][j]:
                dp[i+3][j]-=dp[i+1][j]
                dp[i+3][j]+=dp[i][j]
            dp[i+3][j]%=M

# for i in dp:
#     print(i)
print(sum(dp[-1])%M)