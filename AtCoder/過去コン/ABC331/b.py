n,s,m,l = map(int,input().split())

dp = [float("inf") for _ in range(n+1)]
dp[0] = 0

for i in range(n):
    dp[i+1] = s*(i//6 + 1)
# print(dp)
for i in range(n):
    if i <= 6:
        dp[i+1] = min(dp[i+1], m)
    else:
        dp[i+1] = min(dp[i+1], dp[i+1-8] + m)
# print(dp)

for i in range(n):
    if i <= 10:
        dp[i+1] = min(dp[i+1], l)
    else:
        dp[i+1] = min(dp[i+1], dp[i+1-12] + l)
print(dp[n])

# print(dp)