n = int(input())
dp = [[0,0] for _ in range(n)]
dp[0]=[1,1]
a,b = list(map(int,input().split()))
M = 998244353
for i in range(n-1):
    a2,b2 = map(int,input().split())

    if a2!=a and a2!=b:
        dp[i+1][0]+=dp[i][0]+dp[i][1]
    elif a2!=a and a2==b:
        dp[i+1][0]+=dp[i][0]
    elif a2==a and a2!=b:
        dp[i+1][0]+=dp[i][1]
    else:
        dp[i+1][0] = 0
    dp[i+1][0]%=M

    if b2!=a and b2!=b:
        dp[i+1][1]+=dp[i][0]+dp[i][1]
    elif b2!=a and b2==b:
        dp[i+1][1]+=dp[i][0]
    elif b2==a and b2!=b:
        dp[i+1][1]+=dp[i][1]
    else:
        dp[i+1][1] = 0
    dp[i+1][0]%=M

    a,b = a2,b2

# print(dp)
print(sum(dp[-1])%M)