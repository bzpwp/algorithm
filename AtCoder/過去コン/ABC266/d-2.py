n = int(input())
dp = [[0]*5 for i in range(10**5+1)]

# dp = [[0]*5 for i in range(10+2)]
from collections import defaultdict

dd = defaultdict(int)

# for l in range(4):
#     for m in range(l+1,5):
#         dp[l][m]= -10**18
#         # dp[l][m]= -10


for k in range(n):
    t,x,a = map(int,input().split())
    dp[t][x] += a

for l in range(4):
    for m in range(l+1,5):
        dp[l][m]= -10**18
        # dp[l][m]= -10

# print(dp)
# print("-^----")

# for i in range(10+1):
for i in range(10**5):
    for j in range(5):
        if j == 0:
            dp[i+1][0]=max(dp[i][0],dp[i][1])+dp[i+1][j]
        elif j == 4:
            dp[i+1][4]=max(dp[i][4],dp[i][3])+dp[i+1][j]
        else:
            dp[i+1][j]=max(dp[i][j-1],dp[i][j],dp[i][j+1])+dp[i+1][j]
    # print(dp)
print(max(dp[10**5]))
# print(dp[10**5])