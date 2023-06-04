"""
LCS
"""
s1 = input()
s2 = input()

dp = [[0 for i in range(len(s2)+1)] for __ in range(len(s1)+1)]
dp[0][0]=0
for i in range(len(s1)):
    c1 = s1[i]
    for j in range(len(s2)):
        c2 = s2[j]
        if c1 == c2:
            dp[i+1][j+1]=max(dp[i][j]+1,dp[j+1][j],dp[i][j+1])
        else:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
            
print(dp[-1][-1])