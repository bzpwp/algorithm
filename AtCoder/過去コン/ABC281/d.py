n,k,d = map(int,input().split())
ls = list(map(int,input().split()))

dp = [[[-1 for ___ in range(d)]for __ in range(k+1)]for _ in range(n+1)]

for i in range(n):
    dp[i][0][0]=0

for a in range(n):
    x = ls[a]
    y = x%d
    for b in range(0,min(a+1,k)):
        for c in range(d):
            if dp[a][b][c] >= 0:
                dp[a+1][b+1][(c+y)%d] = max(dp[a][b+1][(c+y)%d], dp[a][b][c]+x)

A =  dp[-1][-1][0]

# for i in dp[0]:
#     print(i)
for i in dp:
    print(i)
print(A)