x1 = 0
x2 = 1
num_all =[]
num_odd = []
while x1 <= 10**6:
    x1 = x2*(x2+1)*(x2+2)//6
    num_all.append(x1)
    if x1%2==1:
        num_odd.append(x1)
    x2 += 1

import bisect
n = int(input())
dp = [[float("inf") for _ in range(2)] for _ in range(n+1)]
dp[0][0]=0
dp[0][1]=0
for i in range(n):
    all = num_all[:bisect.bisect_right(num_all,i+1)]
    odd = num_odd[:bisect.bisect_right(num_odd,i+1)]
    for j in all:
        dp[i+1][0] = min(dp[i+1][0],dp[i+1-j][0]+1)
    for j in odd:
        dp[i+1][1] = min(dp[i+1][1],dp[i+1-j][1]+1)

print(*dp[-1])