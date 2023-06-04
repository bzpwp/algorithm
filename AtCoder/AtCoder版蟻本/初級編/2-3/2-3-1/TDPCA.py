n = int(input())

ls = list(map(int,input().split()))
x = sum(ls)
dp = [[False]*(x+1) for _ in range(n+1)]

dp[0][0]=True
for i in range(1,n+1):
    y = ls[i-1]
    for j in range(x+1):
        if dp[i-1][j]:
            dp[i][j]=True
        elif j-y >=0:
            if dp[i-1][j-y]:
                dp[i][j]=True

z = 0
for k in range(x+1):
    if dp[n][k]:
        z+=1
print(z)